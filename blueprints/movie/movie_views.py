from flask import Blueprint, jsonify

from blueprints.movie.dao.movie_dao import get_by_title_query, range_release_years_query
from utils import get_one, get_all

movie_blueprint = Blueprint('movie_blueprint', __name__)


@movie_blueprint.get('/movie/<title>/')
def get_by_title(title):
    """
    Views для вывода фильмов по названию.
    :param title: Название фильма.
    :return: jsonify.
    """
    query = get_by_title_query(title)
    result = get_one(query)

    if result is None:
        return jsonify(status=404)

    movie = {
        "title": result['title'],
        "country": result['country'],
        "release_year": result['release_year'],
        "genre": result['listed_in'],
        "description": result['description'],
    }

    return jsonify(movie)


@movie_blueprint.get('/<from_year>/to/<to_year>/')
def range_release_years(from_year, to_year):
    """
    Views для вывода фильмов снятых в диапазоне дат.
    :param from_year: От этой даты.
    :param to_year: До этой даты.
    :return: jsonify.
    """
    query = range_release_years_query(from_year, to_year)

    result = []

    for item in get_all(query):
        result.append(
            {
                "title": item['title'],
                "release_year": item['release_year']
            }
        )

    return jsonify(result)
