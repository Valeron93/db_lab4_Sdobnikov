import psycopg2
from matplotlib import pyplot as plt

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

vis_1, vis_2, vis_3 = [], [], []

with psycopg2.connect(**db) as conn:

    for l, q in zip([vis_1, vis_2, vis_3], [QUERY_1, QUERY_2, QUERY_3]):
        with conn.cursor() as cur:
            cur.execute(q)
            l.extend(cur.fetchall())

def q1():

    fig, ax = plt.subplots()
    authors = [author for author, _ in vis_1]
    counts = [count for _, count in vis_1]
    ax.set_title('Кількість віршів від автора')
    ax.bar(authors, counts)

def q2():
    fig, ax = plt.subplots()
    genres = [genre for genre, _ in vis_2]
    counts = [count for _, count in vis_2]

    ax.set_title('Розподіл віршів за жанром')
    ax.pie(counts, labels=genres, autopct='%1.1f%%')

def q3():
    fig, ax = plt.subplots()

    authors = [author for author, _ in vis_3]
    counts = [count for _, count in vis_3]

    ax.set_title('Кількість віршів від автора з жанром "Love"')
    ax.bar(authors, counts)

q1()
q2()
q3()

plt.show()
