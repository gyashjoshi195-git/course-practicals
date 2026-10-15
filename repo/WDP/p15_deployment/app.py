"""Deployment-ready Flask app (Practical 15): config from environment variables,
no debug mode, database path configurable, served by Gunicorn."""
import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, g

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")
DATABASE = os.environ.get("DATABASE_PATH", "students.db")


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, email TEXT NOT NULL, course TEXT NOT NULL)""")


init_db()   # runs on import so Gunicorn/WSGI servers get the table too


@app.route("/")
def index():
    students = get_db().execute("SELECT * FROM students ORDER BY id DESC").fetchall()
    return render_template("index.html", students=students)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        db = get_db()
        db.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
                   (request.form["name"], request.form["email"], request.form["course"]))
        db.commit()
        flash("Student added.", "success")
        return redirect(url_for("index"))
    return render_template("form.html", student=None)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    db = get_db()
    student = db.execute("SELECT * FROM students WHERE id = ?", (id,)).fetchone()
    if student is None:
        return redirect(url_for("index"))
    if request.method == "POST":
        db.execute("UPDATE students SET name=?, email=?, course=? WHERE id=?",
                   (request.form["name"], request.form["email"], request.form["course"], id))
        db.commit()
        flash("Student updated.", "success")
        return redirect(url_for("index"))
    return render_template("form.html", student=student)


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    db = get_db()
    db.execute("DELETE FROM students WHERE id = ?", (id,))
    db.commit()
    flash("Student deleted.", "warning")
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run()
