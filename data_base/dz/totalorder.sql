--ОБЩЕЕ КОЛИЧЕСТВО НЕ ДОСТАВЛЕННЫХ ЗАКАЗОВ
SELECT COUNT(DISTINCT(date)) AS quiantity FROM orders  WHERE delivered = 0;