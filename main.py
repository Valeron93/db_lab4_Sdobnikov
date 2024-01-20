import psycopg2

db = {
    'dbname': 'valeron',
    'user': 'postgres',
    'password': '',
    'host': 'localhost',
    'port': '5432',
}

QUERY_1 = """
SELECT
    Authors.author_name,
COUNT(PoemsAuthors.poem_id) as poems_count
FROM Authors
LEFT JOIN PoemsAuthors ON Authors.author_id = PoemsAuthors.author_id
GROUP BY Authors.author_name;"""

QUERY_2 = """
SELECT
    Genres.genre_name,
    COUNT(Poems.poem_id) as poems_count
FROM Genres
LEFT JOIN Poems ON Genres.genre_id = Poems.genre_id
GROUP BY Genres.genre_name;
"""

QUERY_3 = """
SELECT
    Authors.author_name,
    COUNT(PoemsAuthors.poem_id) as poems_count
FROM Authors
LEFT JOIN PoemsAuthors ON Authors.author_id = PoemsAuthors.author_id
LEFT JOIN Poems ON PoemsAuthors.poem_id = Poems.poem_id
LEFT JOIN Genres ON Poems.genre_id = Genres.genre_id
WHERE
    Genres.genre_name = 'Love'
GROUP BY
    Authors.author_name;
"""

with psycopg2.connect(**db) as conn:

    with conn.cursor() as cur:
        cur.execute(QUERY_1)
        result = cur.fetchall()

        print("Кількість віршів від кожного автора")
        print(*result, sep='\n', end='\n\n')

    with conn.cursor() as cur:
        cur.execute(QUERY_2)
        result = cur.fetchall()

        print("Кількість віршів за жанром")
        print(*result, sep='\n', end='\n\n')
    
    with conn.cursor() as cur:
        cur.execute(QUERY_3)
        result = cur.fetchall()

        print("Скільки віршів з жанром \"Love\" написав автор")
        print(*result, sep='\n', end='\n\n')

