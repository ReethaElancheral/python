--  5. Customer Order Journey Report 
-- Requirements: 
--  Track the journey of customers through the order process. 
--  Use ROW_NUMBER() to order events per customer. 
--  Use LAG() to find time between each order stage. 
--  Use WITH RECURSIVE if order states are hierarchical. 
--  Use RANK() to find customers with highest frequency. 

-- Create Database
CREATE DATABASE IF NOT EXISTS CustomerJourneyDB;
USE CustomerJourneyDB;

-- Tables
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_status (
    status_id INT PRIMARY KEY,
    name VARCHAR(50),
    next_status_id INT NULL,
    FOREIGN KEY (next_status_id) REFERENCES order_status(status_id)
);

CREATE TABLE order_journey (
    journey_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    status_id INT,
    status_date DATE,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (status_id) REFERENCES order_status(status_id)
);

-- Sample Data
INSERT INTO customers VALUES
(1,'Alice'),(2,'Bob'),(3,'Charlie');

INSERT INTO orders VALUES
(101,1,'2025-01-01'),
(102,2,'2025-01-02'),
(103,1,'2025-01-03');

INSERT INTO order_status VALUES
(1,'Placed',2),
(2,'Processed',3),
(3,'Shipped',4),
(4,'Delivered',NULL);

INSERT INTO order_journey (order_id, status_id, status_date) VALUES
(101,1,'2025-01-01'),
(101,2,'2025-01-02'),
(101,3,'2025-01-03'),
(101,4,'2025-01-05'),
(102,1,'2025-01-02'),
(102,2,'2025-01-04'),
(102,3,'2025-01-06'),
(103,1,'2025-01-03');

-- ROW_NUMBER() to order events per customer
WITH journey_order AS (
    SELECT j.journey_id, o.customer_id, c.name AS customer_name, j.order_id, s.name AS status_name, j.status_date,
           ROW_NUMBER() OVER (PARTITION BY o.customer_id, j.order_id ORDER BY j.status_date) AS step_no
    FROM order_journey j
    JOIN orders o ON j.order_id = o.order_id
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN order_status s ON j.status_id = s.status_id
)
SELECT * FROM journey_order
ORDER BY customer_id, order_id, step_no;

-- LAG() to find time between order stages
WITH journey_lag AS (
    SELECT j.journey_id, o.customer_id, c.name AS customer_name, j.order_id, s.name AS status_name, j.status_date,
           LAG(j.status_date) OVER (PARTITION BY o.customer_id, j.order_id ORDER BY j.status_date) AS prev_status_date
    FROM order_journey j
    JOIN orders o ON j.order_id = o.order_id
    JOIN customers c ON o.customer_id = c.customer_id
    JOIN order_status s ON j.status_id = s.status_id
)
SELECT customer_name, order_id, status_name, status_date,
       prev_status_date,
       DATEDIFF(status_date, prev_status_date) AS days_between_stages
FROM journey_lag
ORDER BY customer_id, order_id, status_date;

-- Recursive CTE: Track hierarchical order states
WITH RECURSIVE order_flow AS (
    SELECT status_id, name AS status_name, next_status_id, 1 AS level
    FROM order_status
    WHERE next_status_id IS NOT NULL
    UNION ALL
    SELECT os.status_id, os.name, os.next_status_id, of.level + 1
    FROM order_status os
    INNER JOIN order_flow of ON os.status_id = of.next_status_id
)
SELECT * FROM order_flow
ORDER BY level;

-- RANK() to find customers with highest order frequency
WITH order_count AS (
    SELECT customer_id, COUNT(order_id) AS total_orders
    FROM orders
    GROUP BY customer_id
)
SELECT c.customer_id, c.name AS customer_name, oc.total_orders,
       RANK() OVER (ORDER BY oc.total_orders DESC) AS rank_by_orders
FROM order_count oc
JOIN customers c ON oc.customer_id = c.customer_id;
