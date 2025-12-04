SELECT
    DATE_FORMAT(joindate, GET_FORMAT(DATE,'EUR')) AS joindate,
    ID
FROM mhl_suppliers
WHERE DAYOFMONTH(LAST_DAY(joindate))-DAYOFMONTH(joindate) <= 7