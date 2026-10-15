"""Practical 3: SQLite connectivity and basic SQL operations."""
import sqlite3

conn = sqlite3.connect("college.db")     # creates the file if missing
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        name   TEXT NOT NULL,
        branch TEXT,
        marks  INTEGER
    )
""")

cur.execute("DELETE FROM students")      # start fresh for demo
cur.execute("INSERT INTO students (name, branch, marks) VALUES ('Yash', 'CSE', 85)")
cur.execute("INSERT INTO students (name, branch, marks) VALUES ('Amit', 'IT', 72)")
cur.execute("INSERT INTO students (name, branch, marks) VALUES ('Riya', 'CSE', 91)")
conn.commit()

print("All students:")
for row in cur.execute("SELECT * FROM students"):
    print(row)

print("\nCSE students with marks > 80:")
for row in cur.execute("SELECT name, marks FROM students WHERE branch='CSE' AND marks > 80"):
    print(row)

print("\nSorted by marks (desc):")
for row in cur.execute("SELECT name, marks FROM students ORDER BY marks DESC"):
    print(row)

cur.execute("SELECT COUNT(*), AVG(marks), MAX(marks) FROM students")
print("\nCount, Avg, Max:", cur.fetchone())

conn.close()
print("\nConnection closed.")
