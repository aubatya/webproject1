--ИНФОРМАЦИ О ДОСТАВКЕ ДАННОГО ПОЛЬЗОВАТЕЛЯ
SELECT
	(SELECT name FROM user WHERE user.id=user_id) AS user_name,
	(SELECT surname FROM user WHERE user.id=user_id) AS user_surname,
	(SELECT name FROM product WHERE product.id=product_id) AS product_name,
	address,
	(SELECT telephone FROM user WHERE user.id=user_id) AS user_tel,
	quantity,
	(SELECT price FROM product WHERE product.id=product_id )AS price_for_one
FROM ordeer WHERE user_id=10 AND delivered = 0;
	