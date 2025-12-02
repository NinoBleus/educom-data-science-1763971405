SELECT c.name, ifnull(co.name, "INVALID")
FROM mhl_cities as c
LEFT JOIN mhl_communes as co on c.commune_ID = co.id
WHERE isnull(co.name)