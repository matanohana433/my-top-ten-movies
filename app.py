from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import DecimalField
from wtforms.validators import DataRequired, Length, NumberRange
import requests
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)



app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
Bootstrap5(app)


class RateMovieForm(FlaskForm):
    movie_rating = DecimalField('Your Rating out of 10 e.g. 7.5', validators=[DataRequired(), NumberRange(min=0, max=10)])
    movie_review = StringField('Your Review', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired(), Length(min=2)])
    submit = SubmitField("Add Movie")


ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
API_KEY = os.environ.get("API_KEY")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

def search_movies(query):
    url = f"https://api.themoviedb.org/3/search/movie?"

    params = {
        "query": query
    }
    response = requests.get(url, headers=headers, params=params)
    movies_data = response.json()['results']
    movies_result = [{"id": movie["id"], "title": movie["title"], "release_date": movie["release_date"]} for movie in movies_data]
    return movies_result



@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating).all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)



@app.route("/edit/<int:_id>", methods=["POST", "GET"])
def edit(_id):
    edit_form = RateMovieForm()
    selected_movie = Movie.query.filter_by(id=_id).first()
    if edit_form.is_submitted() and edit_form.validate_on_submit():
        selected_movie.rating = round(edit_form.movie_rating.data, 1)
        selected_movie.review = edit_form.movie_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=selected_movie, form=edit_form)

@app.route("/delete/<int:_id>")
def delete(_id):
    movie_to_delete = Movie.query.filter_by(id=_id).first()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["POST", "GET"])
def add():
    add_form = AddMovieForm()
    if add_form.is_submitted() and add_form.validate_on_submit():
        results = search_movies(query=add_form.movie_title.data)
        return render_template("select.html", movies=results)
    return render_template("add.html", form=add_form)

@app.route("/add/<int:_id>")
def add_to_db(_id):
    url = f"https://api.themoviedb.org/3/movie/{_id}?"
    response = requests.get(url, headers=headers)
    movie_data = response.json()
    new_movie = Movie(title=movie_data['title'], year=int(movie_data['release_date'][:4]), description=movie_data['overview'][:499], img_url=f"https://image.tmdb.org/t/p/w500" + movie_data['poster_path'])
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', _id=new_movie.id))



if __name__ == '__main__':
    app.run(debug=True)
