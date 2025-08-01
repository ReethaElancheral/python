-- Project 8: Food Delivery Platform

CREATE DATABASE IF NOT EXISTS food_delivery_db;
USE food_delivery_db;

-- Tables

CREATE TABLE restaurants (
    restaurant_id INT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    restaurant_id INT,
    delivery_agent_id INT,
    order_value DECIMAL(10,2),
    order_date DATE,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

CREATE TABLE order_items (
    item_id INT PRIMARY KEY,
    order_id INT,
    item_name VARCHAR(100),
    price DECIMAL(10,2),
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

CREATE TABLE delivery_agents (
    agent_id INT PRIMARY KEY,
    name VARCHAR(100),
    contact VARCHAR(20)
);

-- Sample Data

INSERT INTO restaurants (restaurant_id, name, location) VALUES
(1, 'Spice Hub', 'Delhi'),
(2, 'Burger Binge', 'Mumbai'),
(3, 'Pasta Point', 'Delhi'),
(4, 'Sushi Station', 'Bangalore');

INSERT INTO delivery_agents (agent_id, name, contact) VALUES
(1, 'Arjun', '9999888877'),
(2, 'Meera', '8888777766'),
(3, 'Raj', '7777666655');

INSERT INTO orders (order_id, restaurant_id, delivery_agent_id, order_value, order_date) VALUES
(1, 1, 1, 1200.00, '2025-07-01'),
(2, 1, 2, 2200.00, '2025-07-02'),
(3, 2, 1, 1800.00, '2025-07-03'),
(4, 3, 3, 5000.00, '2025-07-04'),
(5, 3, 2, 9000.00, '2025-07-04'),
(6, 1, 1, 15000.00, '2025-07-05'),
(7, 1, 3, 18000.00, '2025-07-06'),
(8, 1, 2, 11000.00, '2025-07-07');

INSERT INTO order_items (item_id, order_id, item_name, price, quantity) VALUES
(1, 1, 'Paneer Tikka', 300, 2),
(2, 1, 'Naan', 50, 4),
(3, 2, 'Butter Chicken', 400, 2),
(4, 3, 'Burger', 200, 3),
(5, 4, 'Pasta', 250, 4),
(6, 5, 'Pizza', 450, 4),
(7, 6, 'Biryani', 350, 5),
(8, 7, 'Thali', 500, 6),
(9, 8, 'Kebab', 600, 3);

-- Queries

-- 1. Total orders per restaurant
SELECT 
    r.name AS restaurant_name,
    COUNT(o.order_id) AS total_orders
FROM restaurants r
JOIN orders o ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_id, r.name;

-- 2. Sum of order values per delivery agent
SELECT 
    d.name AS agent_name,
    SUM(o.order_value) AS total_delivery_value
FROM delivery_agents d
JOIN orders o ON d.agent_id = o.delivery_agent_id
GROUP BY d.agent_id, d.name;

-- 3. Restaurants with revenue > ₹50,000
SELECT 
    r.name AS restaurant_name,
    SUM(o.order_value) AS total_revenue
FROM restaurants r
JOIN orders o ON r.restaurant_id = o.restaurant_id
GROUP BY r.restaurant_id, r.name
HAVING total_revenue > 50000;

-- 4. INNER JOIN: restaurants ↔ orders
SELECT 
    r.name AS restaurant_name,
    o.order_id,
    o.order_value,
    o.order_date
FROM restaurants r
INNER JOIN orders o ON r.restaurant_id = o.restaurant_id;

-- 5. LEFT JOIN: delivery agents ↔ orders
SELECT 
    d.name AS agent_name,
    o.order_id,
    o.order_value
FROM delivery_agents d
LEFT JOIN orders o ON d.agent_id = o.delivery_agent_id;

-- 6. SELF JOIN: restaurants in same location
SELECT 
    r1.name AS restaurant_1,
    r2.name AS restaurant_2,
    r1.location
FROM restaurants r1
JOIN restaurants r2 ON r1.location = r2.location AND r1.restaurant_id < r2.restaurant_id;
