from flask import Flask

from blueprints.movie.movie_views import movie_blueprint
from blueprints.rating.rating_views import rating_blueprint
from blueprints.genre.genre_views import genre_blueprint

app = Flask(__name__)
app.register_blueprint(movie_blueprint)
app.register_blueprint(rating_blueprint)
app.register_blueprint(genre_blueprint)


@app.route('/')
def home_page():
    return 'Это главная страница'




if __name__ == '__main__':
    app.run()
