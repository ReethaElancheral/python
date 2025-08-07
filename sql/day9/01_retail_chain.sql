--  1. Retail Chain Sales Analysis System 
-- Requirements: 
--  Design a Star Schema: fact_sales, dimensions: time, store, product, 
-- customer. 
--  Use OLTP for real-time purchase logging. 
--  Use ETL to load into a fact_sales warehouse daily. 
--  Build OLAP reports: daily, monthly, and quarterly sales. 
--  Compare Star vs Snowflake design for performance.

-- Create Database
CREATE DATABASE IF NOT EXISTS RetailWarehouse;
USE RetailWarehouse;

-- Dimension Tables
CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    sales_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT
);

CREATE TABLE dim_store (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

-- Fact Table
CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    time_id INT,
    store_id INT,
    product_id INT,
    customer_id INT,
    quantity INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (store_id) REFERENCES dim_store(store_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);

-- Sample Dimension Data
INSERT INTO dim_time VALUES
(1,'2025-08-01',1,8,3,2025),
(2,'2025-08-02',2,8,3,2025);

INSERT INTO dim_store VALUES
(1,'Downtown Store','City Center'),
(2,'Mall Store','Mall Road');

INSERT INTO dim_product VALUES
(1,'Laptop','Electronics',70000),
(2,'Headphones','Electronics',2000);

INSERT INTO dim_customer VALUES
(1,'Alice','alice@example.com','Doha'),
(2,'Bob','bob@example.com','Doha');

-- Sample Fact Data (after ETL from OLTP)
INSERT INTO fact_sales (time_id, store_id, product_id, customer_id, quantity, total_amount)
VALUES
(1,1,1,1,1,70000),
(1,1,2,2,2,4000),
(2,2,1,2,1,70000);

-- OLAP Queries

-- Daily Sales
SELECT t.sales_date, SUM(f.total_amount) AS daily_sales
FROM fact_sales f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.sales_date;

-- Monthly Sales
SELECT t.year, t.month, SUM(f.total_amount) AS monthly_sales
FROM fact_sales f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.year, t.month;

-- Quarterly Sales
SELECT t.year, t.quarter, SUM(f.total_amount) AS quarterly_sales
FROM fact_sales f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.year, t.quarter;
