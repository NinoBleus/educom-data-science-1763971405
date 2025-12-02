SELECT s.name, s.straat, s.huisnr, s.postcode
FROM mhl_yn_properties as p
JOIN mhl_suppliers as s on p.supplier_ID = s.id
JOIN mhl_propertytypes as pt on p.propertytype_ID = pt.id
WHERE pt.name = 'specialistische leverancier' or pt.name = 'ook voor particulieren' 