
import unittest
from pydb import *

class TestDb(unittest.TestCase):
    cur = None
    conn = base_init("site.db")

    def setUp(self) -> None:
        data_del(self.conn)
        self.cur = self.conn.cursor()
        return super().setUp() 

    def tearDown(self) -> None:
        data_del(self.conn)
        self.cur.close()
        return super().setUp()

    def test_total_order(self) -> None:
        self.assertEqual(total_order(self.conn), 0)
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 1, "2021-04-04")])
        self.assertEqual(total_order(self.conn), 0)
        data_del(self.conn)
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 0, "2021-04-04")])
        self.assertEqual(total_order(self.conn), 1)

    def test_total_sum_quan(self) -> None:
        self.assertEqual(total_sum_quan(self.conn), [0, 0])
        l = [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01")]
        l.append((3, "i3", "asfas", bin(3), 321, "2021-02-02"))
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", l)
        self.assertEqual(total_sum_quan(self.conn), [5*123+3*321, 5+3])

    def test_or_sum(self) -> None:
        self.assertEqual(or_sum(self.conn, "2021-12-03"), [(0, 0)])
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 1, "2021-04-04")])
        self.assertEqual(or_sum(self.conn, "2021-03-03"), [(3, 3*123)])

    def test_date_sel(self) -> None:
        self.assertEqual(date_sel(self.conn), [])
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 1, "2021-04-04")])
        self.assertEqual(date_sel(self.conn), ["2021-03-03"])

    def test_statis(self) -> None:
        self.assertEqual(statis(self.conn), [])
    
    def test_ost(self) -> None:
        self.assertEqual(ost(self.conn, 123), 0)
        l = [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01")]
        l.append((3, "i3", "asfas", bin(3), 321, "2021-02-02"))
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", l)
        self.assertEqual(ost(self.conn, 1), 5)

    def test_user_id(self) -> None:
        self.assertEqual(user_id(self.conn), [])
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 1, "2021-04-04")])
        self.assertEqual(user_id(self.conn, "2021-04-04"), [1])

    def test_inf_user(self) -> None:
        self.assertEqual(inf_user(self.conn, 135125), [])
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01"), (3, "i3", "asfas", bin(3), 321, "2021-02-02")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 1, "2021-04-04"), ("asqrwraf", 1, 2, 1, "2021-03-03", 1, "2021-04-04")])
        self.assertEqual(inf_user(self.conn, 1), [])
        data_del(self.conn)
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01"), (3, "i3", "asfas", bin(3), 321, "2021-02-02")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 0, "2021-04-04"), ("asqrwraf", 1, 2, 1, "2021-03-03", 0, "2021-04-04")])
        self.assertEqual(inf_user(self.conn, 1), [("Aub", "Abdullaev", "i9", "asqrwraf", "+79031145402", 3, 123), ("Aub", "Abdullaev", "i3", "asqrwraf", "+79031145402", 1, 321)])
        data_del(self.conn)
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01"), (3, "i3", "asfas", bin(3), 321, "2021-02-02")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 0, "2021-04-04"), ("asqrwraf", 1, 2, 1, "2021-03-03", 1, "2021-04-04")])
        self.assertEqual(inf_user(self.conn, 1), [("Aub", "Abdullaev", "i9", "asqrwraf", "+79031145402", 3, 123)])
        data_del(self.conn)
        self.cur.executemany("INSERT INTO product (quantity_in_stock, name, description, image, price, date) VALUES (?, ?, ?, ?, ?, ?)", [(5, "i9", "asfasfasg", bin(2), 123, "2021-01-01"), (3, "i3", "asfas", bin(3), 321, "2021-02-02")])
        self.cur.executemany("INSERT INTO user (name, surname, email, telephone, birth_date, start_date, password) VALUES (?, ?, ?, ?, ?, ?, ?)", [("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "2004-01-14", "2021-02-02", hash("1q24124"))])
        self.cur.executemany("INSERT INTO ordeer (address, quantity, product_id, user_id, date, delivered, delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?)", [("asqrwraf", 3, 1, 1, "2021-03-03", 1, "2021-04-04"), ("asqrwraf", 1, 2, 1, "2021-03-03", 0, "2021-04-04")])
        self.assertEqual(inf_user(self.conn, 1), [("Aub", "Abdullaev", "i3", "asqrwraf", "+79031145402", 1, 321)])
        
if __name__=='__main__':
    unittest.main()