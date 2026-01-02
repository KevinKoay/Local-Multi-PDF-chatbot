from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

def get_vectorstore(text_chunks):
    """
    Creates a FAISS vector store from text chunks using local HuggingFace embeddings.
    """
    # Initialize HuggingFace embeddings (runs locally)
    # "all-MiniLM-L6-v2" is a good balance of speed and performance for CPU
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Create vector store
    # This will process the chunks and embed them.
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    
    return vectorstore
