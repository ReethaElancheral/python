-- 9. E-commerce Product Movement 
-- Requirements: 
--  Track top products in sales weekly/monthly. 
--  Use RANK() and DENSE_RANK() for weekly top charts. 
--  Use LAG() to show previous position in sales rank. 
--  Use CTEs to track product performance over time.

-- Create Database
CREATE DATABASE IF NOT EXISTS ECommerceDB;
USE ECommerceDB;

-- Tables
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    sale_date DATE,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Sample Data
INSERT INTO products VALUES
(1,'Laptop'),
(2,'Smartphone'),
(3,'Headphones'),
(4,'Camera');

INSERT INTO sales (product_id, sale_date, quantity) VALUES
(1,'2025-07-01',10),
(2,'2025-07-01',5),
(3,'2025-07-01',7),
(1,'2025-07-08',8),
(2,'2025-07-08',12),
(4,'2025-07-08',6),
(3,'2025-07-15',9),
(1,'2025-07-15',4),
(2,'2025-07-15',10);

-- CTE: Weekly product sales
WITH weekly_sales AS (
    SELECT product_id, 
           YEARWEEK(sale_date, 1) AS year_week,
           SUM(quantity) AS total_quantity
    FROM sales
    GROUP BY product_id, YEARWEEK(sale_date, 1)
)
-- Weekly ranking using RANK() and DENSE_RANK()
SELECT ws.product_id, p.name, ws.year_week, ws.total_quantity,
       RANK() OVER (PARTITION BY ws.year_week ORDER BY ws.total_quantity DESC) AS rank_week,
       DENSE_RANK() OVER (PARTITION BY ws.year_week ORDER BY ws.total_quantity DESC) AS dense_rank_week
FROM weekly_sales ws
JOIN products p ON ws.product_id = p.product_id
ORDER BY ws.year_week, rank_week;

-- Track previous week's rank using LAG()
WITH weekly_sales_rank AS (
    SELECT ws.product_id, p.name, ws.year_week, ws.total_quantity,
           RANK() OVER (PARTITION BY ws.year_week ORDER BY ws.total_quantity DESC) AS rank_week
    FROM (
        SELECT product_id, YEARWEEK(sale_date, 1) AS year_week, SUM(quantity) AS total_quantity
        FROM sales
        GROUP BY product_id, YEARWEEK(sale_date, 1)
    ) ws
    JOIN products p ON ws.product_id = p.product_id
)
SELECT *,
       LAG(rank_week) OVER (PARTITION BY product_id ORDER BY year_week) AS prev_week_rank
FROM weekly_sales_rank
ORDER BY year_week, rank_week;

-- CTE to track product performance over time
WITH product_performance AS (
    SELECT p.product_id, p.name, s.sale_date, s.quantity,
           SUM(s.quantity) OVER (PARTITION BY s.product_id ORDER BY s.sale_date) AS cumulative_sales
    FROM sales s
    JOIN products p ON s.product_id = p.product_id
)
SELECT * FROM product_performance
ORDER BY product_id, sale_date;
