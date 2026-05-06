import sqlite3

def run_query(sql):
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute(sql)
    result = cur.fetchall()

    conn.close()
    return result