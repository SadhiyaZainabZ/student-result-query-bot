# 🎓 AI Student Result Query Bot

A FastAPI + SQLite + Streamlit + RAG (FAISS) based AI system that answers student-related queries like marks, topper, attendance, and class performance using natural language queries.

---

# 🚀 Features

- 🧠 Natural Language to SQL conversion
- 📊 Student marks visualization using charts
- 🏆 Topper detection system
- 📅 Attendance query support
- 🤖 RAG fallback using FAISS vector search
- ⚡ FastAPI backend API system
- 🎨 Streamlit chat-style frontend
- 🗄️ SQLite database integration
- 📜 Query history support
- 🧾 SQL query display
- 🔐 Basic login authentication system
- 📝 Logging system for queries and outputs
- 💡 AI-based result explanation feature

---

# 🏗️ Project Structure

```text
student-query-bot/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── intent.py
│   ├── rag.py
│   ├── sql_engine.py
│   ├── sql_query.py
│   ├── vector_store.py
│   ├── logger.py
│   ├── explainer.py
│
├── frontend/
│   └── app.py
│
├── data/
│   └── students.txt
│
├── faiss_index/
├── students.db
├── logs.txt
├── db_setup.py
├── test_cases.txt
├── requirements.txt
├── README.md
```

---

# 🗄️ Database

- SQLite database: `students.db`
- Table name: `students`

## Schema

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

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/SadhiyaZainabZ/student-query-bot.git
cd student-query-bot
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧱 Setup Database

Run:

```bash
python db_setup.py
```

This creates:

- `students.db`
- `students` table
- Sample student data

---

# 🔍 Create Vector Database

Run:

```bash
python backend/vector_store.py
```

This creates:

- `faiss_index/`

Used for:

- RAG retrieval
- AI fallback answering

---

# 🚀 Run Project

## Start FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## Start Streamlit Frontend

Open another terminal:

```bash
streamlit run frontend/app.py
```

Frontend opens automatically in browser.

---

# 🔐 Login Credentials

| Username | Password |
|---|---|
| admin | admin123 |

---

# 🧪 Example Queries

- marks of Meena
- marks of Aisha
- attendance of Rahul
- who is topper
- total marks of Rahul
- maths marks of Aisha
- science marks of Meena

---

# 📊 Features Implemented Across 3 Weeks

## ✅ Week 1

- SQLite database creation
- FastAPI backend setup
- Streamlit frontend setup
- FAISS vector store integration
- Sample dataset creation

---

## ✅ Week 2

- Rule-based SQL generation
- Intent detection system
- Safe SQL execution layer
- Dynamic chart generation
- Query history system
- SQL query display
- RAG fallback integration

---

## ✅ Week 3

- Login authentication system
- Improved chat UI
- Sidebar quick queries
- Loading spinner
- Logging system
- AI result explanation
- Better project architecture
- Final testing and documentation

---

# 🧠 Architecture Flow

```text
User Query
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
Intent Detection
    ↓
SQL Generator
    ↓
SQLite Database
    ↓
Response Formatter
    ↓
Chart + Explanation + Answer
```

---

# 🧠 Tech Stack

- FastAPI
- Streamlit
- SQLite
- LangChain
- HuggingFace Transformers
- FAISS
- Python

---

# 🧪 Test Cases

| Input | Expected Output |
|---|---|
| marks of meena | Correct marks displayed |
| attendance of aisha | Attendance shown |
| who is topper | Topper displayed |
| show chart | Bar chart generated |
| invalid query | Proper fallback/error |
| marks of rahul | Correct marks displayed |

---

# 📌 Future Improvements

- 🌐 Cloud deployment
- 🎤 Voice input support
- 📄 PDF report generation
- 👥 Multi-user authentication
- 🤖 OpenAI/Gemini API integration
- 🧠 Chat memory system

---

# 👨‍💻 Author

Sadhiya Zainab

GenAI Education Domain Project  
FastAPI + LangChain + Streamlit + FAISS

---

# 📜 License

This project is developed for educational and learning purposes.