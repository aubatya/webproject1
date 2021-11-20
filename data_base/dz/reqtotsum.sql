--КОЛИЧЕСТВО ПРОДАНННОГО ТОВАРА В ДАННЫЙ И СУММА
SELECT 
	date,
	(SELECT SUM(quantity) where date = '2021-05-02') AS total_quantity,  
	(SELECT quantity*(SELECT price FROM product WHERE product.id = product_id) AS price_for_one) AS total_sum
FROM ordeer WHERE delivered = 1;
	