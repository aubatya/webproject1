--id ПОЛЬЗОВАТЕЛЕЙ У КОТОРЫХ ДОСТАВКА НАЗНАЧЕНА НА СЕГОДНЯ
SELECT DISTINCT(id) FROM ordeer WHERE date = DATE('now');