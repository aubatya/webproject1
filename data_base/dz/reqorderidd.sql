--id ПОЛЬЗОВАТЕЛЕЙ У КОТОРЫХ ДОСТАВКА НАЗНАЧЕНА НА ДАННУЮ ДАТУ ИЛИ БЫЛА НАЗНАЧЕНА
SELECT DISTINCT(id) FROM orders WHERE delivery_date = '2021-05-04' ;