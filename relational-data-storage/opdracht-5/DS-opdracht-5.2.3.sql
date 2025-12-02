SELECT
    year,
    SUM(IF(month IN ('1', '2', '3'),hitcount,0)) AS 'Q1',
    SUM(IF(month IN ('4', '5', '6'),hitcount,0)) AS 'Q2',
    SUM(IF(month IN ('7', '8', '9'),hitcount,0)) AS 'Q3',
    SUM(IF(month IN ('10', '11', '12'), hitcount, 0)) AS 'Q4',
    SUM(hitcount) AS Totaal
FROM mhl_hitcount
GROUP BY year