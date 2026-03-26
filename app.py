import streamlit as st
from main import run_agent

# Page config
st.set_page_config(page_title="Research Agent", layout="wide")

st.title("🤖 Research Agent")

# Session memory (chat history)
if "history" not in st.session_state:
    st.session_state.history = []

# Chat input
query = st.chat_input("Ask something...")

# When user enters query
if query:
    with st.spinner("Thinking..."):
        response = run_agent(query)

    # Save history
    st.session_state.history.append(("user", query))
    st.session_state.history.append(("assistant", response))

# Display chat history
for role, message in st.session_state.history:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)