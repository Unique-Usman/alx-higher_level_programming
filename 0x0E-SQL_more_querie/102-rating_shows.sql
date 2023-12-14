select tv_shows.title, sum(tv_show_ratings.rate) as rating
from tv_show_ratings
inner join tv_shows on tv_show_ratings.show_id = tv_shows.id
group by tv_shows.title
order by rating desc;
