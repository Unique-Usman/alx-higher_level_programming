-- list all the record with same in the table
-- order by numbers of record

SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
