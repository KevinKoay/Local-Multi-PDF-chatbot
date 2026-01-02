from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os

def get_vectorstore(text_chunks, save_path="faiss_index"):
    """
    Creates a FAISS vector store from text chunks using local HuggingFace embeddings
    and saves it locally.
    """
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Create vector store
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    
    # Save locally
    vectorstore.save_local(save_path)
    
    return vectorstore

def load_vectorstore(save_path="faiss_index"):
    """
    Loads a FAISS vector store from local path. 
    Returns None if path doesn't exist.
    """
    if os.path.exists(save_path):
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        # allow_dangerous_deserialization is required for loading pickled files 
        # (trusted source since we created it)
        vectorstore = FAISS.load_local(save_path, embeddings, allow_dangerous_deserialization=True)
        return vectorstore
    return None
