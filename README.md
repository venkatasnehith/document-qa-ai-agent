# document-qa-ai-agent
Perfect 👌
Here’s a **clean, professional, interview-ready `README.md`** you can **copy-paste directly** into your repo.

---

```md
# 📄 Document Q&A AI Agent (RAG System)

An **Enterprise-style Retrieval-Augmented Generation (RAG)** system that answers questions **strictly from uploaded PDF documents**, with **zero hallucination**.

This project is built using **Streamlit**, **FAISS**, **Sentence Transformers**, and **Groq LLM** — designed to be **interview-safe, production-aligned, and explainable**.

---

## 🚀 Key Features

- 📚 **PDF-only answers** (Source of truth = uploaded PDFs)
- 🔍 Semantic search using **FAISS + embeddings**
- 🧠 **LLM used only for enrichment**, not answering
- ❌ No hallucination, no external knowledge
- 🎨 Clean dark UI with readable white text
- 🤖 AI avatar + professional project layout

---

## 🧠 System Architecture (RAG)

### 🔒 Source of Truth
- Only the uploaded PDF files
- No internet or model knowledge used for answering

### 🔍 Retrieval Layer
- PDFs → text extraction
- Chunking with overlap
- Embeddings using `all-MiniLM-L6-v2`
- Vector search using **FAISS**

### 🧠 LLM (Groq) — Limited Role
The external LLM is used **only after retrieval**, for:

- ✍️ **Overview / summary**
- 🤖 **AI-style rephrased explanation**
- ⭐ **Important points extraction**

👉 The LLM **never answers directly** from its own knowledge.

---

## 🧩 Output Sections

For every valid question, the system generates:

1. **📄 Full Explanation (From PDFs)**  
   → Raw retrieved content (verbatim meaning)

2. **🧠 Overview**  
   → Short auto-summary generated from retrieved text

3. **🤖 AI-Style Rephrased Answer**  
   → Clear, professional rewrite (PDF content only)

4. **⭐ Important Points**  
   → Key bullet points extracted from the same text

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **PDF Parsing:** PyPDF2  
- **Embeddings:** Sentence Transformers  
- **Vector Store:** FAISS  
- **LLM:** Groq (LLaMA-3 models)  
- **Language:** Python  

---

## 📁 Project Structure

```

document-qa-ai-agent/
│
├── main.py              # Streamlit app (UI + pipeline)
├── pdf_loader.py        # PDF text extraction
├── embeddings.py        # Chunking & embeddings logic
├── qa_engine.py         # FAISS search & relevance filtering
├── README.md            # Project documentation
├── .gitignore
└── venv/

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/venkatasnehith/document-qa-ai-agent.git
cd document-qa-ai-agent
````

### 2️⃣ Create Virtual Environment (optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit PyPDF2 faiss-cpu sentence-transformers groq
```

### 4️⃣ Add Groq API Key

Set your API key (example for Windows):

```bash
setx GROQ_API_KEY "your_groq_api_key_here"
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

Open browser at:

```
http://localhost:8501
```

---

## 🧪 Example Use Cases

* Academic PDF Q&A
* Exam preparation from notes
* Technical document understanding
* Enterprise document search
* Interview-ready RAG demo project

---

## 🎯 Why This Project Is Interview-Safe

* Clear **RAG separation**
* No hallucination risk
* Explainable pipeline
* Proper relevance filtering
* Industry-standard tools (FAISS, embeddings)
* Clean Git history and structure

---

## 📌 Future Improvements

* Page number citation
* Highlight exact PDF sources
* Multi-PDF topic clustering
* PDF preview inside UI

---

## 👤 Author

**Venkat Snehith**
AI / ML Enthusiast
GitHub: [https://github.com/venkatasnehith](https://github.com/venkatasnehith)

---

⭐ If you like this project, consider starring the repository!

```

---


```
