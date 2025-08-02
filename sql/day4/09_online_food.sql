-- Project 9: Online Food Ordering Insights

CREATE DATABASE IF NOT EXISTS food_ordering_db;
USE food_ordering_db;

CREATE TABLE restaurants (
    restaurant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    area VARCHAR(100)
);

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    area VARCHAR(100)
);

CREATE TABLE dishes (
    dish_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    restaurant_id INT,
    price DECIMAL(10,2),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    restaurant_id INT,
    dish_id INT,
    order_date DATE,
    delivery_type ENUM('Delivery', 'Pickup'),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (dish_id) REFERENCES dishes(dish_id)
);

-- Insert sample data

INSERT INTO restaurants (name, area) VALUES
('Spice Hub', 'Downtown'),
('Green Leaf', 'Uptown'),
('Burger Barn', 'Downtown'),
('Sushi World', 'Midtown'),
('Pasta Palace', 'Uptown');

INSERT INTO customers (name, area) VALUES
('Alice', 'Downtown'),
('Bob', 'Uptown'),
('Charlie', 'Midtown'),
('Diana', 'Downtown'),
('Evan', 'Uptown');

INSERT INTO dishes (name, restaurant_id, price) VALUES
('Spicy Chicken', 1, 250),
('Vegan Salad', 2, 150),
('Cheeseburger', 3, 200),
('California Roll', 4, 300),
('Fettuccine Alfredo', 5, 350);

INSERT INTO orders (customer_id, restaurant_id, dish_id, order_date, delivery_type) VALUES
(1, 1, 1, '2025-07-20', 'Delivery'),
(2, 2, 2, '2025-07-21', 'Pickup'),
(3, 3, 3, '2025-07-22', 'Delivery'),
(4, 4, 4, '2025-07-23', 'Delivery'),
(5, 5, 5, '2025-07-24', 'Pickup'),
(1, 1, 1, '2025-07-25', 'Delivery'),
(2, 2, 2, '2025-07-26', 'Pickup');

-- Queries

-- 1. SELECT subquery to show dish popularity percentage
SELECT
  d.name AS dish_name,
  COUNT(o.order_id) AS order_count,
  (COUNT(o.order_id) * 100 / (SELECT COUNT(*) FROM orders)) AS popularity_percent
FROM dishes d
LEFT JOIN orders o ON d.dish_id = o.dish_id
GROUP BY d.dish_id, d.name;

-- 2. FROM subquery to calculate order volume by area
SELECT
  area,
  COUNT(*) AS total_orders
FROM (
  SELECT c.area, o.order_id
  FROM orders o
  JOIN customers c ON o.customer_id = c.customer_id
) AS sub
GROUP BY area;

-- 3. CASE to bucket customers based on total orders
SELECT
  c.name,
  COUNT(o.order_id) AS total_orders,
  CASE
    WHEN COUNT(o.order_id) >= 5 THEN 'Frequent'
    WHEN COUNT(o.order_id) BETWEEN 2 AND 4 THEN 'Regular'
    ELSE 'Occasional'
  END AS customer_type
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;

-- 4. Correlated subquery to get customer with highest order in each area
SELECT
  c.area,
  c.name,
  (SELECT COUNT(*) FROM orders o2 WHERE o2.customer_id = c.customer_id) AS orders_count
FROM customers c
WHERE (SELECT COUNT(*) FROM orders o2 WHERE o2.customer_id = c.customer_id) = (
  SELECT MAX(order_count) FROM (
    SELECT COUNT(*) AS order_count FROM orders o3
    JOIN customers c2 ON o3.customer_id = c2.customer_id
    WHERE c2.area = c.area
    GROUP BY o3.customer_id
  ) AS area_counts
);

-- 5. UNION ALL to compare delivery and pickup orders
SELECT 'Delivery' AS delivery_type, COUNT(*) AS total_orders
FROM orders
WHERE delivery_type = 'Delivery'
UNION ALL
SELECT 'Pickup' AS delivery_type, COUNT(*) AS total_orders
FROM orders
WHERE delivery_type = 'Pickup';

-- 6. Group orders by delivery date using date functions
SELECT
  order_date,
  COUNT(order_id) AS total_orders
FROM orders
GROUP BY order_date
ORDER BY order_date;

