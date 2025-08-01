-- Project 18: Online Order Management
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    total DECIMAL(10,2),
    order_date DATE,
    status VARCHAR(20),
    address TEXT
);

INSERT INTO orders (order_id, customer_name, total, order_date, status, address) VALUES
(1, 'Ravi Kumar', 2500, '2025-07-20', 'Shipped', '123 Main St'),
(2, 'Reena Sharma', 1500, '2025-07-21', NULL, '456 Oak Rd'),
(3, 'Rajesh Gupta', 3200, '2025-07-22', 'Delivered', '789 Pine Ave'),
(4, 'Rina Das', 2800, '2025-07-23', 'Pending', '321 Elm St'),
(5, 'Rakesh Jain', 4000, '2025-07-24', 'Cancelled', '654 Maple Blvd');

SELECT * FROM orders WHERE order_date BETWEEN CURDATE() - INTERVAL 7 DAY AND CURDATE();
SELECT * FROM orders WHERE customer_name LIKE 'R%';
SELECT * FROM orders WHERE status IS NULL;
SELECT DISTINCT address FROM orders;
SELECT * FROM orders ORDER BY order_date DESC, total DESC;