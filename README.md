# 🎓 AI Student Result Query Bot

A FastAPI + SQLite + Streamlit + RAG (FAISS) based AI system that answers student-related queries like marks, topper, and attendance using natural language.

---

## 🚀 Features

- 🧠 Natural language to SQL conversion
- 📊 Student marks visualization
- 🏆 Topper detection system
- 📅 Attendance queries
- 🤖 RAG fallback using FAISS vector search
- ⚡ FastAPI backend
- 🎨 Streamlit chat-style frontend
- 🗄️ SQLite database integration

---

## 🏗️ Project Structure
student-query-bot/
│
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── intent.py
│ ├── rag.py
│ ├── sql_engine.py
│ ├── sql_query.py
│ ├── vector_store.py
│
├── frontend/
│ └── app.py
│
├── students.db
├── faiss_index/
├── db_setup.py
├── test_cases.txt
├── requirements.txt

---

## 🗄️ Database

- SQLite database: `students.db`
- Table: `students`

### Schema:

```sql
students(
    name TEXT,
    maths INTEGER,
    science INTEGER,
    english INTEGER,
    total INTEGER,
    attendance INTEGER
)
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/student-query-bot.git
cd student-query-bot

pip install -r requirements.txt
```

---

## 🧱 Setup Database

```bash
python db_setup.py
```

---

## 🚀 Run Project

### Start Backend

```bash
uvicorn backend.main:app --reload
```

### Start Frontend

```bash
streamlit run frontend/app.py
```

---

## 🧪 Example Queries

- marks of Meena  
- marks of Aisha  
- who is topper  
- attendance of Meena  
- attendance of Aisha  

---

## 🧠 Tech Stack

- FastAPI  
- Streamlit  
- SQLite  
- LangChain  
- HuggingFace Transformers  
- FAISS  

---

## 📌 Future Improvements

- Chat memory system  
- Multi-user login  
- Cloud deployment  
- Voice input support  

---

## 👨‍💻 Author

AI Student Query Bot Project (Week 2 GenAI Learning Project)
