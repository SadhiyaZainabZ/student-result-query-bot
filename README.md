# 🎓 Student Result Query Bot

## 📌 Project Overview
This project is a GenAI-based chatbot that answers student-related queries such as marks, attendance, total scores, and class performance.

It uses a hybrid approach combining:
- Rule-based logic for accurate responses
- Retrieval-Augmented Generation (RAG) for flexible queries

---

## 🚀 Features
- Marks, Attendance, Total Queries
- Topper Identification
- Chart Visualization
- Query History (Saved Questions)
- AI-based Q&A using LangChain

---

## 🛠️ Tech Stack
- FastAPI (Backend)
- Streamlit (Frontend)
- LangChain
- FAISS
- HuggingFace (FLAN-T5)

---

## 📁 Project Structure
student-query-bot/
│
├── backend/
│ └── main.py
│
├── frontend/
│ └── app.py
│
├── data/
│ └── students.txt
│
├── faiss_index/
│
├── test_cases.txt
├── README.md

---

## ▶️ How to Run

### 1. Start Backend
uvicorn backend.main:app --reload

### 2. Start Frontend
streamlit run frontend/app.py

---

## 🧪 Test Cases
Refer to `test_cases.txt` for validation.

---

## 🧠 How It Works
1. User enters query in Streamlit UI  
2. FastAPI processes request  
3. Rule-based logic handles structured queries  
4. LangChain + FAISS handles AI queries  
5. Response is returned to UI  

---

## 👩‍💻 Author
Sadhiya Zainab  
CSE Department  

---

## 📌 Notes
- Dummy data is used  
- No sensitive information exposed  
