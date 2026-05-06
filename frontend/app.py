import streamlit as st
import requests
import pandas as pd

st.title("🎓 Student Result Query Bot")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    res = requests.get("http://127.0.0.1:8000/ask", params={"query": query})
    data = res.json()

    # 📊 Chart
    if "chart" in data:
        st.subheader("📊 Student Marks Chart")
        df = pd.DataFrame(data["chart"]).T
        st.bar_chart(df[["maths", "science", "english"]])

    # 🤖 Answer
    elif "answer" in data:
        st.subheader("Answer:")
        st.write(data["answer"])

# -------------------------------
# 📜 SHOW HISTORY
# -------------------------------
st.subheader("📜 Query History")

hist = requests.get("http://127.0.0.1:8000/history").json()

for q in hist["history"]:
    st.write("•", q)