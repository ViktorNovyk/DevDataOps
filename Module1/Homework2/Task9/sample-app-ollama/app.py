# Based on https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps
import os
import requests
import streamlit as st

st.set_page_config(page_title="Chatbot (aka ChatGPT)")
st.title("Chatbot via Ollama")

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
MODEL = os.getenv("SMOLLM2_MODEL", "smollm2:135m")

# initial state
if "messages" not in st.session_state:
    st.session_state.messages = []

# showing history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# waiting for messages
if prompt := st.chat_input("Ask me anything"):
    # showing user msg
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        r = requests.post(
            f"{OLLAMA_URL}/api/generate",
            json={"model": MODEL, "prompt": prompt, "stream": False},
            timeout=120,
        )
        r.raise_for_status()
        data = r.json()
        reply = data.get("response", "").strip() or "*No response text.*"
    except Exception as e:
        reply = f"Error calling at {OLLAMA_URL}: `{e}`"

    # show reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)