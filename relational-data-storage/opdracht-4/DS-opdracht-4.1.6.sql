SELECT 	h.hitcount as hitcount,
		s.name as leverancier, 
        c.name as stad, 
        co.name as gemeente,
        d.name as provincie,
        cou.name as land,
        h.year as year,
        h.month as month
FROM mhl_hitcount as h
INNER JOIN mhl_suppliers as s ON h.supplier_ID = s.id
INNER JOIN mhl_cities as c on s.city_ID = c.id
INNER JOIN mhl_communes as co on c.commune_ID = co.id
INNER JOIN mhl_districts as d on co.district_ID = d.id
INNER JOIN mhl_countries as cou on cou.id = d.country_ID
WHERE h.year=2014 and h.month=1 and d.name IN ("limburg", "noord-brabant", "zeeland") 