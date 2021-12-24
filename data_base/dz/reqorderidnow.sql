--id ПОЛЬЗОВАТЕЛЕЙ У КОТОРЫХ ДОСТАВКА НАЗНАЧЕНА НА СЕГОДНЯ
SELECT DISTINCT(id) FROM orders WHERE date = DATE('now');