from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index_card.html")

if __name__ == "__main__":
    app.run()
