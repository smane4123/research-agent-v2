import streamlit as st
from main import run_agent

st.set_page_config(page_title="Research Agent", layout="wide")

st.title("🤖 Research Agent")

if "history" not in st.session_state:
    st.session_state.history = []

query = st.chat_input("Ask something...")

if query:
    with st.spinner("Thinking..."):
        response = run_agent(query)

    st.session_state.history.append(("user", query))
    st.session_state.history.append(("assistant", response))

for role, message in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)