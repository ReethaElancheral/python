--  2. E-commerce Product Performance Warehouse 
-- Requirements: 
--  OLTP tables: orders, order_items, customers, products. 
--  Design a Snowflake Schema with normalized dimensions. 
--  Use ETL scripts to clean and load data into fact_orders. 
--  Create aggregation reports like top-selling products, seasonal trends. 
--  Show how OLAP queries (drill-down, roll-up) support decisions. 

CREATE DATABASE IF NOT EXISTS ECommerceWarehouse;
USE ECommerceWarehouse;

-- Dimension Tables (normalized for Snowflake)
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    city_id INT
);

CREATE TABLE dim_city (
    city_id INT PRIMARY KEY,
    city_name VARCHAR(50),
    state_name VARCHAR(50)
);

CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category_id INT
);

CREATE TABLE dim_category (
    category_id INT PRIMARY KEY,
    category_name VARCHAR(50)
);

CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    order_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT
);

-- Fact Table
CREATE TABLE fact_orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    product_id INT,
    time_id INT,
    quantity INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);

-- Sample Data
INSERT INTO dim_city VALUES (1,'Doha','Qatar');
INSERT INTO dim_customer VALUES (1,'Alice','Smith',1);
INSERT INTO dim_category VALUES (1,'Electronics');
INSERT INTO dim_product VALUES (1,'Laptop',1);
INSERT INTO dim_time VALUES (1,'2025-08-01',1,8,3,2025);

INSERT INTO fact_orders (customer_id, product_id, time_id, quantity, total_amount)
VALUES (1,1,1,1,70000);

-- OLAP Query: Top-selling Products
SELECT p.product_name, SUM(f.quantity) AS total_sold
FROM fact_orders f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;

-- Seasonal Trend (Monthly)
SELECT t.year, t.month, SUM(f.total_amount) AS monthly_sales
FROM fact_orders f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.year, t.month
ORDER BY t.year, t.month;
