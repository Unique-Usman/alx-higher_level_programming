-- Retrieve the count of TV shows for each genre,
-- ordering by the number of shows in descending order

SELECT tv_genres.name AS genre, COUNT(tv_genres.name) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
