--КОЛИЧЕСТВО ПРОДАНННОГО ТОВАРА В ДАННЫЙ ДЕНЬ И ОБЩАЯ СУММА
SELECT 
        date,
        (SELECT SUM(quantity)) AS total_quantity,  
        (SELECT quantity*(SELECT price FROM product WHERE product.id = product_id) AS price_for_one) AS total_sum
    FROM ordeer WHERE date =:date;