SELECT 
    s.name,
    p.name,
    IFNULL(yn.content, 'NOT SET') AS value
FROM mhl_suppliers AS s
CROSS JOIN mhl_propertytypes AS p
LEFT JOIN mhl_yn_properties AS yn
    ON yn.supplier_ID = s.id
   AND yn.propertytype_ID = p.id
INNER JOIN mhl_cities AS c
    ON s.city_ID = c.id
WHERE c.name = 'amsterdam'
  AND p.proptype = 'A';
