-- Selects city ID, city name, and state name
SELECT cities.id, cities.name, states.name
FROM cities
-- Joins the cities table with the states table based on the state_id and id columns
JOIN states ON cities.state_id = states.id
-- Orders the result set by city ID in ascending order
ORDER BY cities.id;

