--  5. Online Food Delivery Reporting System 
-- Requirements: 
--  OLTP for real-time orders, drivers, restaurants. 
--  Create Snowflake Schema with normalized customer and location tables. 
--  ETL includes data cleanup, time parsing, and cost breakdown. 
--  Aggregation reports: avg delivery time by region, food category trends. 
--  OLAP queries for city-wise, vendor-wise KPIs.

-- Create Database
CREATE DATABASE IF NOT EXISTS FoodDeliveryWarehouse;
USE FoodDeliveryWarehouse;

-- Dimension Tables

-- Customer dimension
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    region VARCHAR(50)
);

-- Restaurant dimension
CREATE TABLE dim_restaurant (
    restaurant_id INT PRIMARY KEY,
    restaurant_name VARCHAR(100),
    cuisine_type VARCHAR(50),
    city VARCHAR(50)
);

-- Food item dimension
CREATE TABLE dim_food_item (
    food_id INT PRIMARY KEY,
    food_name VARCHAR(100),
    category VARCHAR(50),
    restaurant_id INT,
    FOREIGN KEY (restaurant_id) REFERENCES dim_restaurant(restaurant_id)
);

-- Time dimension
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
    restaurant_id INT,
    food_id INT,
    time_id INT,
    order_time TIME,
    delivery_time TIME,
    delivery_duration_minutes INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (restaurant_id) REFERENCES dim_restaurant(restaurant_id),
    FOREIGN KEY (food_id) REFERENCES dim_food_item(food_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);

-- Sample Dimension Data
INSERT INTO dim_customer VALUES
(1,'Alice','Doha','West'),
(2,'Bob','Doha','West'),
(3,'Charlie','Al Wakrah','South');

INSERT INTO dim_restaurant VALUES
(1,'Pizza Heaven','Italian','Doha'),
(2,'Sushi World','Japanese','Doha');

INSERT INTO dim_food_item VALUES
(1,'Margherita Pizza','Pizza',1),
(2,'Pepperoni Pizza','Pizza',1),
(3,'Sushi Roll','Sushi',2);

INSERT INTO dim_time VALUES
(1,'2025-08-01',1,8,3,2025),
(2,'2025-08-02',2,8,3,2025);

-- Sample Fact Data (after ETL)
INSERT INTO fact_orders (customer_id, restaurant_id, food_id, time_id, order_time, delivery_time, delivery_duration_minutes, total_amount)
VALUES
(1,1,1,1,'12:00:00','12:30:00',30,15.50),
(2,1,2,1,'13:00:00','13:25:00',25,18.00),
(3,2,3,2,'18:00:00','18:40:00',40,22.00);

-- OLAP Queries

-- Average Delivery Time by Region
SELECT c.region, AVG(f.delivery_duration_minutes) AS avg_delivery_time
FROM fact_orders f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.region;

-- Food Category Trends (total orders per category)
SELECT fi.category, COUNT(f.order_id) AS total_orders, SUM(f.total_amount) AS revenue
FROM fact_orders f
JOIN dim_food_item fi ON f.food_id = fi.food_id
GROUP BY fi.category
ORDER BY total_orders DESC;

-- City-wise Total Revenue
SELECT c.city, SUM(f.total_amount) AS city_revenue
FROM fact_orders f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.city
ORDER BY city_revenue DESC;

-- Vendor-wise KPI: average delivery time per restaurant
SELECT r.restaurant_name, AVG(f.delivery_duration_minutes) AS avg_delivery_time
FROM fact_orders f
JOIN dim_restaurant r ON f.restaurant_id = r.restaurant_id
GROUP BY r.restaurant_name
ORDER BY avg_delivery_time ASC;

-- Monthly Revenue Trend per Cuisine Type
SELECT r.cuisine_type, t.month, t.year, SUM(f.total_amount) AS revenue
FROM fact_orders f
JOIN dim_restaurant r ON f.restaurant_id = r.restaurant_id
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY r.cuisine_type, t.year, t.month
ORDER BY t.year, t.month;
