-- 6. Restaurant Order Management
-- Requirements:
-- Tables: menu_items, orders, customers, staff.
-- Use INNER JOIN to list full orders with customer and waiter info.
-- Use LIKE '%Pizza%' to find pizza items.
-- Use GROUP BY to get total orders per staff.
-- Use ORDER BY on amount and customer name.
-- Use CASE WHEN for categorizing customers (New/Returning).
-- Use subquery to find customers who ordered more than 5 times.
-- Combine dine-in and delivery data using UNION.


CREATE DATABASE IF NOT EXISTS RestaurantDB;
USE RestaurantDB;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE staff (
    staff_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    role ENUM('Waiter', 'Chef', 'Manager')
);

CREATE TABLE menu_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(6,2)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    staff_id INT,
    item_id INT,
    order_type ENUM('Dine-In', 'Delivery'),
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (item_id) REFERENCES menu_items(item_id)
);

-- Insert Sample Data

INSERT INTO customers (name, phone) VALUES
('Amit Sinha', '9876543210'),
('Riya Kapoor', '9123456789'),
('Arjun Rao', '9012345678'),
('Priya Mehta', '9345678901');

INSERT INTO staff (name, role) VALUES
('Karan Thakur', 'Waiter'),
('Sunita Iyer', 'Chef'),
('Raj Patel', 'Waiter'),
('Anjali Deshmukh', 'Manager');

INSERT INTO menu_items (name, category, price) VALUES
('Margherita Pizza', 'Main Course', 300.00),
('Pepperoni Pizza', 'Main Course', 350.00),
('Veg Biryani', 'Main Course', 280.00),
('Chocolate Cake', 'Dessert', 150.00),
('Garlic Bread', 'Starter', 120.00);

INSERT INTO orders (customer_id, staff_id, item_id, order_type, quantity, order_date) VALUES
(1, 1, 1, 'Dine-In', 2, '2025-07-01'),
(2, 3, 2, 'Delivery', 1, '2025-07-02'),
(3, 1, 3, 'Dine-In', 3, '2025-07-03'),
(4, 3, 4, 'Delivery', 1, '2025-07-04'),
(1, 1, 5, 'Dine-In', 1, '2025-07-05'),
(2, 3, 1, 'Dine-In', 1, '2025-07-06'),
(2, 1, 2, 'Dine-In', 2, '2025-07-07'),
(3, 1, 4, 'Delivery', 1, '2025-07-08');

-- Queries

-- 1. INNER JOIN to list full orders with customer and waiter info
SELECT o.order_id, c.name AS customer_name, s.name AS waiter_name, m.name AS item, o.quantity, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN staff s ON o.staff_id = s.staff_id
JOIN menu_items m ON o.item_id = m.item_id
WHERE s.role = 'Waiter';

-- 2. LIKE '%Pizza%' to find pizza items
SELECT * FROM menu_items
WHERE name LIKE '%Pizza%';

-- 3. GROUP BY to get total orders per staff
SELECT s.name AS staff_name, COUNT(o.order_id) AS total_orders
FROM orders o
JOIN staff s ON o.staff_id = s.staff_id
GROUP BY s.staff_id;

-- 4. ORDER BY on amount and customer name
SELECT c.name AS customer_name,
       m.name AS item_name,
       o.quantity,
       (o.quantity * m.price) AS total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN menu_items m ON o.item_id = m.item_id
ORDER BY total_amount DESC, customer_name ASC;

-- 5. CASE WHEN for categorizing customers (New/Returning)
SELECT c.name,
       COUNT(o.order_id) AS total_orders,
       CASE
           WHEN COUNT(o.order_id) = 1 THEN 'New'
           ELSE 'Returning'
       END AS customer_type
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

-- 6. Subquery to find customers who ordered more than 5 times
SELECT name
FROM customers
WHERE customer_id IN (
    SELECT customer_id
    FROM orders
    GROUP BY customer_id
    HAVING COUNT(order_id) > 5
);

-- 7. Combine dine-in and delivery data using UNION
SELECT o.order_id, c.name AS customer_name, 'Dine-In' AS type, o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_type = 'Dine-In'

UNION

SELECT o.order_id, c.name, 'Delivery', o.order_date
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.order_type = 'Delivery';
