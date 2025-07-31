-- -----------------------------------------------
-- Project 13: Food Delivery Order Tracker
-- Requirements:
-- • Create food_delivery database
-- • Tables: restaurants, menus, orders, customers, delivery_agents
-- • Track orders, delivery status, and agent assigned
-- • Insert 10 menu items, 5 restaurants, 15 orders
-- • Queries:
--    - Pending deliveries
--    - Total revenue by restaurant
-- -----------------------------------------------

CREATE DATABASE IF NOT EXISTS food_delivery;
USE food_delivery;

-- Restaurants table
CREATE TABLE restaurants (
    restaurant_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    address VARCHAR(255)
);

-- Menus table
CREATE TABLE menus (
    menu_id INT PRIMARY KEY AUTO_INCREMENT,
    restaurant_id INT,
    item_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Delivery agents table
CREATE TABLE delivery_agents (
    agent_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20)
);

-- Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    menu_id INT,
    agent_id INT,
    order_date DATETIME,
    delivery_status ENUM('Pending', 'Delivered', 'Cancelled') DEFAULT 'Pending',
    quantity INT DEFAULT 1,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (menu_id) REFERENCES menus(menu_id),
    FOREIGN KEY (agent_id) REFERENCES delivery_agents(agent_id)
);

-- Insert restaurants
INSERT INTO restaurants (name, address) VALUES
('Pizza Palace', '123 Main St'),
('Burger Barn', '456 Oak Ave'),
('Sushi Spot', '789 Pine Rd'),
('Taco Town', '321 Maple Dr'),
('Curry Corner', '654 Elm St');

-- Insert menus (10 items)
INSERT INTO menus (restaurant_id, item_name, price) VALUES
(1, 'Margherita Pizza', 8.99),
(1, 'Pepperoni Pizza', 9.99),
(2, 'Cheeseburger', 7.50),
(2, 'Veggie Burger', 7.00),
(3, 'Salmon Sushi', 12.00),
(3, 'Tuna Roll', 10.00),
(4, 'Beef Taco', 3.00),
(4, 'Chicken Taco', 3.50),
(5, 'Chicken Curry', 11.00),
(5, 'Vegetable Curry', 10.00);

-- Insert customers (5 customers)
INSERT INTO customers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com'),
('Eva', 'eva@example.com');

-- Insert delivery agents (3 agents)
INSERT INTO delivery_agents (name, phone) VALUES
('Agent A', '555-0101'),
('Agent B', '555-0102'),
('Agent C', '555-0103');

-- Insert orders (15 orders)
INSERT INTO orders (customer_id, menu_id, agent_id, order_date, delivery_status, quantity) VALUES
(1, 1, 1, '2025-07-20 12:00:00', 'Pending', 1),
(2, 2, 2, '2025-07-20 12:15:00', 'Delivered', 2),
(3, 3, 3, '2025-07-20 12:30:00', 'Pending', 1),
(4, 4, 1, '2025-07-20 12:45:00', 'Delivered', 1),
(5, 5, 2, '2025-07-20 13:00:00', 'Cancelled', 3),
(1, 6, 3, '2025-07-20 13:15:00', 'Pending', 2),
(2, 7, 1, '2025-07-20 13:30:00', 'Delivered', 1),
(3, 8, 2, '2025-07-20 13:45:00', 'Pending', 1),
(4, 9, 3, '2025-07-20 14:00:00', 'Delivered', 1),
(5, 10, 1, '2025-07-20 14:15:00', 'Pending', 2),
(1, 1, 2, '2025-07-20 14:30:00', 'Delivered', 1),
(2, 3, 3, '2025-07-20 14:45:00', 'Pending', 1),
(3, 5, 1, '2025-07-20 15:00:00', 'Delivered', 2),
(4, 7, 2, '2025-07-20 15:15:00', 'Pending', 1),
(5, 9, 3, '2025-07-20 15:30:00', 'Delivered', 1);

-- -----------------------------------------------
-- Queries
-- -----------------------------------------------

-- 1. Pending deliveries (show orders not yet delivered)
SELECT 
    o.order_id,
    c.name AS customer_name,
    r.name AS restaurant_name,
    m.item_name,
    o.quantity,
    o.order_date,
    da.name AS delivery_agent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN menus m ON o.menu_id = m.menu_id
JOIN restaurants r ON m.restaurant_id = r.restaurant_id
JOIN delivery_agents da ON o.agent_id = da.agent_id
WHERE o.delivery_status = 'Pending'
ORDER BY o.order_date;

-- 2. Total revenue by restaurant
SELECT 
    r.name AS restaurant_name,
    SUM(m.price * o.quantity) AS total_revenue
FROM orders o
JOIN menus m ON o.menu_id = m.menu_id
JOIN restaurants r ON m.restaurant_id = r.restaurant_id
WHERE o.delivery_status = 'Delivered'
GROUP BY r.restaurant_id
ORDER BY total_revenue DESC;
