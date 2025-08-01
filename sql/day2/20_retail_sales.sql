-- Project 20: Retail Sales Tracker
CREATE DATABASE IF NOT EXISTS retail_sales_db;
USE retail_sales_db;

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    quantity INT,
    sale_date DATE
);

INSERT INTO sales (item_name, category, price, quantity, sale_date) VALUES
('iPhone 14 Pro', 'Electronics', 1200.00, 2, '2025-07-25'),
('Samsung TV', 'Electronics', 950.00, 1, '2025-07-22'),
('MacBook Pro', 'Electronics', 1800.00, 3, '2025-07-30'),
('Gaming Chair', 'Furniture', 450.00, 2, '2025-07-20'),
('Leather Wallet', 'Accessories', 300.00, 1, '2025-07-28'),
('Dell Inspiron', 'Electronics', 780.00, 2, '2025-07-27'),
('HP Printer', 'Office', 520.00, NULL, '2025-07-18'),
('Google Pixel Pro', 'Electronics', 999.00, 2, '2025-07-29'),
('Office Desk', 'Furniture', 1300.00, 1, '2025-07-23'),
('Sony Headphones', 'Accessories', 599.00, 2, '2025-07-31');

-- 1. Items with price > 500 and quantity >= 2
SELECT * FROM sales
WHERE price > 500 AND quantity >= 2;

-- 2. LIKE search for items with "Pro"
SELECT * FROM sales
WHERE item_name LIKE '%Pro%';

-- 3. Check for NULL quantity
SELECT * FROM sales
WHERE quantity IS NULL;

-- 4. List all categories
SELECT DISTINCT category FROM sales;

-- 5. Sort by sale_date and price
SELECT * FROM sales
ORDER BY sale_date DESC, price DESC;
