# ChatGPT-like Clone with Llama 2

This README provides instructions on how to run a Streamlit application that mimics the behavior of ChatGPT, using Llama 2 as the underlying language model. Below, you'll find the necessary steps and explanations to get your application up and running.

## Prerequisites

Before running the application, ensure you have the following prerequisites:

- Python installed on your system.
- An active internet connection.
- A Hugging Face API key.

## Installation

1. **Install Required Packages**:
   You need to install Streamlit and Requests. You can do this via pip:

```bash
pip install -r requirements.txt
```

## Running the Application
 
### Set up Streamlit Secrets:
In your Streamlit app settings, add your Hugging Face API key as a secret. The key should be named HF_API_KEY.

### Start the Streamlit Server:
Run:

```bash
streamlit run app.py
```

## Code Explanation

- `st.title`: Sets the title of the web application.

- `HF_API_KEY`: Retrieves the Hugging Face API key from Streamlit secrets.

- `API_URL`: The endpoint for the Hugging Face Llama 2 model.

- `headers`: Necessary HTTP headers for the API request.

- `query_llama_2`: A function that constructs the prompt for the Llama 2 model and gets the response.

- `st.session_state`: Streamlit's way of maintaining state in the application.

- `st.chat_message`, `st.markdown`, `st.chat_input`: Streamlit functions for handling chat interface elements.
