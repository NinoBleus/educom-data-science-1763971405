CREATE VIEW months (id, name) AS 
  SELECT 1,'Januari'
  UNION SELECT 2,'Februari'
  UNION SELECT 3,'Maart'
  UNION SELECT 4,'April'
  UNION SELECT 5,'Mei'
  UNION SELECT 6,'Juni'
  UNION SELECT 7,'Juli'
  UNION SELECT 8,'Augustus'
  UNION SELECT 9,'September'
  UNION SELECT 10, 'Oktober'
  UNION SELECT 11,'November'
  UNION SELECT 12,'December';

SELECT
    year as jaar,
    months.name as maand,
    num_sup as 'aantal leveranciers',
    total_hit as 'totaal aantal hits'
FROM (
    SELECT year, month, COUNT(supplier_ID) as num_sup, SUM(hitcount) AS total_hit 
    FROM mhl_hitcount 
    GROUP BY year, month 
    ORDER BY year, month 
) AS totals
JOIN months ON month=months.id
ORDER BY year DESC, months.name ASC