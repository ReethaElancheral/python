-- Project 3: Sales Performance Analyzer for Retail Chain

CREATE DATABASE IF NOT EXISTS RetailSalesDB;
USE RetailSalesDB;

-- Create tables
CREATE TABLE stores (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    store_id INT,
    product_id INT,
    employee_id INT,
    sale_date DATE,
    sale_type VARCHAR(20), -- 'Online' or 'Offline'
    quantity INT,
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

-- Insert sample data
INSERT INTO stores VALUES
(1, 'Store A', 'North'),
(2, 'Store B', 'South'),
(3, 'Store C', 'East');

INSERT INTO products VALUES
(1, 'Laptop', 'Electronics', 60000),
(2, 'Smartphone', 'Electronics', 25000),
(3, 'Headphones', 'Accessories', 2000);

INSERT INTO employees VALUES
(1, 'Rahul', 'North'),
(2, 'Priya', 'South'),
(3, 'Kiran', 'East');

INSERT INTO sales VALUES
(1, 1, 1, 1, '2025-06-01', 'Offline', 5),
(2, 1, 2, 1, '2025-06-02', 'Online', 10),
(3, 2, 2, 2, '2025-06-03', 'Offline', 8),
(4, 3, 3, 3, '2025-07-01', 'Online', 20),
(5, 2, 3, 2, '2025-07-05', 'Offline', 15);

-- Subquery in SELECT: each store’s revenue as % of total
SELECT s.store_name,
       SUM(p.price * sa.quantity) AS store_revenue,
       ROUND((SUM(p.price * sa.quantity) / (SELECT SUM(p.price * sa.quantity)
                                            FROM sales sa
                                            JOIN products p ON sa.product_id = p.product_id)) * 100, 2) AS revenue_percentage
FROM sales sa
JOIN stores s ON sa.store_id = s.store_id
JOIN products p ON sa.product_id = p.product_id
GROUP BY s.store_name;

-- Correlated subquery: top performer in each region
SELECT e1.name, e1.region
FROM employees e1
WHERE employee_id = (
    SELECT s.employee_id
    FROM sales s
    JOIN stores st ON s.store_id = st.store_id
    WHERE st.region = e1.region
    GROUP BY s.employee_id
    ORDER BY SUM(s.quantity * (SELECT price FROM products WHERE product_id = s.product_id)) DESC
    LIMIT 1
);

-- UNION: online and offline sales
SELECT * FROM sales WHERE sale_type = 'Online'
UNION
SELECT * FROM sales WHERE sale_type = 'Offline';

-- CASE WHEN to group products
SELECT product_name, price,
    CASE
        WHEN price >= 50000 THEN 'Top Seller'
        WHEN price >= 10000 THEN 'Medium'
        ELSE 'Low'
    END AS product_category
FROM products;

-- Monthly sales trend
SELECT MONTH(sale_date) AS sale_month, YEAR(sale_date) AS sale_year,
       SUM(quantity * p.price) AS monthly_revenue
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY YEAR(sale_date), MONTH(sale_date)
ORDER BY sale_year, sale_month;

-- Store-level performance with JOIN + GROUP BY + SUM
SELECT st.store_name, SUM(p.price * s.quantity) AS total_sales
FROM sales s
JOIN stores st ON s.store_id = st.store_id
JOIN products p ON s.product_id = p.product_id
GROUP BY st.store_id, st.store_name;
