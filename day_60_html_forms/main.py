from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":

        return render_template(
            "login.html",
            username=request.form["username"],
            password=request.form["password"]
        )


if __name__ == "__main__":
    app.run(debug=True)
