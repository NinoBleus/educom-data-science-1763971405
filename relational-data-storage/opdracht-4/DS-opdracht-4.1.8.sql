SELECT c1.name, c2.name, c1.id, c2.id, c1.commune_ID, c2.commune_ID, co1.name, co2.name
FROM mhl_cities as c1
JOIN mhl_cities as c2 on c1.name = c2.name
JOIN mhl_communes as co1 on c1.commune_ID = co1.id
JOIN mhl_communes as co2 on c2.commune_ID = co2.id
WHERE c1.id < c2.id
ORDER BY c1.name