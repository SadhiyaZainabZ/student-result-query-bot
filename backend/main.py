from fastapi import FastAPI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
from langchain.prompts import PromptTemplate

app = FastAPI()

# -------------------------------
# STEP 0: STRUCTURED DATA
# -------------------------------
students_data = {
    "aisha": {"maths": 90, "science": 85, "english": 88, "total": 263, "attendance": 92},
    "meena": {"maths": 95, "science": 92, "english": 94, "total": 281, "attendance": 96},
    "rahul": {"maths": 80, "science": 78, "english": 82, "total": 240, "attendance": 85}
}

# -------------------------------
# 💾 QUERY HISTORY (NEW FEATURE)
# -------------------------------
query_history = []

# -------------------------------
# STEP 1: PROMPT
# -------------------------------
prompt_template = """
You are a student result assistant.

Use the given data to answer the question.

Context:
{context}

Question:
{question}

Rules:
- Always answer in a full sentence
- Include student name
- Do NOT include other students
"""

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# -------------------------------
# STEP 2: LOAD DB
# -------------------------------
embeddings = HuggingFaceEmbeddings()

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# -------------------------------
# STEP 3: MODEL
# -------------------------------
pipe = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=120,
    do_sample=False
)

llm = HuggingFacePipeline(pipeline=pipe)

# -------------------------------
# STEP 4: QA CHAIN
# -------------------------------
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever(search_kwargs={"k": 1}),
    chain_type="stuff",
    chain_type_kwargs={"prompt": PROMPT},
    return_source_documents=False
)

# -------------------------------
# STEP 5: ROUTES
# -------------------------------
@app.get("/")
def home():
    return {"message": "🎓 Student Result Query Bot Running"}

@app.get("/ask")
def ask(query: str):
    try:
        q = query.lower()

        # 💾 SAVE QUERY
        query_history.append(query)

        # 📊 CHART FEATURE
        if "chart" in q or "graph" in q or "visualize" in q:
            return {"chart": students_data}

        # 🏆 TOPPER FEATURE
        if "topper" in q or "highest" in q:
            topper = max(students_data, key=lambda x: students_data[x]["total"])
            marks = students_data[topper]["total"]
            return {"answer": f"{topper.capitalize()} is the topper with {marks} marks."}

        # 🔍 DETECT STUDENT
        student = None
        for name in students_data:
            if name in q:
                student = name
                break

        # 🎯 STUDENT-SPECIFIC LOGIC
        if student:
            data = students_data[student]

            if "attendance" in q:
                return {"answer": f"{student.capitalize()}'s attendance is {data['attendance']}%."}

            if "total" in q:
                return {"answer": f"{student.capitalize()}'s total marks are {data['total']}."}

            if "marks" in q:
                return {
                    "answer": f"{student.capitalize()} scored {data['maths']} in Maths, {data['science']} in Science, and {data['english']} in English."
                }

        # 🤖 RAG FALLBACK
        raw_answer = qa.run(query)
        return {"answer": raw_answer.strip()}

    except Exception as e:
        return {"error": str(e)}

# -------------------------------
# 📜 HISTORY ROUTE (NEW)
# -------------------------------
@app.get("/history")
def get_history():
    return {"history": query_history}