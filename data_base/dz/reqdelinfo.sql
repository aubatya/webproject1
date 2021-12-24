--ИНФОРМАЦИ О ДОСТАВКЕ ДАННОГО ПОЛЬЗОВАТЕЛЯ
SELECT
	(SELECT name FROM users WHERE users.id=user_id) AS user_name,
	(SELECT surname FROM users WHERE users.id=user_id) AS user_surname,
	(SELECT name FROM products WHERE products.id=product_id) AS product_name,
	address,
	(SELECT telephone FROM users WHERE users.id=user_id) AS user_tel,
	quantity,
	(SELECT price FROM products WHERE products.id=product_id )AS price_for_one
FROM orders WHERE user_id=10 AND delivered = 0;
	