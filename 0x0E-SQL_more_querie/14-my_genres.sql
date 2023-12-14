 select tv_genres.name
from tv_genres
left join tv_show_genres on tv_genres.id = tv_show_genres.genre_id
left join tv_shows on tv_shows.id = tv_show_genres.show_id
where tv_shows.title = "Dexter"
order by name asc;
