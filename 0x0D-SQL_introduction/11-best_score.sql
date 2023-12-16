-- list all records with a score >= 10

SELECT score, name FROM SECOND_TABLE
WHERE score >= 10
ORDER BY score DESC
