SELECT
    ID,
    joindate,
    TO_DAYS(CURDATE())-TO_DAYS(joindate) AS dagen_lid
FROM mhl_suppliers
ORDER BY dagen_lid ASC