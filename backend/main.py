from fastapi import FastAPI
from backend.sql_engine import rule_based_sql, clean_sql
from backend.sql_query import run_query
from backend.intent import detect_intent
from backend.rag import run_rag
from backend.logger import save_log
from backend.explainer import explain_result

app = FastAPI()

# -------------------------------
# 💾 QUERY HISTORY
# -------------------------------
query_history = []

# -------------------------------
# 🚀 HOME
# -------------------------------
@app.get("/")
def home():
    return {
        "message": "🎓 Student Bot Running (Week 3 Upgrade)"
    }

# -------------------------------
# 🚀 ASK ENDPOINT
# -------------------------------
@app.get("/ask")
def ask(query: str):

    # -------------------------------
    # SAVE HISTORY
    # -------------------------------
    query_history.append(query)
    query_history[:] = query_history[-10:]

    # -------------------------------
    # STEP 1 → DETECT INTENT
    # -------------------------------
    intent = detect_intent(query)

    # -------------------------------
    # STEP 2 → GENERATE SQL
    # -------------------------------
    sql = rule_based_sql(query)
    sql = clean_sql(sql)

    # -------------------------------
    # STEP 3 → STRUCTURED SQL FLOW
    # -------------------------------
    if intent in ["marks", "attendance", "topper"]:

        # -------------------------------
        # SQL VALIDATION
        # -------------------------------
        if not sql:
            return {
                "intent": intent,
                "error": "SQL not generated"
            }

        # -------------------------------
        # RUN QUERY
        # -------------------------------
        try:
            result = run_query(sql)

        except Exception as e:
            return {
                "intent": intent,
                "error": str(e),
                "sql": sql
            }

        # -------------------------------
        # NO DATA
        # -------------------------------
        if not result:
            return {
                "intent": intent,
                "answer": "No data found",
                "sql": sql
            }

        # =================================================
        # 📊 MARKS
        # =================================================
        if intent == "marks":

            m, s, e = result[0]

            answer = f"Maths {m}, Science {s}, English {e}"

            # ✅ SAVE LOG
            save_log(query, sql, answer)

            return {
                "intent": intent,
                "answer": answer,
                "explanation": explain_result(intent, result),
                "sql": sql,
                "chart": {
                    "marks": {
                        "maths": m,
                        "science": s,
                        "english": e
                    }
                }
            }

        # =================================================
        # 📅 ATTENDANCE
        # =================================================
        if intent == "attendance":

            attendance = result[0][0]

            answer = f"Attendance: {attendance}%"

            # ✅ SAVE LOG
            save_log(query, sql, answer)

            return {
                "intent": intent,
                "answer": answer,
                "explanation": explain_result(intent, result),
                "sql": sql
            }

        # =================================================
        # 🏆 TOPPER
        # =================================================
        if intent == "topper":

            name, total = result[0]

            answer = f"{name} is topper with {total} marks"

            # ✅ SAVE LOG
            save_log(query, sql, answer)

            return {
                "intent": intent,
                "answer": answer,
                "explanation": explain_result(intent, result),
                "sql": sql
            }

    # -------------------------------
    # STEP 4 → RAG FALLBACK
    # -------------------------------
    try:

        rag_answer = run_rag(query)

        # ✅ SAVE LOG
        save_log(query, "RAG", rag_answer)

        return {
            "intent": "general",
            "answer": rag_answer
        }

    except Exception as e:

        return {
            "intent": "general",
            "answer": "Unable to process query",
            "error": str(e)
        }

# -------------------------------
# 📜 HISTORY
# -------------------------------
@app.get("/history")
def history():

    return {
        "history": query_history
    }