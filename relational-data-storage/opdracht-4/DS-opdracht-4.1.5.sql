SELECT s.name, s.straat, s.huisnr, s.postcode, geo.lat, geo.lng
FROM mhl_suppliers as s 
JOIN pc_lat_long as geo on geo.pc6 = s.postcode
ORDER BY geo.lat DESC
LIMIT 5