import unittest
from models import *

class Test(unittest.TestCase):
    def setUp(self) -> None:
        db.create_all()

    def tearDown(self) -> None:
        db.session.close()
    
    def testQuery(self) -> None:
        us = Users("Aub", "Abdullaev", "aubhon.a@gmail.com", "+79031145402", "14.01.2004", "01.09.2021", "qwerty")
        pr = Products(10, "i9", "qwertyuiop[asdfghjklzxcvbnm,.", bin(124124), 123, "01.01.2001")
        ore = Orders("Балаклавский проспект 6А", 3, 1, 1, "12.12.2021", 1, "31.12.2021", pr, us)
        db.session.add(ore)
        self.assertEqual(Orders.query.one().quantity, 3)
        self.assertEqual(Users.query.one().surname, "Abdullaev")
        self.assertEqual(Products.query.one().quantity_in_stock, 10)
        self.assertEqual(Orders.query.one().product.price, 123)
        self.assertEqual(Orders.query.one().user.telephone, "+79031145402")

if __name__=='__main__':
    unittest.main()