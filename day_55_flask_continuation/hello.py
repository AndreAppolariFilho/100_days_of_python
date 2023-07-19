import random

from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)

def make_bold(function):
    def wrapper():
        return f"<b> {function()} </b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em> {function()} </em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<ul> {function()} </ul>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>'
@app.route('/<int:guessed_number>')
def guess_number(guessed_number):
    if guessed_number < random_number:
        return "<h1> too low, try again </h1>"
    if guessed_number > random_number:
        return "<h1> too high, try again </h1>"
    return "<h1> You found me! </h1>"

if __name__ == "__main__":
    app.run()
