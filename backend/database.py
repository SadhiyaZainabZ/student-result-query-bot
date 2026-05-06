import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

# CLEAN OLD TABLES
cur.execute("DROP TABLE IF EXISTS studentss;")
cur.execute("DROP TABLE IF EXISTS student;")
cur.execute("DROP TABLE IF EXISTS students;")

# CREATE CORRECT TABLE
cur.execute("""
CREATE TABLE students (
    name TEXT,
    maths INTEGER,
    science INTEGER,
    english INTEGER,
    total INTEGER,
    attendance INTEGER
);
""")

# SAMPLE DATA
cur.execute("""
INSERT INTO students VALUES
('Meena', 95, 92, 94, 281, 96),
('Aisha', 90, 91, 89, 270, 95),
('Rahul', 80, 78, 82, 240, 85);
""")

conn.commit()
conn.close()