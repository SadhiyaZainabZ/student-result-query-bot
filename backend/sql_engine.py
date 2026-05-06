import re

# -------------------------------
# RULE BASED SQL (FAST + SAFE)
# -------------------------------
def rule_based_sql(query: str):
    q = query.lower()

    if "marks of" in q:
        name = query.split("of")[-1].strip().title()
        return f"SELECT maths, science, english FROM students WHERE name = '{name}'"

    if "topper" in q:
        return "SELECT name, total FROM students ORDER BY total DESC LIMIT 1"

    if "attendance of" in q:
        name = query.split("of")[-1].strip().title()
        return f"SELECT attendance FROM students WHERE name = '{name}'"

    return None


# -------------------------------
# SQL CLEANER (ANTI-HALLUCINATION)
# -------------------------------
def clean_sql(sql: str):
    sql = sql.strip()

    # fix wrong table names
    sql = re.sub(r"studentss+", "students", sql, flags=re.IGNORECASE)
    sql = re.sub(r"\bstudent\b", "students", sql, flags=re.IGNORECASE)

    # safety check
    if "students" not in sql.lower():
        return None

    # remove duplicate semicolons
    sql = sql.split(";")[0] + ";"

    return sql