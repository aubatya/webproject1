from intit_db import initdb

db = initdb("sqlite:///site.db")

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    surname = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    telephone = db.Column(db.String, nullable = False)
    birth_date = db.Column(db.String, nullable = False)
    start_date = db.Column(db.String, nullable = False)
    password = db.Column(db.Integer, nullable = False)
    
    def __init__(self, name, surname, email, telephone, birh_date, start_date, password) -> None:
        self.name, self.surname, self.email, self.telephone, self.birth_date, self.start_date, self.password = name, surname, email, telephone, birh_date, start_date, hash(password)
    
    def __repr__(self) -> str:
        return f"{self.id}"

class Products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    quantity_in_stock = db.Column(db.Integer, nullable = False)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    image = db.Column(db.String, nullable = False)
    price = db.Column(db.Float, nullable = False)
    date = db.Column(db.String, nullable = False)
    
    def __init__(self, quantity_in_stock, name, description, image, price, date) -> None:
        self.quantity_in_stock, self.name, self.description, self.image, self.price, self.date = quantity_in_stock, name, description, image, price, date

    def __repr__(self) -> str:
        return f"{self.id}"

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.String, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    date = db.Column(db.String, nullable = False)
    delivered = db.Column(db.Integer, nullable = False)
    delivery_date = db.Column(db.String, nullable = False)
    product = db.relationship("Products", backref = db.backref("orders", lazy = False))
    user = db.relationship("Users", backref = db.backref("orders", lazy = False))
    
    def __init__(self, address, quantity, product_id, user_id, date, delivered, delivery_date, product, user) -> None:
        self.address, self.quantity, self.product_id, self.user_id, self.date, self.delivered, self.delivery_date, self.product, self.user = address, quantity, product_id, user_id, date, delivered, delivery_date, product, user

    def __repr__(self) -> str:
        return f"{self.id}"

#db.create_all()

