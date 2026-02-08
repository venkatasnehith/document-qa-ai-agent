from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

def build_qa_chain(docs, embeddings, llm):
    # Create vector store
    vectorstore = FAISS.from_documents(docs, embeddings)

    # Create retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 5}  # top 5 chunks
    )

    # Create QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",   # simple + reliable
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
