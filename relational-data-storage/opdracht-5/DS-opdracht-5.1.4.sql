SELECT 	s.name AS supplier, 
		SUM(hitcount.hitcount) AS SumHit, 
        COUNT(hitcount.month) AS CountMonth, 
        ROUND(AVG(hitcount.hitcount), 0) AS MonthAverage
FROM mhl_hitcount AS hitcount
JOIN mhl_suppliers AS s ON hitcount.supplier_ID = s.id
GROUP BY s.name
HAVING SumHit > 100
ORDER BY MonthAverage DESC