--ОБЩЕЕ КОЛИЧЕСТВО НЕ ДОСТАВЛЕННЫХ ЗАКАЗОВ
SELECT COUNT(DISTINCT(date)) AS quiantity FROM ordeer  WHERE delivered = 0;