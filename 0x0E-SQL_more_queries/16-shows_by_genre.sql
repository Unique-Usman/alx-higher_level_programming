-- This query retrieves information about TV shows,
-- their genres, and sorts them by title.

SELECT *
FROM tv_show_genres
RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title;
