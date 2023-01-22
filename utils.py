import sqlite3


def get_all(query: str) -> list[dict]:
    """
    Функция получения всех данных из БД.
    :param query: Запрос.
    :return: Список словарей с данными.
    """
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row

        result = []

        for item in connection.execute(query).fetchall():
            result.append(dict(item))

        return result


def get_one(query: str) -> dict or str:
    """
    Функция получения одного значения из БД
    :param query: Запрос.
    :return: Словарь данных.
    """
    with sqlite3.connect('netflix.db') as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(query).fetchone()

        if result is None:
            return None
        else:
            return dict(result)


def get_movie_by_genre(type_movie: str, release_year: int, listed_in: str) -> list[dict]:
    """
    Функция по поиску фильма.
    :param type_movie: Тип фильма.
    :param release_year: Год выпуска.
    :param listed_in: Жанр фильма.
    :return: JSON с наименованием картины и ее описанием.
    """
    query = f"""
    SELECT title, description
    FROM netflix
    WHERE 'type' = '{type_movie}'
    AND release_year = {release_year}
    AND listed_in LIKE '%{listed_in}%'
    """

    result = []

    for item in get_all(query):
        result.append(
            {
                "title": item['title'],
                "description": item['description'],
            }
        )

    return result


def search_by_cast(name_1: str, name_2: str) -> list:
    """
    Функция по поиску актеров кто играет больше 2-х раз.
    :param name_1: Имя актера 1.
    :param name_2: Имя актера 2.
    :return: Список актеров кто играет больше 2-х раз.
    """
    query = f"""
        SELECT title, description
        FROM netflix
        WHERE 'cast' 
        LIKE '%{name_1}%'
        AND 'cast'
        LIKE '%{name_2}%'
        """

    cast = []
    set_cast = set()
    result = get_all(query)

    for item in result:
        for actor in item['cast'].split(','):
            cast.append(actor)

    for actor in cast:
        if cast.count(actor) > 2:
            set_cast.add(actor)

    return list(set_cast)


# test функции search_by_cast
# print(search_by_cast('Rose McIve', 'Ben Lamb'))
# print(search_by_cast('Jack Black', 'Dustin Hoffman'))
