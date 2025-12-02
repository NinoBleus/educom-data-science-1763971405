SELECT
    sup.name,
    sup.straat,
    sup.huisnr,
    sup.postcode,
    rub.name,
    city.name 
FROM mhl_suppliers_mhl_rubriek_view as suprub 
JOIN mhl_rubrieken as rub on rub.id = suprub.mhl_rubriek_view_ID
LEFT JOIN mhl_rubrieken as parrub on rub.parent = parrub.id
JOIN mhl_suppliers as sup on sup.id = suprub.mhl_suppliers_ID
JOIN mhl_cities as city on city.id = sup.city_ID
WHERE city.name = 'amsterdam' and (rub.name like 'drank' or parrub.name like 'drank')
ORDER BY rub.name, sup.name 