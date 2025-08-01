-- Project 22: Online Retail Order Tracking

-- Create and use database
CREATE DATABASE IF NOT EXISTS online_retail_db;
USE online_retail_db;

-- Create tables

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data

INSERT INTO customers (customer_id, name, email) VALUES
(1, 'Alice Johnson', 'alice@example.com'),
(2, 'Bob Smith', 'bob@example.com'),
(3, 'Charlie Lee', 'charlie@example.com'),
(4, 'Diana Prince', 'diana@example.com');

INSERT INTO products (product_id, product_name, price) VALUES
(1, 'Laptop', 70000.00),
(2, 'Smartphone', 30000.00),
(3, 'Headphones', 2000.00),
(4, 'Keyboard', 1500.00),
(5, 'Mouse', 800.00),
(6, 'Monitor', 12000.00);

INSERT INTO orders (order_id, customer_id, order_date) VALUES
(1, 1, '2025-07-01'),
(2, 1, '2025-07-10'),
(3, 2, '2025-07-12'),
(4, 3, '2025-07-15');

INSERT INTO order_items (order_item_id, order_id, product_id, quantity) VALUES
(1, 1, 1, 1),  -- Alice bought 1 Laptop
(2, 1, 3, 2),  -- Alice bought 2 Headphones
(3, 2, 2, 1),  -- Alice bought 1 Smartphone
(4, 3, 4, 3),  -- Bob bought 3 Keyboards
(5, 3, 5, 2),  -- Bob bought 2 Mouse
(6, 4, 3, 1);  -- Charlie bought 1 Headphones

-- Queries

-- 1. Total amount spent per customer (SUM)
SELECT 
    c.name,
    SUM(oi.quantity * p.price) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN order_items oi ON o.order_id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.name;

-- 2. Products sold count and total revenue (COUNT, SUM)
SELECT 
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold,
    SUM(oi.quantity * p.price) AS total_revenue
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name;

-- 3. Group sales by product and filter with HAVING SUM > 10,000
SELECT 
    p.product_name,
    SUM(oi.quantity * p.price) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
HAVING total_revenue > 10000;

-- 4. INNER JOIN orders ↔ order_items, order_items ↔ products
SELECT 
    o.order_id, 
    c.name AS customer_name,
    p.product_name,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_price
FROM orders o
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
INNER JOIN customers c ON o.customer_id = c.customer_id;

-- 5. LEFT JOIN to show customers without orders
SELECT 
    c.name,
    o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- 6. RIGHT JOIN to show products that were never sold
SELECT 
    p.product_name,
    oi.order_item_id
FROM products p
RIGHT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.order_item_id IS NULL;
