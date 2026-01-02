# Deploying Local Multi-PDF Chatbot to Another Computer

To run this application on another computer, follow these steps:

## Prerequisites

1.  **Install Python**: Download and install Python (version 3.10 or higher recommended) from [python.org](https://www.python.org/).
2.  **Install Ollama**: Download and install Ollama from [ollama.com](https://ollama.com/).

## Setup Instructions

1.  **Copy Files**: Copy this entire project folder to the new computer.
    *   Ensure you have `app.py`, `requirements.txt`, and the `utils/` folder.

2.  **Open Terminal**: Open Command Prompt or PowerShell and navigate to the project folder:
    ```powershell
    cd path/to/your/folder
    ```

3.  **Install Dependencies**: Run the following command to install the required Python libraries:
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Download AI Model**: Pull the AI model you want to use (e.g., Llama 3) using Ollama:
    ```powershell
    ollama pull llama3
    ```

5.  **Run the App**: Start the application with this command:
    ```powershell
    python -m streamlit run app.py
    ```

6.  **Access the App**: The app should open automatically in your browser. If not, go to `http://localhost:8501`.
