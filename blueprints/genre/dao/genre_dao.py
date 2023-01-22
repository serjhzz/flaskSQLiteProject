def get_movie_by_genre_query(genre):
    """
    Запрос к БД для поиска фильмов по жанру.
    :param genre: Значение жанра.
    :return: query.
    """
    query = f"""
    SELECT *
    FROM netflix
    WHERE listed_in LIKE '%{genre}%'
    ORDER BY date_added DESC 
    LIMIT 10
    """
    return query
