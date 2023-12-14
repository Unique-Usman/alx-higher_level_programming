select tv_shows.title, tv_genres.name
from tv_show_genres
right join tv_g
enres on tv_show_genres.genre_id = tv_genres.id
right join tv_shows on tv_show_genres.show_id = tv_shows.id
order by tv_shows.title;
