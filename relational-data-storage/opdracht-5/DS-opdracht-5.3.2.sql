CREATE VIEW POSTADRES AS
    SELECT
        mhl_suppliers.ID,
        IF (p_address<>'', p_address, CONCAT(straat, ' ', huisnr)) AS adres,
        IF (p_address<>'',  p_postcode, postcode) AS postcode,
        IF (p_address<>'', p_city.name, city.name) AS stad
     FROM mhl_suppliers
     LEFT JOIN mhl_cities AS p_city ON p_city.ID=mhl_suppliers.p_city_ID
     LEFT JOIN mhl_cities AS city ON city.ID=mhl_suppliers.city_ID