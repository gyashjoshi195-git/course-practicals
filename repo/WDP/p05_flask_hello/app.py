from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/home")
def home():
    return render_template("index.html", title="Flask Project Structure")


@app.route("/user/<name>")
def user(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    app.run(debug=True)
