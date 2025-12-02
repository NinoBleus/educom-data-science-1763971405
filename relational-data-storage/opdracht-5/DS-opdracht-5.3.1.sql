CREATE VIEW DIRECTIE AS
    SELECT
        supplier_ID,
        mhl_contacts.name AS contact,
        contacttype AS functie,
        mhl_departments.name AS department
    FROM mhl_contacts
    LEFT JOIN mhl_departments ON department=mhl_departments.id
    WHERE IF (mhl_departments.name="Directie", TRUE, contacttype LIKE '%directeur%')