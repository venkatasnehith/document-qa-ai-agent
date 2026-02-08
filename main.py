import streamlit as st
import PyPDF2
import numpy as np
import faiss
import re
import os
from sentence_transformers import SentenceTransformer

# Optional LLM (Groq)
from groq import Groq

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Document Q&A AI Agent",
    page_icon="🤖",
    layout="centered"
)

# ================= UI STYLE =================
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #39ff14 0%, #0b1f0b 45%, #000000 100%);
    color: white;
}
.card {
    background: rgba(0,0,0,0.85);
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 0 20px rgba(57,255,20,0.5);
}
input {
    color: white !important;
    background: black !important;
    border: 2px solid #39ff14 !important;
    font-size: 18px !important;
}
.answer-box {
    background: rgba(0,0,0,0.9);
    padding: 20px;
    border-radius: 12px;
    margin-top: 10px;
}
h1,h2,h3,p,li {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
<div class="card" align="center">
    <img src="https://cdn-icons-png.flaticon.com/512/4712/4712109.png" width="50">
    <h2>Document Q&A AI Agent</h2>
    <p>Enterprise-Style Retrieval-Augmented System</p>
</div>
""", unsafe_allow_html=True)

# ================= PDF FUNCTIONS =================
def extract_text(pdf):
    reader = PyPDF2.PdfReader(pdf)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + " "
    return text.lower()

def chunk_text(text, size=300, overlap=100):
    words = text.split()
    chunks = []
    for i in range(0, len(words), size - overlap):
        chunks.append(" ".join(words[i:i+size]))
    return chunks

# ================= GROQ SAFE WRAPPER =================
def groq_safe(prompt):
    try:
        client = Groq()
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",  # ✅ WORKING MODEL
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=400
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ LLM Error: {str(e)}"



# ================= FILE UPLOAD =================
uploaded_files = st.file_uploader(
    "📤 Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Reading PDFs..."):
        full_text = ""
        for f in uploaded_files:
            full_text += extract_text(f)

    st.success("PDFs loaded successfully ✅")

    chunks = chunk_text(full_text)

    embedder = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = embedder.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    question = st.text_input("Ask a question")

    if question:
      with st.spinner("Searching PDFs... 🤖"):

        # 1️⃣ Encode question
        q_emb = embedder.encode([question])

        # 2️⃣ FAISS search
        distances, indices = index.search(np.array(q_emb), k=12)

        # 3️⃣ RELEVANCE CHECK (MUST COME FIRST)
        best_distance = distances[0][0]   # ✅ THIS WAS MISSING
        RELEVANCE_THRESHOLD = 0.85        # adjust if needed

        if best_distance > RELEVANCE_THRESHOLD:
            st.error("❌ Question is NOT related to the uploaded PDFs.")
            st.info("This system answers strictly from the uploaded documents.")
            st.stop()

        # 4️⃣ ONLY NOW build answer from PDFs
        pdf_answer = "\n\n".join(chunks[i] for i in indices[0])

        # 5️⃣ Show PDF answer
        st.subheader("📄 Full Explanation (From PDFs)")
        st.markdown(
            f"<div class='answer-box'>{pdf_answer}</div>",
            unsafe_allow_html=True
        )

        # 6️⃣ LLM enrichment (SAFE – PDF ONLY)
        overview = groq_safe(f"Summarize briefly:\n{pdf_answer}")
        points = groq_safe(f"Give 5 key points:\n{pdf_answer}")
        rephrase = groq_safe(f"Rewrite clearly:\n{pdf_answer}")

        st.subheader("🧠 Overview")
        st.markdown(
            f"<div class='answer-box'>{overview}</div>",
            unsafe_allow_html=True
        )

        st.subheader("⭐ Important Points")
        st.markdown(
            f"<div class='answer-box'>{points}</div>",
            unsafe_allow_html=True
        )

        st.subheader("🤖 AI-Style Rephrased Answer")
        st.markdown(
            f"<div class='answer-box'>{rephrase}</div>",
            unsafe_allow_html=True
        )
