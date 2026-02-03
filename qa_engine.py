from langchain.vectorstores import FAISS

def build_qa_chain(docs, embeddings):
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore
