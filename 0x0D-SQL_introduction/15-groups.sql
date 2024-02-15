-- list number of records with same score

SELECT score, COUNT(*) FROM second_table GROUP BY score;