select tv_genres.name as genre, count(tv_genres.name) as number_of_shows
from tv_genres
inner join tv_show_genres on tv_genres.id = tv_show_genres.genre_id
group by genre
order by number_of_shows desc;
