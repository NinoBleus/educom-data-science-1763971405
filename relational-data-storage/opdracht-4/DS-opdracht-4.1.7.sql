SELECT c1.name, c2.name, c1.id, c2.id, c1.commune_ID, c2.commune_ID
FROM mhl_cities as c1
JOIN mhl_cities as c2 on c1.name = c2.name
WHERE c1.id < c2.id
ORDER BY c1.name