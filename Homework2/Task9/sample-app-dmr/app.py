# Based on https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps
import os
import requests
import streamlit as st

st.set_page_config(page_title="Chatbot (aka ChatGPT)")
st.title("Chatbot via DMR")

DMR_BASE = os.getenv("DMR_BASE", "http://localhost:12434")
DMR_CHAT_PATH = os.getenv("DMR_CHAT_PATH", "/engines/llama.cpp/v1/chat/completions")
DMR_URL = f"{DMR_BASE.rstrip('/')}{DMR_CHAT_PATH}"
MODEL = os.getenv("DMR_MODEL", "ai/smollm2:135M-Q4_K_M")

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

    body = {
        "model": MODEL,
        "messages": st.session_state.messages,  # put all messages from the conversation
        # docs: higher values like 0.8 will make the output more random, while lower values like 0.2
        "temperature": 0.7,
        "stream": False, # waiting for full response
    }

    try:
        r = requests.post(DMR_URL, json=body, timeout=120)
        r.raise_for_status()
        data = r.json()

        reply = (
            data.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "")
            .strip()
        )
        if not reply:
            reply = "*No response text.*"
    except Exception as e:
        reply = f"Error calling at `{DMR_URL}`:\n\n`{e}`"

    # Show reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
