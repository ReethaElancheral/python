--  9. Restaurant Order and Billing 
-- Requirements: 
--  Tables: customers, orders, menu_items, bills 
--  Insert orders with FOREIGN KEY to customer and item. 
--  Update item availability after order. 
--  Delete unpaid orders after timeout. 
--  Enforce CHECK for order quantity ≤ 10. 
--  Drop and reapply NOT NULL constraint on table number. 
--  Use a transaction to create order and bill together.

-- Create Database
CREATE DATABASE IF NOT EXISTS RestaurantDB;
USE RestaurantDB;

-- Create Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE
);

-- Create Menu Items Table
CREATE TABLE menu_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

-- Create Orders Table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    item_id INT,
    quantity INT CHECK (quantity <= 10),
    table_number INT,
    order_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
);

-- Create Bills Table
CREATE TABLE bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    total_amount DECIMAL(10,2),
    paid BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Insert Sample Customers
INSERT INTO customers (name, phone) VALUES
('Aanya Sharma', '9876543210'),
('Kabir Verma', '9123456789');

-- Insert Sample Menu Items
INSERT INTO menu_items (item_name, price, available) VALUES
('Pasta', 250.00, TRUE),
('Pizza', 400.00, TRUE),
('Mojito', 120.00, TRUE);

-- Insert Orders (with valid quantity <= 10)
INSERT INTO orders (customer_id, item_id, quantity, table_number)
VALUES (1, 1, 2, 5), (2, 2, 1, 7);

-- Update availability after order (example: Pizza is no longer available)
UPDATE menu_items SET available = FALSE WHERE item_id = 2;

-- DELETE unpaid orders after timeout (simulate timeout logic manually)
DELETE FROM orders WHERE order_id NOT IN (SELECT order_id FROM bills WHERE paid = TRUE);

-- Drop and Reapply NOT NULL constraint on table_number
-- Step 1: Drop constraint by allowing NULL
ALTER TABLE orders MODIFY COLUMN table_number INT NULL;

-- Step 2: Reapply NOT NULL
ALTER TABLE orders MODIFY COLUMN table_number INT NOT NULL;

-- Transaction: Create new order and bill together
START TRANSACTION;

-- Insert new order
INSERT INTO orders (customer_id, item_id, quantity, table_number)
VALUES (1, 3, 2, 6);

-- Get last inserted order ID
SET @last_order_id = LAST_INSERT_ID();

-- Insert corresponding bill
INSERT INTO bills (order_id, total_amount, paid)
VALUES (@last_order_id, (SELECT price FROM menu_items WHERE item_id = 3) * 2, FALSE);

-- If all good
COMMIT;

-- If something goes wrong
-- ROLLBACK;

-- View current bills and orders
SELECT * FROM bills;
SELECT * FROM orders;
