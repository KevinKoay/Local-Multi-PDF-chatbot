import streamlit as st
import ollama
from utils.processor import get_pdf_text, get_text_chunks
from utils.vector_store import get_vectorstore
from utils.chat import get_rag_chain

def main():
    st.set_page_config(page_title="Multi-PDF Chatbot (Local)", page_icon=":books:")
    st.header("Chat with Manuals (Local AI)")

    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Initialize chain
    if "rag_chain" not in st.session_state:
        st.session_state.rag_chain = None

    # Sidebar
    with st.sidebar:
        st.subheader("Configuration")
        # Fetch available models
        try:
            models_info = ollama.list()
            # models_info['models'] is a list of objects in newer SDKs
            # We try to access .model or .name attribute
            model_names = []
            for m in models_info['models']:
                if hasattr(m, 'model'):
                    model_names.append(m.model)
                elif hasattr(m, 'name'):
                    model_names.append(m.name)
                else:
                    # Fallback for dicts
                    model_names.append(m.get('name', 'unknown'))
        except Exception as e:
            st.warning(f"Could not fetch models from Ollama: {e}")
            model_names = ["llama3", "mistral", "gemma:2b"] # Fallback


        model_name = st.selectbox("Select Ollama Model", model_names)
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader(
            "Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
            
        if st.button("Process"):
            if not pdf_docs:
                st.error("Please upload at least one PDF.")
            else:
                with st.spinner("Processing..."):
                    raw_text = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    st.write(f"Processed {len(text_chunks)} chunks.")
                    
                    vectorstore = get_vectorstore(text_chunks)
                    st.session_state.rag_chain = get_rag_chain(vectorstore, model_name)
                    st.success("Done!")

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Ask a question regarding your manuals:"):
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate response
        if st.session_state.rag_chain:
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                # Stream the response
                try:
                    for chunk in st.session_state.rag_chain.stream(prompt):
                        full_response += chunk
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                except Exception as e:
                    st.error(f"Error generating response: {e}")
                    
                st.session_state.messages.append({"role": "assistant", "content": full_response})
        else:
            if not pdf_docs:
                st.info("Please upload and process PDFs to start chatting.")
                

    # Move Download Button to the end so it captures the latest chat history
    with st.sidebar:
        # Download Chat History
        if st.session_state.messages:
            st.divider()
            chat_str = ""
            for msg in st.session_state.messages:
                chat_str += f"{msg['role'].upper()}: {msg['content']}\n\n"
            
            st.download_button(
                label="Download Chat History",
                data=chat_str,
                file_name="chat_history.txt",
                mime="text/plain"
            )

if __name__ == '__main__':
    main()
