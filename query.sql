-- Кількість віршів від кожного автора

SELECT
    Authors.author_name,
    COUNT(PoemsAuthors.poem_id) as poems_count
FROM Authors
LEFT JOIN PoemsAuthors ON Authors.author_id = PoemsAuthors.author_id
GROUP BY Authors.author_name;

-- Кількість віршів за жанром

SELECT
    Genres.genre_name,
    COUNT(Poems.poem_id) as poems_count
FROM Genres
LEFT JOIN Poems ON Genres.genre_id = Poems.genre_id
GROUP BY Genres.genre_name;

-- Скільки віршів з жанром "Love" написав автор

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