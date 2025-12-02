SELECT
    mhl_cities.name AS Stad,
    COUNT(IF(mhl_membertypes.name = 'Gold', 1, NULL)) 'Gold',
    COUNT(IF(mhl_membertypes.name = 'Silver', 1, NULL)) 'Silver',
    COUNT(IF(mhl_membertypes.name = 'Bronze', 1, NULL)) 'Bronze',
    COUNT(IF (mhl_membertypes.name NOT IN ('Gold','Silver','Bronze'), 1, NULL)) 'Other'
FROM mhl_suppliers
JOIN mhl_membertypes ON mhl_suppliers.membertype=mhl_membertypes.id
JOIN mhl_cities ON city_ID = mhl_cities.ID
GROUP BY city_id
ORDER BY Gold DESC, Silver DESC, Bronze DESC, Other DESC