from datetime import datetime
import sqlite3
import create_ex

def base_init(path: str) -> sqlite3.Connection:
    return sqlite3.connect(path)

def data_del(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.executescript("""
    DELETE FROM ordeer;
    DELETE FROM product;
    DELETE FROM user;
    UPDATE sqlite_sequence SET seq = 0;
    """)
    conn.commit()
    cursor.close()

def update_date(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.executescript("""
    UPDATE user SET start_date = SUBSTR(start_date, 7, 4) || '-' || SUBSTR(start_date, 4, 2) || '-' ||SUBSTR(start_date, 1, 2);
    UPDATE user SET birth_date = SUBSTR(birth_date, 7, 4) || '-' || SUBSTR(birth_date, 4, 2) || '-' ||SUBSTR(birth_date, 1, 2);
    UPDATE ordeer SET date = SUBSTR(date, 7, 4) || '-' || SUBSTR(date, 4, 2) || '-' ||SUBSTR(date, 1, 2);
    UPDATE product SET date = SUBSTR(date, 7, 4) || '-' || SUBSTR(date, 4, 2) || '-' ||SUBSTR(date, 1, 2);
    UPDATE ordeer SET delivery_date = SUBSTR(delivery_date, 7, 4) || '-' || SUBSTR(delivery_date, 4, 2) || '-' ||SUBSTR(delivery_date, 1, 2);
    """)
    conn.commit()
    cursor.close()

def random_data(conn: sqlite3.Connection, quantity_object : int) -> None:
    lproduct, luser, lorder = create_ex.randomdb(quantity_object)
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", lproduct)
    cursor.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", luser)
    cursor.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", lorder)
    update_date(conn)
    conn.commit()
    cursor.close()

#ОБЩЕЕ КОЛИЧЕСТВО НЕ ДОСТАВЛЕННЫХ ЗАКАЗОВ
def total_order(conn: sqlite3.Connection) -> int:
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT(date)) AS quiantity FROM ordeer WHERE delivered = 0;")
    req_res = int(cursor.fetchall()[0][0])
    cursor.close()
    return req_res

#ОБЩАЯ СУММА И КОЛИЧЕСТВО ТОВАРОВ НА СКЛАДЕ
def total_sum_quan(conn: sqlite3.Connection) -> list:
    cursor = conn.cursor()
    cursor.execute("SELECT SUM((quantity_in_stock*price)) AS TOTAL_SUM, SUM(quantity_in_stock) AS TOTAL_QUANTITY FROM product;")
    req_res = list(cursor.fetchall()[0])
    for i in range(2):
        if req_res[i]==None:
            req_res[i] = 0
    cursor.close()
    return req_res

#КОЛИЧЕСТВО ПРОДАНННОГО ТОВАРА В ДАННЫЙ ДЕНЬ И ОБЩАЯ СУММА
def or_sum(conn: sqlite3.Connection, date: str) -> list: #date YYYY-MM-DD
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except Exception as e:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    cursor = conn.cursor()
    cursor.execute("""SELECT 
        (SELECT SUM(quantity)) AS total_quantity,  
        (SELECT quantity*(SELECT price FROM product WHERE product.id = product_id) AS price_for_one) AS total_sum
    FROM ordeer WHERE delivered = 1 AND date = :date;""", {"date": date})
    req_res = list(cursor.fetchall())
    for i in range(len(req_res)):
        if req_res[i][0]==None:
            req_res[i] = (0, req_res[i][1])
        if req_res[i][1]==None:
            req_res[i] = (req_res[i][0], 0)
    cursor.close()
    return req_res

#ДНИ В КОТОРЫЕ БЫЛИ ПРОДАНЫ ТОВАРЫ
def date_sel(conn: sqlite3.Connection) -> list:
    cursor = conn.cursor()
    cursor.execute("""SELECT date FROM ordeer WHERE delivered = 1;""")
    req_res1 = list(cursor.fetchall())
    req_res = []
    for i in req_res1:
        req_res.append(i[0])
    cursor.close()
    return req_res

#СТАТИСТИКА ПРОДАЖ
def statis(conn: sqlite3.Connection) -> list: #[[(date, qunatity, sum)], ]
    stat = []
    for i in date_sel(conn):
        stat.append((i[0], or_sum(conn, i[0])))
    return stat

#КОЛИЧЕСТВО ОСТАВШЕГОСЯ ДАННОГО ТОВАРА
def ost(conn: sqlite3.Connection, id: int) -> int:
    cursor = conn.cursor()
    cursor.execute("SELECT quantity_in_stock FROM product WHERE id = :id", {"id": id})
    req_res = cursor.fetchall()
    if req_res:
        req_res = int(req_res[0][0])
    else:
        req_res = 0
    cursor.close()
    return req_res

#id ПОЛЬЗОВАТЕЛЕЙ У КОТОРЫХ ДОСТАВКА НАЗНАЧЕНА НА ДАННУЮ ДАТУ ИЛИ БЫЛА НАЗНАЧЕНА
def user_id(conn: sqlite3.Connection, date = 'now') -> list: #date YYYY-MM-DD
    try:
        if date!='now':
            datetime.strptime(date, "%Y-%m-%d")
    except Exception as e:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(id) FROM ordeer WHERE delivery_date = :date;", {"date": date})
    req_res1 = list(cursor.fetchall())
    req_res = [] 
    for i in req_res1:
        req_res.append(i[0])
    cursor.close()
    return req_res

#ИНФОРМАЦИ О ДОСТАВКЕ ДАННОГО ПОЛЬЗОВАТЕЛЯ
def inf_user(conn: sqlite3.Connection, id: int) ->list:#[(user_name, user_surname, product_name, address, user_tel, quantity, price_for_one), ]
    cursor = conn.cursor()
    cursor.execute("""SELECT
        (SELECT name FROM user WHERE user.id=user_id) AS user_name,
        (SELECT surname FROM user WHERE user.id=user_id) AS user_surname,
        (SELECT name FROM product WHERE product.id=product_id) AS product_name,
        address,
        (SELECT telephone FROM user WHERE user.id=user_id) AS user_tel,
        quantity,
        (SELECT price FROM product WHERE product.id=product_id ) AS price_for_one
    FROM ordeer WHERE user_id = :id AND delivered = 0;""", {"id": id})
    #req_res = [("user_name", "user_surname", "product_name", "address", "user_tel", "quantity", "price_for_one")]
    req_res = []
    req_res.extend(list(cursor.fetchall()))
    cursor.close()
    return req_res

conn = base_init("site.db")
conn.close()