UPDATE user SET start_date = SUBSTR(start_date, 7, 4) || '-' || SUBSTR(start_date, 4, 2) || '-' ||SUBSTR(start_date, 1, 2);
UPDATE user SET birth_date = SUBSTR(birth_date, 7, 4) || '-' || SUBSTR(birth_date, 4, 2) || '-' ||SUBSTR(birth_date, 1, 2);
UPDATE ordeer SET date = SUBSTR(date, 7, 4) || '-' || SUBSTR(date, 4, 2) || '-' ||SUBSTR(date, 1, 2);
UPDATE product SET date = SUBSTR(date, 7, 4) || '-' || SUBSTR(date, 4, 2) || '-' ||SUBSTR(date, 1, 2);
UPDATE ordeer SET delivery_date = SUBSTR(delivery_date, 7, 4) || '-' || SUBSTR(delivery_date, 4, 2) || '-' ||SUBSTR(delivery_date, 1, 2);