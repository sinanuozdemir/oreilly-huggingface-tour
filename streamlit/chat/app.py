import requests
import streamlit as st

st.title("ChatGPT-like clone with Llama 2")

HF_API_KEY = st.secrets["HF_API_KEY"]

API_URL = "https://sa0b44ky03zvbtds.us-east-1.aws.endpoints.huggingface.cloud"
headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


def query_llama_2(messages):
    system = '<<SYS>> You are a helpful assistant. You keep your answers short. <</SYS>>'
    prompt = ''
    for i, _message in enumerate(messages):
        if _message['role'] == 'user':
            if i == 0:
                prompt += f' <s>[INST] {system} {_message["content"]} [/INST]'
            else:
                prompt += f'<s>[INST] {_message["content"]} [/INST]'
        else:
            prompt += f' {_message["content"]} </s>'
    print(prompt)
    output = requests.post(API_URL, headers=headers, json={
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 128
        }
    })
    response = output.json()[0]['generated_text'].strip()
    return response


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = query_llama_2(
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )
        stream = st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
