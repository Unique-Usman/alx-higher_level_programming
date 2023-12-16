-- list all records of the second_table
-- with name value order by score

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
