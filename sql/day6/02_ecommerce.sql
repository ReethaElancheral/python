--  2. E-Commerce Product Catalog 
-- Requirements: 
--  Tables: products, categories, suppliers, inventory, orders, order_items 
--  Design schema in 3NF; show how to denormalize into a reporting table. 
--  Create indexes on product_name, category_id, supplier_id. 
--  Use EXPLAIN to optimize product search with filters. 
--  Use a subquery to find products with the highest sales. 
--  Compare JOIN performance with and without indexing. 
--  Use LIMIT for "Top 10 most ordered products" display.

CREATE DATABASE IF NOT EXISTS ecommerce_catalog_db;
USE ecommerce_catalog_db;

-- 2. Normalized Tables
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255),
    category_id INT,
    supplier_id INT,
    price DECIMAL(10,2),
    stock INT,
    INDEX idx_product_name (product_name),
    INDEX idx_category_id (category_id),
    INDEX idx_supplier_id (supplier_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_date DATE
);

CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 3. Denormalized Reporting Table
CREATE TABLE product_sales_report (
    product_id INT,
    total_quantity INT,
    total_revenue DECIMAL(10,2),
    PRIMARY KEY (product_id)
);

-- 4. Sample Data
INSERT INTO categories (name) VALUES ('Electronics'), ('Toys');
INSERT INTO suppliers (name) VALUES ('Samsung'), ('Lego');

INSERT INTO products (product_name, category_id, supplier_id, price, stock)
VALUES 
('Smartphone', 1, 1, 29999.99, 100),
('Building Blocks', 2, 2, 999.99, 200);

INSERT INTO orders (order_date) VALUES ('2025-08-01'), ('2025-08-02');

INSERT INTO order_items (order_id, product_id, quantity)
VALUES 
(1, 1, 2),
(2, 2, 5);

-- 5. EXPLAIN Optimized Query
EXPLAIN SELECT * FROM products WHERE category_id = 1 AND supplier_id = 1;

-- 6. Subquery: Highest Selling Product
SELECT product_id, SUM(quantity) AS total
FROM order_items
GROUP BY product_id
ORDER BY total DESC
LIMIT 1;

-- 7. Compare JOIN performance (with and without index shown via EXPLAIN)
EXPLAIN
SELECT p.product_name, s.name AS supplier
FROM products p
JOIN suppliers s ON p.supplier_id = s.supplier_id;

-- 8. LIMIT: Top 10 Products
SELECT product_id, SUM(quantity) AS sold_units
FROM order_items
GROUP BY product_id
ORDER BY sold_units DESC
LIMIT 10;

-- 9. Denormalized Reporting Table Update
INSERT INTO product_sales_report (product_id, total_quantity, total_revenue)
SELECT 
    oi.product_id,
    SUM(oi.quantity),
    SUM(oi.quantity * p.price)
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY oi.product_id;
