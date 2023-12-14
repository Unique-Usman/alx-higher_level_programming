select tv_shows.title
from tv_show_genres
left join tv_genres on tv_show_genres.genre_id = tv_genres.id
left join tv_shows on tv_show_genres.show_id = tv_shows.id
where tv_genres.name = "Comedy"
order by tv_shows.title;
