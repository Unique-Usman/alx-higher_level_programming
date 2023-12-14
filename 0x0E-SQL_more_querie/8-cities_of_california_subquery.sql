select id, name from cities where state_id=(select id
from states
where name = "California") order by cities.id asc;
