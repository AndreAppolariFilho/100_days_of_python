import random
import requests
from flask import Flask, render_template
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    return render_template("index.html", greetings="Hello World!", year=year)


@app.route('/guess/<name>')
def guess(name):
    parameters = {
        "name":name
    }
    age = requests.get(url="https://api.agify.io/",params=parameters).json()["age"]
    gender = requests.get(url="https://api.genderize.io/",params=parameters).json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)


