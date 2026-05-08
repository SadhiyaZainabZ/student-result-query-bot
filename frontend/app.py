import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="AI Student Bot",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------
# LOGIN SYSTEM
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == "admin" and password == "admin123":
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid credentials")

    st.stop()

# -------------------------------
# HEADER
# -------------------------------
st.title("🎓 AI Student Result Query Bot")

st.markdown("""
Ask questions like:
- marks of Meena
- attendance of Aisha
- who is topper
""")

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("📌 Quick Queries")

example_queries = [
    "marks of Meena",
    "marks of Aisha",
    "attendance of Meena",
    "attendance of Aisha",
    "who is topper"
]

for q in example_queries:
    if st.sidebar.button(q):
        st.session_state.selected_query = q

# -------------------------------
# CLEAR CHAT
# -------------------------------
if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.chat = []
    st.rerun()

# -------------------------------
# CHAT STORAGE
# -------------------------------
if "chat" not in st.session_state:
    st.session_state.chat = []

# -------------------------------
# CHAT INPUT
# -------------------------------
query = st.chat_input("Ask your query...")

if "selected_query" in st.session_state:
    query = st.session_state.selected_query
    del st.session_state.selected_query

# -------------------------------
# SEND QUERY
# -------------------------------
if query:

    st.session_state.chat.append(("user", query))

    with st.spinner("Generating response..."):

        try:
            res = requests.get(
                "http://127.0.0.1:8000/ask",
                params={"query": query}
            )

            data = res.json()

            st.session_state.chat.append(("bot", data))

        except Exception as e:
            st.session_state.chat.append(
                ("bot", {"error": str(e)})
            )

# -------------------------------
# DISPLAY CHAT
# -------------------------------
for role, msg in st.session_state.chat:

    if role == "user":
        st.chat_message("user").write(msg)

    else:

        with st.chat_message("assistant"):

            if isinstance(msg, dict):

                # ERROR
                if "error" in msg:
                    st.error(msg["error"])

                # SQL
                if "sql" in msg:
                    st.subheader("🧾 SQL Query")
                    st.code(msg["sql"], language="sql")

                # ANSWER
                if "answer" in msg:
                    st.success(msg["answer"])

                # ✅ EXPLANATION
                if "explanation" in msg:
                    st.info(msg["explanation"])

                # CHART
                if "chart" in msg:

                    st.subheader("📊 Marks Chart")

                    df = pd.DataFrame(msg["chart"]).T

                    st.bar_chart(df)

            else:
                st.write(msg)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("🚀 Week 3 GenAI Project | FastAPI + Streamlit + LangChain + FAISS")