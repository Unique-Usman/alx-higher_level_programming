select cities.id, cities.name, states.name
from cities
join states on cities.state_id = states.id
order by cities.id;
