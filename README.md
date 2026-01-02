# Local Multi-PDF Chatbot 🤖📚

A privacy-focused, local RAG (Retrieval-Augmented Generation) application that allows you to chat with multiple PDF documents using local AI models. Built with **Streamlit**, **LangChain**, and **Ollama**.

## 🌟 Features

*   **100% Local Processing**: No data leaves your machine. Your documents stay private.
*   **Multi-PDF Support**: Upload and process multiple PDF manuals or documents at once.
*   **Local AI Models**: Integration with [Ollama](https://ollama.com) to use models like Llama 3, Mistral, or Gemma.
*   **Vector Search**: Uses FAISS and HuggingFace embeddings for efficient document retrieval.
*   **Chat History**: Interactive chat interface with the ability to **download your chat history**.

## 🛠️ Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **Framework**: [LangChain](https://www.langchain.com/) (LCEL)
*   **LLM Backend**: [Ollama](https://ollama.com/)
*   **Vector Store**: [FAISS](https://github.com/facebookresearch/faiss)
*   **Embeddings**: [HuggingFace](https://huggingface.co/) (`all-MiniLM-L6-v2`)

## 🚀 Getting Started

### Prerequisites

1.  **Python 3.10+** installed.
2.  **Ollama** installed and running.
    *   Download from [ollama.com](https://ollama.com).
    *   Pull a model: `ollama pull llama3`

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/KevinKoay/local-pdf-chatbot.git
    cd local-pdf-chatbot
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  Start the app:
    ```bash
    python -m streamlit run app.py
    ```

2.  Open your browser to `http://localhost:8501`.

3.  **Sidebar Setup**:
    *   Select your Ollama model from the dropdown.
    *   Upload your PDF documents.
    *   Click **Process**.

4.  **Chat**: Ask questions about your documents!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)
