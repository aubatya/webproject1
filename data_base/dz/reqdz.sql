SELECT MAX(start_date) AS start_date, name FROM users;
SELECT DISTINCT(SUBSTR(birth_date, 1, 4)) AS age FROM users;
SELECT SUM(quantity_in_stock)  AS  total_items FROM products ;
SELECT AVG(CAST(2021 AS INTEGER)-CAST(SUBSTR(birth_date, 1, 4) AS INTEGER)) AS AGE FROM users WHERE JULIANDAY('now')-JULIANDAY(start_date)<=JULIANDAY('now')-JULIANDAY(DATE('now', '-2 months'));