
-- 7. Online Gadget Store
-- Requirements:
-- Tables: products, categories, customers, orders.
-- Use DISTINCT to get unique customer locations.
-- Use BETWEEN to filter high-value orders.
-- Subquery in WHERE to find customers who never ordered accessories.
-- Use MAX(), MIN() for order value analytics.
-- Use JOINs for full product category mapping.
-- Sort by most purchased products.
-- CASE to label customers as "VIP" or "Regular".

CREATE DATABASE IF NOT EXISTS GadgetStoreDB;
USE GadgetStoreDB;

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    category_id INT,
    price DECIMAL(10,2),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    city VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert Sample Data

INSERT INTO categories (name) VALUES
('Smartphones'),
('Laptops'),
('Accessories'),
('Tablets');

INSERT INTO products (name, category_id, price) VALUES
('iPhone 14', 1, 80000.00),
('Galaxy S22', 1, 75000.00),
('MacBook Air', 2, 120000.00),
('Dell Inspiron', 2, 70000.00),
('Wireless Mouse', 3, 1500.00),
('Bluetooth Earphones', 3, 2500.00),
('iPad Air', 4, 60000.00);

INSERT INTO customers (name, city, email) VALUES
('Raj Malhotra', 'Delhi', 'raj@example.com'),
('Neha Singh', 'Mumbai', 'neha@example.com'),
('Vikram Rao', 'Chennai', 'vikram@example.com'),
('Pooja Sharma', 'Bangalore', 'pooja@example.com');

INSERT INTO orders (customer_id, product_id, quantity, order_date) VALUES
(1, 1, 1, '2025-07-01'),
(2, 3, 1, '2025-07-02'),
(3, 5, 2, '2025-07-03'),
(1, 6, 1, '2025-07-04'),
(2, 2, 1, '2025-07-05'),
(4, 4, 1, '2025-07-06'),
(3, 1, 1, '2025-07-07'),
(2, 5, 3, '2025-07-08');

-- Queries

-- 1. DISTINCT to get unique customer locations
SELECT DISTINCT city FROM customers;

-- 2. BETWEEN to filter high-value orders (price * quantity > ₹50,000)
SELECT o.order_id, c.name AS customer, p.name AS product,
       o.quantity, (p.price * o.quantity) AS total_value
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE (p.price * o.quantity) BETWEEN 50000 AND 150000;

-- 3. Subquery in WHERE to find customers who never ordered accessories
SELECT name FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT o.customer_id
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    WHERE p.category_id = (
        SELECT category_id FROM categories WHERE name = 'Accessories'
    )
);

-- 4. MAX() and MIN() for order value analytics
SELECT 
    MAX(p.price * o.quantity) AS max_order_value,
    MIN(p.price * o.quantity) AS min_order_value
FROM orders o
JOIN products p ON o.product_id = p.product_id;

-- 5. JOINs for full product category mapping
SELECT p.name AS product_name, c.name AS category, p.price
FROM products p
JOIN categories c ON p.category_id = c.category_id;

-- 6. Sort by most purchased products
SELECT p.name AS product_name, SUM(o.quantity) AS total_sold
FROM products p
JOIN orders o ON p.product_id = o.product_id
GROUP BY p.product_id
ORDER BY total_sold DESC;

-- 7. CASE to label customers as "VIP" or "Regular"
SELECT c.name, COUNT(o.order_id) AS total_orders,
       CASE
           WHEN COUNT(o.order_id) >= 3 THEN 'VIP'
           ELSE 'Regular'
       END AS customer_type
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;
