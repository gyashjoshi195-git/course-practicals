"""Practical 4: SQLite CRUD using parameterized queries (? placeholders).
Parameterized queries prevent SQL injection."""
import sqlite3

DB = "crud_demo.db"


def get_conn():
    return sqlite3.connect(DB)


def init_db():
    with get_conn() as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, email TEXT UNIQUE, course TEXT)""")


def create(name, email, course):
    with get_conn() as conn:
        cur = conn.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
                           (name, email, course))
        return cur.lastrowid


def read_all():
    with get_conn() as conn:
        return conn.execute("SELECT * FROM students").fetchall()


def read_one(student_id):
    with get_conn() as conn:
        return conn.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()


def update(student_id, name, email, course):
    with get_conn() as conn:
        cur = conn.execute("UPDATE students SET name=?, email=?, course=? WHERE id=?",
                           (name, email, course, student_id))
        return cur.rowcount


def delete(student_id):
    with get_conn() as conn:
        cur = conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
        return cur.rowcount


if __name__ == "__main__":
    init_db()
    with get_conn() as c:
        c.execute("DELETE FROM students")
    sid = create("Yash", "yash@example.com", "CSE")
    create("Amit", "amit@example.com", "IT")
    print("After CREATE:", read_all())
    print("READ one    :", read_one(sid))
    update(sid, "Yash Patel", "yash@example.com", "Computer Engg")
    print("After UPDATE:", read_one(sid))
    delete(sid)
    print("After DELETE:", read_all())
