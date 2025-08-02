-- Project 1: Customer Spending Dashboard for an E-commerce Platform

CREATE DATABASE IF NOT EXISTS ecommerce_dashboard;
USE ecommerce_dashboard;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  item_id INT PRIMARY KEY,
  order_id INT,
  product_id INT,
  quantity INT,
  price DECIMAL(10,2),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  name VARCHAR(100),
  category VARCHAR(100)
);

INSERT INTO customers VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

INSERT INTO orders VALUES
(101, 1, '2025-01-15'),
(102, 1, '2025-05-10'),
(103, 2, '2025-03-25');

INSERT INTO products VALUES
(201, 'Laptop', 'Electronics'),
(202, 'Shoes', 'Apparel');

INSERT INTO order_items VALUES
(301, 101, 201, 1, 60000.00),
(302, 102, 202, 2, 2500.00),
(303, 103, 201, 1, 60000.00);

-- Subquery: Average Order Value per Customer
SELECT c.customer_id, c.name,
  (SELECT AVG(total)
   FROM (
     SELECT o.order_id, SUM(oi.quantity * oi.price) AS total
     FROM orders o
     JOIN order_items oi ON o.order_id = oi.order_id
     WHERE o.customer_id = c.customer_id
     GROUP BY o.order_id
   ) AS customer_totals) AS avg_order_value
FROM customers c;

-- Subquery in FROM: Total revenue per product
SELECT p.product_id, p.name, revenue.total_revenue
FROM products p
JOIN (
  SELECT product_id, SUM(quantity * price) AS total_revenue
  FROM order_items
  GROUP BY product_id
) AS revenue ON p.product_id = revenue.product_id;

-- Correlated subquery: Customers whose orders are above their own average
SELECT o.customer_id, o.order_id
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id
HAVING SUM(oi.quantity * oi.price) > (
  SELECT AVG(total)
  FROM (
    SELECT o2.order_id, SUM(oi2.quantity * oi2.price) AS total
    FROM orders o2
    JOIN order_items oi2 ON o2.order_id = oi2.order_id
    WHERE o2.customer_id = o.customer_id
    GROUP BY o2.order_id
  ) AS customer_avg
);

-- UNION: Old and new customers
SELECT customer_id FROM orders WHERE order_date < '2025-01-01'
UNION
SELECT customer_id FROM orders WHERE order_date >= '2025-01-01';

-- INTERSECT: Customers who placed orders AND submitted reviews (assuming review table exists)
-- MySQL doesn't support INTERSECT, emulate with INNER JOIN
-- Example only: Assume reviews table
-- SELECT customer_id FROM orders
-- INTERSECT
-- SELECT customer_id FROM reviews;
-- Emulated:
-- SELECT DISTINCT o.customer_id
-- FROM orders o
-- JOIN reviews r ON o.customer_id = r.customer_id;

-- CASE to categorize customers
SELECT c.customer_id, c.name,
  CASE
    WHEN AVG(oi.quantity * oi.price) > 50000 THEN 'High Spender'
    WHEN AVG(oi.quantity * oi.price) BETWEEN 10000 AND 50000 THEN 'Medium'
    ELSE 'Low'
  END AS spending_category
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY c.customer_id;

-- Filter orders by year
SELECT * FROM orders
WHERE YEAR(order_date) = YEAR(CURDATE());
