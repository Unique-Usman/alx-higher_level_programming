-- Retrieve the titles of TV shows associated with the genre
-- "Comedy" and order them alphabetically

SELECT tv_shows.title
FROM tv_show_genres
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title;
