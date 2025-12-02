SELECT COUNT(hitcount), AVG(hitcount), MIN(hitcount), MAX(hitcount), SUM(hitcount)
FROM mhl_hitcount as hitcount
GROUP BY hitcount.year