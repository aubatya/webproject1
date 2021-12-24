CREATE TABLE "users" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"telephone"	TEXT NOT NULL,
	"birth_date"	TEXT NOT NULL,
	"start_date"	TEXT NOT NULL,
	"password"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "products" (
	"id"	INTEGER,
	"quantity_in_stock"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"image"	BLOB NOT NULL,
	"price"	REAL NOT NULL,
	"date"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "orders" (
	"id"	INTEGER,
	"address"	TEXT NOT NULL,
	"quantity"	INTEGER NOT NULL,
	"product_id"	INTEGER NOT NULL,
	"user_id"	INTEGER NOT NULL,
	"date"	TEXT,
	"delivered"	INTEGER,
	"delivery_date"	TEXT NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "users"("id"),
	FOREIGN KEY("product_id") REFERENCES "products"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);