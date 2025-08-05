--  12. Online Shopping Cart System 
-- Requirements: 
--  Tables: users, cart_items, products, orders 
--  Insert products into cart with FOREIGN KEY to product. 
--  Update item quantities and total price. 
--  Delete abandoned carts after 7 days. 
--  Add a CHECK on quantity (1–10). 
--  Drop and re-add constraint on cart uniqueness. 
--  Use transaction to place order, update stock, and clear cart.


-- Create Database
CREATE DATABASE IF NOT EXISTS OnlineShoppingDB;
USE OnlineShoppingDB;

-- Create Tables
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at DATE DEFAULT (CURDATE())
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0)
);

CREATE TABLE cart_items (
    cart_item_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity BETWEEN 1 AND 10),
    added_on DATE DEFAULT (CURDATE()),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    UNIQUE KEY unique_user_product (user_id, product_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    total_price DECIMAL(10,2),
    order_date DATE DEFAULT (CURDATE()),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Sample Inserts
INSERT INTO users (username, email) VALUES
('nisha01', 'nisha@example.com'),
('reetha02', 'reetha@example.com');

INSERT INTO products (name, price, stock) VALUES
('Baby Lotion', 299.99, 100),
('Diapers Pack', 499.00, 50),
('Baby Shampoo', 199.50, 30);

INSERT INTO cart_items (user_id, product_id, quantity) VALUES
(1, 1, 2),
(1, 2, 1);

-- Update quantity example
UPDATE cart_items SET quantity = 3 WHERE cart_item_id = 1;

-- Delete abandoned carts older than 7 days
DELETE FROM cart_items WHERE added_on < (CURRENT_DATE - INTERVAL 7 DAY);

-- Transaction: Place order, update stock, clear cart
START TRANSACTION;

-- Calculate total price for user_id = 1
SELECT SUM(p.price * c.quantity) INTO @total_price
FROM cart_items c JOIN products p ON c.product_id = p.product_id
WHERE c.user_id = 1;

-- Insert order record
INSERT INTO orders (user_id, total_price) VALUES (1, @total_price);

-- Check stock availability before updating
-- This part needs to be done outside SQL or with application logic
-- For demo, update stock only if sufficient stock exists
UPDATE products p
JOIN cart_items c ON p.product_id = c.product_id
SET p.stock = p.stock - c.quantity
WHERE c.user_id = 1 AND p.stock >= c.quantity;

-- Confirm no product went negative
SELECT COUNT(*) INTO @neg_stock FROM products WHERE stock < 0;

-- If any stock negative, rollback (simulate by manual check)
-- Since MySQL SQL scripts cannot do IF/ELSE outside procedures,
-- you must check @neg_stock value and decide rollback or commit manually.

-- For demo, just commit
COMMIT;

-- Clear cart after successful order
DELETE FROM cart_items WHERE user_id = 1;
