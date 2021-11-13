CREATE TABLE "user" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	"surname"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"telephone"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "product" (
	"id"	INTEGER,
	"quantity_in_stock"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	"image"	BLOB NOT NULL,
	"price"	REAL NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE "ordeer" (
	"id"	INTEGER,
	"address"	TEXT NOT NULL,
	"quantity"	INTEGER NOT NULL,
	"product_id"	INTEGER NOT NULL,
	"user_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("product_id") REFERENCES "product"("id"),
	FOREIGN KEY("user_id") REFERENCES "user"("id")
);
