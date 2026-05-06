import streamlit as st
import requests

st.set_page_config(page_title="Student Bot", layout="wide")

st.title("🎓 AI Student Result Query Bot")

if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.chat_input("Ask about marks, topper, attendance...")

if query:
    res = requests.get("http://127.0.0.1:8000/ask", params={"query": query})
    data = res.json()

    st.session_state.chat.append(("user", query))
    st.session_state.chat.append(("bot", data))

# -------------------------------
# CHAT UI
# -------------------------------
for role, msg in st.session_state.chat:

    if role == "user":
        st.chat_message("user").write(msg)

    else:
        with st.chat_message("assistant"):

            if isinstance(msg, dict):

                if "error" in msg:
                    st.error(msg["error"])

                if "sql" in msg:
                    st.code(msg["sql"], language="sql")

                if "answer" in msg:
                    st.success(msg["answer"])

                if "chart" in msg:
                    st.bar_chart(msg["chart"]["marks"])
                if "intent" in data:
                    st.info(f"Intent detected: {data['intent']}")