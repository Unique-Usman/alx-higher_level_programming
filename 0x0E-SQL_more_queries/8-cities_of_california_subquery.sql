-- Selects the id and name of cities within the state of California
SELECT id, name
FROM cities
WHERE state_id = (
    -- Subquery to find the id of the state with the name 'California'
    SELECT id
    FROM states
    WHERE name = 'California'
)
-- Orders the result set by city id in ascending order
ORDER BY cities.id ASC;

