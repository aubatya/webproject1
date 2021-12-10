--ОБЩАЯ СУММА И КОЛИЧЕСТВО ТОВАРОВ НА СКЛАДЕ
SELECT SUM((quantity_in_stock*price)) AS TOTAL_SUM, SUM(quantity_in_stock) AS TOTAL_QUANTITY FROM products;