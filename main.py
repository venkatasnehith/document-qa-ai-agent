import streamlit as st
import PyPDF2

# ---------- PAGE SETUP ----------
st.set_page_config(page_title="Document Q&A AI Agent")
st.title("📄 Document Q&A AI Agent")

st.write("Upload a PDF and ask questions from its content (no paid API needed).")

# ---------- PDF TEXT EXTRACT ----------
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# ---------- FILE UPLOAD ----------
uploaded_file = st.file_uploader(
    "Upload PDF file",
    type=["pdf"]
)

if uploaded_file:
    with st.spinner("Reading PDF..."):
        pdf_text = extract_text_from_pdf(uploaded_file)

    st.success("PDF loaded successfully ✅")

    # ---------- QUESTION INPUT ----------
    question = st.text_input("Ask a question from the document:")

    if question:
        # SIMPLE LOGIC (KEYWORD SEARCH)
        sentences = pdf_text.split(".")
        matched = [s for s in sentences if question.lower() in s.lower()]

        st.subheader("Answer:")
        if matched:
            st.write(matched[0])
        else:
            st.write("❌ Answer not found in document.")
