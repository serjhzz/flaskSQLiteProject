def get_by_title_query(title):
    """
    Запрос к БД для получения фильмов по названию.
    :param title: Название фильма.
    :return: query.
    """
    query = f"""
    SELECT * 
    FROM netflix
    WHERE title = '{title}'
    ORDER BY date_added DESC
    """
    return query


def range_release_years_query(from_year, to_year):
    """
    Запрос к БД для поиска фильмов снятых в диапазоне дат.
    :param from_year: От этой даты.
    :param to_year: До этой даты.
    :return: query.
    """
    query = f"""
    SELECT *
    FROM netflix
    WHERE release_year BETWEEN {from_year} AND {to_year}
    LIMIT 100
    """
    return query
