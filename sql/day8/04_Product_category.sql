--  4. Product Category Tree Analysis 
-- Requirements: 
--  Products belong to categories → subcategories (hierarchical). 
--  Use WITH RECURSIVE to display full category tree. 
--  Rank categories by total product count. 
--  Use LEAD()/LAG() to track category movement over time. 
--  Use CTEs to create product availability report.

-- Create Database
CREATE DATABASE IF NOT EXISTS ProductCategoryDB;
USE ProductCategoryDB;

-- Tables
CREATE TABLE categories (
    category_id INT PRIMARY KEY,
    name VARCHAR(100),
    parent_id INT NULL,
    FOREIGN KEY (parent_id) REFERENCES categories(category_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    category_id INT,
    price DECIMAL(10,2),
    stock INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Sample Data
INSERT INTO categories VALUES
(1,'Electronics',NULL),
(2,'Mobiles',1),
(3,'Laptops',1),
(4,'Home Appliances',NULL),
(5,'Refrigerators',4),
(6,'Microwaves',4);

INSERT INTO products VALUES
(1,'iPhone 14',2,90000,50),
(2,'Samsung Galaxy S23',2,70000,40),
(3,'Dell XPS 13',3,120000,25),
(4,'HP Spectre x360',3,110000,20),
(5,'LG Fridge',5,50000,15),
(6,'Samsung Microwave',6,12000,30);

-- Recursive CTE: Display full category tree
WITH RECURSIVE category_tree AS (
    SELECT category_id, name, parent_id, 1 AS level
    FROM categories
    WHERE parent_id IS NULL
    UNION ALL
    SELECT c.category_id, c.name, c.parent_id, ct.level + 1
    FROM categories c
    INNER JOIN category_tree ct ON c.parent_id = ct.category_id
)
SELECT * FROM category_tree
ORDER BY level, parent_id;

-- CTE: Product availability per category
WITH product_availability AS (
    SELECT c.category_id, c.name AS category_name,
           SUM(p.stock) AS total_stock,
           COUNT(p.product_id) AS total_products
    FROM categories c
    LEFT JOIN products p ON c.category_id = p.category_id
    GROUP BY c.category_id, c.name
)
SELECT * FROM product_availability
ORDER BY total_stock DESC;

-- Rank categories by total products
WITH product_counts AS (
    SELECT c.category_id, c.name AS category_name,
           COUNT(p.product_id) AS product_count
    FROM categories c
    LEFT JOIN products p ON c.category_id = p.category_id
    GROUP BY c.category_id, c.name
)
SELECT *, RANK() OVER (ORDER BY product_count DESC) AS rank_by_products
FROM product_counts;

-- Track category product stock movement using LEAD/LAG
WITH stock_movement AS (
    SELECT category_id, name AS category_name, SUM(stock) AS total_stock
    FROM products p
    JOIN categories c ON p.category_id = c.category_id
    GROUP BY category_id, name
)
SELECT category_name, total_stock,
       LAG(total_stock) OVER (ORDER BY category_id) AS prev_stock,
       LEAD(total_stock) OVER (ORDER BY category_id) AS next_stock
FROM stock_movement;

-- Final: Full category tree with product counts
WITH RECURSIVE category_tree AS (
    SELECT category_id, name, parent_id, 1 AS level
    FROM categories
    WHERE parent_id IS NULL
    UNION ALL
    SELECT c.category_id, c.name, c.parent_id, ct.level + 1
    FROM categories c
    INNER JOIN category_tree ct ON c.parent_id = ct.category_id
),
category_summary AS (
    SELECT c.category_id, c.name AS category_name,
           SUM(p.stock) AS total_stock,
           COUNT(p.product_id) AS total_products
    FROM categories c
    LEFT JOIN products p ON c.category_id = p.category_id
    GROUP BY c.category_id, c.name
)
SELECT ct.level, ct.category_id, ct.name AS category_name, cs.total_products, cs.total_stock
FROM category_tree ct
LEFT JOIN category_summary cs ON ct.category_id = cs.category_id
ORDER BY ct.level, ct.category_id;
