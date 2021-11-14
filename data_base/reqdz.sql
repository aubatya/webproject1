SELECT MAX(start_date) AS start_date, name FROM user;
SELECT DISTINCT(SUBSTR(birth_date, 1, 4)) AS age FROM user;
SELECT SUM(quantity_in_stock)  AS  total_items FROM product ;
SELECT AVG(CAST(2021 AS INTEGER)-CAST(SUBSTR(birth_date, 1, 4) AS INTEGER)) AS AGE FROM user WHERE JULIANDAY('now')-JULIANDAY(start_date)<=JULIANDAY('now')-JULIANDAY(DATE('now', '-2 months'));
SELECT AVG(CAST(2021 AS INTEGER)-CAST(SUBSTR(birth_date, 1, 4) AS INTEGER)) AS AGE FROM user WHERE JULIANDAY('now')-JULIANDAY(start_date)<=JULIANDAY('now')-JULIANDAY(DATE('now', '-1 years'));