DELETE FROM orders;
DELETE FROM products;
DELETE FROM users;
UPDATE sqlite_sequence SET seq = 0;