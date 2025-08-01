
-- 2. Product Inventory Dashboard

-- Create table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT,
    supplier VARCHAR(100),
    description TEXT
);

INSERT INTO products (product_id, name, category, price, stock, supplier, description) VALUES
(1, 'iPhone 14', 'Electronics', 999.99, 10, 'Apple Inc.', 'Latest model with A15 chip'),
(2, 'Samsung Galaxy S22', 'Electronics', 850.50, 15, 'Samsung', 'Flagship Android phone'),
(3, 'Google Pixel 7', 'Electronics', 799.99, 8, 'Google', NULL),
(4, 'Dell XPS 13', 'Computers', 1200.00, 5, 'Dell', 'Ultrabook laptop'),
(5, 'HP Spectre x360', 'Computers', 1150.75, 7, 'HP', 'Convertible laptop'),
(6, 'Logitech Mouse', 'Accessories', 45.99, 50, 'Logitech', 'Wireless mouse'),
(7, 'Sony WH-1000XM4', 'Accessories', 350.00, 20, 'Sony', NULL),
(8, 'Samsung QLED TV', 'Electronics', 1400.00, 3, 'Samsung', '65 inch QLED TV'),
(9, 'Apple Watch Series 7', 'Accessories', 399.00, 12, 'Apple Inc.', 'Smartwatch with fitness tracking'),
(10, 'Asus ROG Strix', 'Computers', 1500.00, 4, 'Asus', 'Gaming laptop');

-- List products with price between 100 and 1000
SELECT name, category, price FROM products
WHERE price BETWEEN 100 AND 1000;

-- Find products with "phone" in the name
SELECT * FROM products
WHERE name LIKE '%phone%';

-- Retrieve items with NULL description
SELECT * FROM products
WHERE description IS NULL;

-- List all distinct suppliers
SELECT DISTINCT supplier FROM products;

-- Filter products where stock is 0 OR price > 5000
SELECT * FROM products
WHERE stock = 0 OR price > 5000;

-- Sort by category ASC, price DESC
SELECT * FROM products
ORDER BY category ASC, price DESC;
