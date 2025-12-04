SELECT
    DAYNAME(joindate) AS 'Dag van de week',
    COUNT(ID) AS 'Aantal aanmeldingen'
FROM mhl_suppliers
GROUP BY DAYNAME(joindate), DAYOFWEEK(joindate)
ORDER BY DAYOFWEEK(joindate)