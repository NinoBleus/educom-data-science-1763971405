SELECT
    S.name AS leverancier,
    IFNULL(C.name, 'tav de directie') AS aanhef,
    IF (p_address<>'', p_address, CONCAT(straat, ' ', huisnr)) AS adres,
    IF (p_address<>'', p_postcode, postcode) AS postcode,
    IF (p_address<>'', P.name, V.name) AS stad,
    IF (p_address<>'', PP.name, VP.name) AS provincie
FROM mhl_suppliers AS S
LEFT JOIN mhl_contacts AS C ON S.ID=C.supplier_ID AND C.department=3
LEFT JOIN mhl_cities AS P ON P.ID=S.p_city_ID
LEFT JOIN mhl_communes AS PC ON PC.ID=P.commune_ID
LEFT JOIN mhl_districts AS PP ON PP.ID=PC.district_ID
LEFT JOIN mhl_cities AS V ON V.ID=S.city_ID
LEFT JOIN mhl_communes AS VC ON VC.ID=V.commune_ID
LEFT JOIN mhl_districts AS VP ON VP.ID=VC.district_ID
WHERE postcode <> ''
ORDER BY provincie, stad, leverancier