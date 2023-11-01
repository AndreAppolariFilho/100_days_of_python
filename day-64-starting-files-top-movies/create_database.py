import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, request
db = sqlite3.connect("movies-collection.db")

cursor = db.cursor()
'''
cursor.execute("""
    CREATE TABLE
    movie (
        id INTEGER PRIMARY KEY,
        title varchar(250) NOT NULL UNIQUE,
        year INTEGER NOT NULL,
        description varchar(250) NOT NULL,
        rating DECIMAL NOT NULL,
        ranking INTEGER NOT NULL,
        review varchar(250) NOT NULL,
       img_url varchar(250) NOT NULL
    )""")
'''
#cursor.execute("""INSERT INTO movie VALUES(1, 'Phone Booth', 2002, "Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.", 7.3, 10, "My favourite character was the caller.", 'https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg')""")
#db.commit()
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
db = SQLAlchemy()
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

with app.app_context():
    db.create_all()

## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice.
new_movie = Movie(
     title="Phone Booth",
     year=2002,
     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
     rating=7.3,
     ranking=10,
     review="My favourite character was the caller.",
     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
second_movie = Movie(
     title="Avatar The Way of Water",
     year=2022,
     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
     rating=7.3,
     ranking=9,
     review="I liked the water.",
     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)
with app.app_context():
    db.session.add(new_movie)
    db.session.add(second_movie)
    db.session.commit()