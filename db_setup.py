import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Clean old tables
cur.execute("DROP TABLE IF EXISTS students;")

# Create table
cur.execute("""
CREATE TABLE students (
    name TEXT,
    maths INTEGER,
    science INTEGER,
    english INTEGER,
    total INTEGER,
    attendance INTEGER
)
""")

# Insert data
cur.execute("""
INSERT INTO students VALUES
('Meena', 95, 92, 94, 281, 96),
('Aisha', 90, 91, 89, 270, 95),
('Rahul', 80, 78, 82, 240, 85)
""")

conn.commit()
conn.close()

print("Database created successfully")