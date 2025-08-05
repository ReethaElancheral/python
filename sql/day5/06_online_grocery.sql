--  6. Online Grocery Inventory Management 
-- Requirements: 
--  Tables: products, categories, suppliers, stock_logs 
--  Insert product with FOREIGN KEY to category and supplier. 
--  Update price and quantity with validation. 
--  Delete expired products. 
--  CHECK (quantity >= 0), NOT NULL on product name. 
--  Drop and recreate the UNIQUE constraint on product code. 
--  Use SAVEPOINT while updating prices in bulk; rollback if any failure. 
--  Ensure atomicity when updating inventory and stock logs.


CREATE DATABASE IF NOT EXISTS GroceryInventoryDB;
USE GroceryInventoryDB;

-- Create Categories Table
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL
);

-- Create Suppliers Table
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    supplier_name VARCHAR(100) NOT NULL,
    contact VARCHAR(50)
);

-- Create Products Table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_code VARCHAR(50) UNIQUE,
    product_name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    supplier_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    price DECIMAL(10,2) NOT NULL,
    expiry_date DATE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Create Stock Logs Table
CREATE TABLE stock_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    change_type ENUM('IN', 'OUT') NOT NULL,
    quantity_changed INT NOT NULL,
    change_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample categories
INSERT INTO categories (category_name) VALUES
('Fruits'), ('Vegetables'), ('Dairy');

-- Insert sample suppliers
INSERT INTO suppliers (supplier_name, contact) VALUES
('Fresh Farm', '1234567890'),
('Organic Ltd.', '9876543210');

-- Insert products with category and supplier foreign keys
INSERT INTO products (product_code, product_name, category_id, supplier_id, quantity, price, expiry_date) VALUES
('P001', 'Apple', 1, 1, 100, 2.50, '2025-09-15'),
('P002', 'Milk', 3, 2, 50, 1.75, '2025-08-10'),
('P003', 'Tomato', 2, 1, 80, 1.20, '2025-08-25');

-- Update product price and quantity manually (with validation in your application logic)
UPDATE products
SET price = 2.70, quantity = 120
WHERE product_id = 1;

-- Delete expired products
DELETE FROM products
WHERE expiry_date < CURDATE();

-- Drop and recreate UNIQUE constraint on product_code
ALTER TABLE products DROP INDEX product_code;
-- You may reinsert products or update here...
ALTER TABLE products ADD UNIQUE (product_code);

-- Use SAVEPOINT while updating prices in bulk; rollback if any failure
START TRANSACTION;

SAVEPOINT before_price_update;

-- Bulk price updates
UPDATE products SET price = price * 1.10 WHERE category_id = 1;
UPDATE products SET price = price * 1.05 WHERE category_id = 2;

-- Uncomment to simulate failure
-- UPDATE products SET price = -50 WHERE product_id = 1;

-- If no error
COMMIT;

-- If failure encountered
-- ROLLBACK TO SAVEPOINT before_price_update;

-- Ensure atomicity: updating inventory and logging stock movement
START TRANSACTION;

-- Example: Sell 10 Apples (OUT)
UPDATE products
SET quantity = quantity - 10
WHERE product_id = 1 AND quantity >= 10;

-- Log the stock change
INSERT INTO stock_logs (product_id, change_type, quantity_changed)
VALUES (1, 'OUT', 10);

-- If both succeed
COMMIT;

-- If any fails
-- ROLLBACK;
