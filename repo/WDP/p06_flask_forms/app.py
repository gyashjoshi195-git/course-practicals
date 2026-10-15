from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "change-this-secret"


@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()
        if not name or not email or not message:
            flash("All fields are required.", "danger")
            return render_template("form.html", form=request.form)
        return render_template("result.html", name=name, email=email, message=message)
    return render_template("form.html", form={})   # GET: show empty form


if __name__ == "__main__":
    app.run(debug=True)
