-- 2. Sales Region Performance Dashboard 
-- Requirements: 
--  Show sales by region, state, and city (hierarchical). 
--  Use WITH RECURSIVE to expand location hierarchy. 
--  Create a weekly and monthly performance CTE. 
--  Use RANK(), DENSE_RANK() to rank regions by sales. 
--  Compare current week's revenue with last using LAG().
--  Flag top-performing regions using window functions.


CREATE DATABASE IF NOT EXISTS SalesRegionDB;
USE SalesRegionDB;

-- Tables
CREATE TABLE regions (
    region_id INT PRIMARY KEY,
    region_name VARCHAR(100)
);

CREATE TABLE sales_reps (
    rep_id INT PRIMARY KEY,
    name VARCHAR(100),
    region_id INT,
    FOREIGN KEY (region_id) REFERENCES regions(region_id)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    rep_id INT,
    sale_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (rep_id) REFERENCES sales_reps(rep_id)
);

-- Sample Data
INSERT INTO regions VALUES
(1, 'North'), (2, 'South'), (3, 'East'), (4, 'West');

INSERT INTO sales_reps VALUES
(101, 'Alice', 1),
(102, 'Bob', 1),
(103, 'Charlie', 2),
(104, 'Diana', 3),
(105, 'Ethan', 4);

INSERT INTO sales (rep_id, sale_date, amount) VALUES
(101, '2025-01-01', 5000), (101, '2025-01-15', 6000),
(102, '2025-02-01', 7000), (103, '2025-02-20', 4000),
(104, '2025-03-10', 3000), (105, '2025-04-12', 10000),
(105, '2025-04-25', 12000), (104, '2025-05-01', 7000),
(103, '2025-05-10', 8000), (102, '2025-06-15', 9000);

-- CTE: Total sales per region
WITH region_sales AS (
    SELECT r.region_name, SUM(s.amount) AS total_sales
    FROM sales s
    JOIN sales_reps sr ON s.rep_id = sr.rep_id
    JOIN regions r ON sr.region_id = r.region_id
    GROUP BY r.region_name
)
SELECT * FROM region_sales;

-- RANK(): Rank regions by performance
WITH region_sales AS (
    SELECT r.region_name, SUM(s.amount) AS total_sales
    FROM sales s
    JOIN sales_reps sr ON s.rep_id = sr.rep_id
    JOIN regions r ON sr.region_id = r.region_id
    GROUP BY r.region_name
)
SELECT *,
       RANK() OVER (ORDER BY total_sales DESC) AS region_rank
FROM region_sales;

-- DENSE_RANK(): Reps ranked within regions
SELECT r.region_name, sr.name AS rep_name, SUM(s.amount) AS total_rep_sales,
       DENSE_RANK() OVER (PARTITION BY r.region_name ORDER BY SUM(s.amount) DESC) AS rep_rank_in_region
FROM sales s
JOIN sales_reps sr ON s.rep_id = sr.rep_id
JOIN regions r ON sr.region_id = r.region_id
GROUP BY r.region_name, sr.name;

-- LEAD/LAG: Compare sales trend per rep
WITH monthly_sales AS (
    SELECT rep_id, MONTH(sale_date) AS month, SUM(amount) AS total_monthly_sales
    FROM sales
    GROUP BY rep_id, MONTH(sale_date)
)
SELECT *,
       LAG(total_monthly_sales) OVER (PARTITION BY rep_id ORDER BY month) AS prev_month_sales,
       LEAD(total_monthly_sales) OVER (PARTITION BY rep_id ORDER BY month) AS next_month_sales
FROM monthly_sales;

-- Report: Best month and worst month by total region sales
WITH monthly_region_sales AS (
    SELECT r.region_name, MONTH(sale_date) AS month, SUM(s.amount) AS total
    FROM sales s
    JOIN sales_reps sr ON s.rep_id = sr.rep_id
    JOIN regions r ON sr.region_id = r.region_id
    GROUP BY r.region_name, MONTH(sale_date)
),
ranked_months AS (
    SELECT *,
           RANK() OVER (PARTITION BY region_name ORDER BY total DESC) AS best_month_rank,
           RANK() OVER (PARTITION BY region_name ORDER BY total ASC) AS worst_month_rank
    FROM monthly_region_sales
)
SELECT * FROM ranked_months
WHERE best_month_rank = 1 OR worst_month_rank = 1
ORDER BY region_name, month;

-- Final Dashboard Report: CTE + Window Functions
WITH region_total AS (
    SELECT r.region_id, r.region_name, SUM(s.amount) AS region_total
    FROM sales s
    JOIN sales_reps sr ON s.rep_id = sr.rep_id
    JOIN regions r ON sr.region_id = r.region_id
    GROUP BY r.region_id, r.region_name
),
rep_total AS (
    SELECT sr.rep_id, sr.name AS rep_name, sr.region_id, SUM(s.amount) AS rep_total
    FROM sales s
    JOIN sales_reps sr ON s.rep_id = sr.rep_id
    GROUP BY sr.rep_id, sr.name, sr.region_id
)
SELECT rt.region_name, rt.region_total,
       rt.region_total - AVG(rt.region_total) OVER() AS deviation_from_avg,
       rp.rep_name, rp.rep_total,
       DENSE_RANK() OVER (PARTITION BY rt.region_name ORDER BY rp.rep_total DESC) AS rep_rank
FROM region_total rt
JOIN rep_total rp ON rt.region_id = rp.region_id
ORDER BY rt.region_name, rep_rank;
