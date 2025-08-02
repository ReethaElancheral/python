CREATE DATABASE IF NOT EXISTS warehouse_db;
USE warehouse_db;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    reorder_level INT,
    category VARCHAR(100)
);

CREATE TABLE inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    stock_quantity INT,
    last_stocked DATE,
    expiry_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity_ordered INT,
    order_date DATE,
    delivery_delay_days INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE deliveries (
    delivery_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    supplier_id INT,
    delivery_date DATE,
    delayed_days INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Sample data

INSERT INTO products (name, reorder_level, category) VALUES
('Product A', 20, 'Fast'),
('Product B', 50, 'Medium'),
('Product C', 30, 'Slow');

INSERT INTO inventory (product_id, stock_quantity, last_stocked, expiry_date) VALUES
(1, 15, '2025-07-01', '2026-01-01'),
(2, 55, '2025-06-15', '2026-02-01'),
(3, 25, '2025-07-10', '2025-12-01');

INSERT INTO orders (product_id, quantity_ordered, order_date, delivery_delay_days) VALUES
(1, 100, '2025-07-05', 2),
(2, 200, '2025-07-01', 0),
(3, 50, '2025-07-10', 5);

INSERT INTO suppliers (name) VALUES ('Supplier X'), ('Supplier Y');

INSERT INTO deliveries (order_id, supplier_id, delivery_date, delayed_days) VALUES
(1, 1, '2025-07-07', 2),
(2, 2, '2025-07-02', 0),
(3, 1, '2025-07-15', 5);

-- Queries

-- 1. Subquery in WHERE to show products below reorder level
SELECT * FROM products
WHERE product_id IN (
    SELECT product_id FROM inventory WHERE stock_quantity < reorder_level
);

-- 2. CASE to categorize products as Fast, Medium, Slow moving
SELECT
    name,
    category,
    CASE
        WHEN category = 'Fast' THEN 'Fast Moving'
        WHEN category = 'Medium' THEN 'Medium Moving'
        WHEN category = 'Slow' THEN 'Slow Moving'
        ELSE 'Unknown'
    END AS movement_category
FROM products;

-- 3. Correlated subquery to get supplier with least delayed deliveries
SELECT
    supplier_id,
    (SELECT MIN(delayed_days) FROM deliveries d2 WHERE d2.supplier_id = d.supplier_id) AS least_delay
FROM deliveries d
GROUP BY supplier_id;

-- 4. JOIN + GROUP BY for fulfillment rate by supplier
SELECT
    s.name AS supplier_name,
    COUNT(d.delivery_id) AS total_deliveries,
    SUM(CASE WHEN d.delayed_days > 0 THEN 0 ELSE 1 END) / COUNT(d.delivery_id) * 100 AS fulfillment_rate_percentage
FROM suppliers s
LEFT JOIN deliveries d ON s.supplier_id = d.supplier_id
GROUP BY s.supplier_id;

-- 5. UNION ALL for online and offline stock (assuming inventory has a source column)
-- For demo, we simulate with dummy data

SELECT product_id, stock_quantity, 'Online' AS stock_source FROM inventory WHERE stock_quantity > 0
UNION ALL
SELECT product_id, stock_quantity, 'Offline' AS stock_source FROM inventory WHERE stock_quantity <= 0;

-- 6. Date filtering for expiry tracking (products expiring in next 30 days)
SELECT * FROM inventory WHERE expiry_date BETWEEN CURDATE() AND CURDATE() + INTERVAL 30 DAY;
