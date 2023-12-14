select tv_genres.name, sum(tv_show_ratings.rate) as rating
from tv_show_genres
inner join tv_genres on tv_genres.id = tv_show_genres.genre_id
inner join tv_show_ratings on tv_show_genres.show_id = tv_show_ratings.show_id
group by tv_genres.name
order by
rating desc;
