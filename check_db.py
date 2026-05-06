import sqlite3

conn = sqlite3.connect("students.db")  # OR data/students.db if you used that
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in DB:", cur.fetchall())

conn.close()