SELECT
    EXTRACT(YEAR FROM joindate) AS jaar,
    MONTHNAME(joindate) AS maand,
    COUNT(ID) AS aantal
FROM `mhl_suppliers`
GROUP BY jaar, MONTHNAME(joindate), MONTH(joindate)
ORDER BY jaar, MONTH(joindate)