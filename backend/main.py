from fastapi import FastAPI
from backend.sql_engine import rule_based_sql, clean_sql
from backend.sql_query import run_query
from backend.intent import detect_intent
from backend.rag import run_rag

app = FastAPI()

query_history = []

# -------------------------------
# HOME
# -------------------------------
@app.get("/")
def home():
    return {"message": "Student Bot Running (Week 2 Upgrade)"}

# -------------------------------
# ASK ENDPOINT
# -------------------------------
@app.get("/ask")
def ask(query: str):

    query_history.append(query)
    query_history[:] = query_history[-10:]

    # -------------------------------
    # STEP 1: INTENT DETECTION
    # -------------------------------
    intent = detect_intent(query)

    # -------------------------------
    # STEP 2: SQL GENERATION (RULE BASED)
    # -------------------------------
    sql = rule_based_sql(query)
    sql = clean_sql(sql)

    # -------------------------------
    # STEP 3: SQL FLOW (structured handling)
    # -------------------------------
    if intent in ["marks", "attendance", "topper"]:

        if not sql:
            return {
                "intent": intent,
                "error": "SQL not generated"
            }

        try:
            result = run_query(sql)
        except Exception as e:
            return {
                "intent": intent,
                "error": str(e),
                "sql": sql
            }

        if not result:
            return {
                "intent": intent,
                "answer": "No data found",
                "sql": sql
            }

        # ---------------- MARKS ----------------
        if intent == "marks":
            m, s, e = result[0]
            return {
                "intent": intent,
                "answer": f"Maths {m}, Science {s}, English {e}",
                "sql": sql,
                "chart": {
                    "marks": {
                        "maths": m,
                        "science": s,
                        "english": e
                    }
                }
            }

        # ---------------- ATTENDANCE ----------------
        if intent == "attendance":
            return {
                "intent": intent,
                "answer": f"Attendance: {result[0][0]}%",
                "sql": sql
            }

        # ---------------- TOPPER ----------------
        if intent == "topper":
            name, total = result[0]
            return {
                "intent": intent,
                "answer": f"{name} is topper with {total} marks",
                "sql": sql
            }

    # -------------------------------
    # STEP 4: FALLBACK → RAG (GENAI)
    # -------------------------------
    try:
        rag_answer = run_rag(query)
        return {
            "intent": "general",
            "answer": rag_answer
        }
    except:
        return {
            "intent": "general",
            "answer": "Unable to process query"
        }


# -------------------------------
# HISTORY
# -------------------------------
@app.get("/history")
def history():
    return {"history": query_history}