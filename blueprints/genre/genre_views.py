from flask import Blueprint, jsonify

from blueprints.genre.dao.genre_dao import get_movie_by_genre_query
from utils import get_all

genre_blueprint = Blueprint('genre_blueprint', __name__)


@genre_blueprint.get('/genere/<genre>/')
def get_movie_by_genre(genre):
    """
    Views для вывода фильмов по жанру.
    :param genre: Значение жанра.
    :return: jsonify.
    """
    query = get_movie_by_genre_query(genre)

    result = []

    for item in get_all(query):
        result.append(
            {
                "title": item['title'],
                "description": item['description']
            }
        )

    return jsonify(result)
