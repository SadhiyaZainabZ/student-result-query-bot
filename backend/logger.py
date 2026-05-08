from datetime import datetime

def save_log(query, sql, answer):

    with open("logs.txt", "a", encoding="utf-8") as f:

        f.write(f"""
TIME: {datetime.now()}
QUERY: {query}
SQL: {sql}
ANSWER: {answer}
-----------------------------------
""")