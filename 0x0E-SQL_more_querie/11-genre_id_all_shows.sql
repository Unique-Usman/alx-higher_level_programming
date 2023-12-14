select tv_shows.title, tv_show_genres.genre_id
from tv_shows
left join tv_show_genres on tv_shows.id = tv_show_genres.genre_id
order by tv_shows.title asc, tv_show_genres.genre_id asc;
