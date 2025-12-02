SELECT
    ms.name AS name,
    SUM(mh.hitcount) AS numhits,
    COUNT(mh.month) AS nummonths,
    ROUND(AVG(mh.hitcount),0) AS avgpermonth
FROM mhl_hitcount mh
JOIN mhl_suppliers ms ON ms.id=mh.supplier_ID
GROUP BY name
HAVING numhits > 100
ORDER BY avgpermonth DESC