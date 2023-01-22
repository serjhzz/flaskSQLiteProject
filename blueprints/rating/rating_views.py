from flask import Blueprint, jsonify

from blueprints.rating.dao.rating_dao import get_movie_by_rating_query
from utils import get_all

rating_blueprint = Blueprint('rating_blueprint', __name__)


@rating_blueprint.get('/<value>/')
def get_movie_by_rating(value):
    """
    Views для вывода фильмов по рейтингу.
    :param value: Значение рейтинга ('children', 'family', 'adult')
    :return: jsonify.
    """
    query = get_movie_by_rating_query()

    if value == 'children':
        query += 'WHERE rating = "G"'
    elif value == 'family':
        query += 'WHERE rating = "G" or rating = "PG" or rating = "PG-13"'
    elif value == 'adult':
        query += 'WHERE rating = "G" or rating = "NC-17"'
    else:
        return jsonify(status=400)

    result = []

    for item in get_all(query):
        result.append(
            {
                "title": item['title'],
                "rating": item['rating'],
                "description": item['description'],
            }
        )

    return jsonify(result)
