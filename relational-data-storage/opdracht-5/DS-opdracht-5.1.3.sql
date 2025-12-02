SELECT COUNT(hitcount), AVG(hitcount), MIN(hitcount), MAX(hitcount), SUM(hitcount)
FROM mhl_hitcount as hitcount
JOIN mhl_suppliers as s on hitcount.supplier_ID
GROUP BY hitcount.year, hitcount.month
ORDER BY hitcount.year