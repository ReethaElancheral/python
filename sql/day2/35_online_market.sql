-- Create database
CREATE DATABASE IF NOT EXISTS MarketplaceDB;
USE MarketplaceDB;

-- Sellers table
CREATE TABLE sellers (
    seller_id INT PRIMARY KEY,
    seller_name VARCHAR(100),
    city VARCHAR(100)
);

-- Buyers table
CREATE TABLE buyers (
    buyer_id INT PRIMARY KEY,
    buyer_name VARCHAR(100)
);

-- Products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    seller_id INT,
    FOREIGN KEY (seller_id) REFERENCES sellers(seller_id)
);

-- Purchases table
CREATE TABLE purchases (
    purchase_id INT PRIMARY KEY,
    product_id INT,
    buyer_id INT,
    quantity INT,
    purchase_date DATE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (buyer_id) REFERENCES buyers(buyer_id)
);


INSERT INTO sellers VALUES
(1, 'Arun Traders', 'Chennai'),
(2, 'Bright Mart', 'Delhi'),
(3, 'City Mart', 'Chennai'),
(4, 'Electro Zone', 'Bangalore');

INSERT INTO buyers VALUES
(101, 'Priya Shah'),
(102, 'Rohan Das'),
(103, 'Sneha Menon');

INSERT INTO products VALUES
(1001, 'LED TV', 45000, 4),
(1002, 'Mixer Grinder', 5000, 1),
(1003, 'Laptop', 60000, 2),
(1004, 'Smartphone', 20000, 2),
(1005, 'Rice Cooker', 3000, 1);

INSERT INTO purchases VALUES
(201, 1002, 101, 5, '2025-07-01'),
(202, 1003, 101, 2, '2025-07-03'),
(203, 1004, 102, 3, '2025-07-04'),
(204, 1001, 103, 1, '2025-07-05'),
(205, 1005, 102, 10, '2025-07-06');

-- 1. Revenue generated per seller
SELECT s.seller_name, SUM(p.quantity * pr.price) AS revenue
FROM purchases p
JOIN products pr ON p.product_id = pr.product_id
JOIN sellers s ON pr.seller_id = s.seller_id
GROUP BY s.seller_id;

-- 2. Most purchased products
SELECT pr.product_name, COUNT(p.purchase_id) AS total_purchases
FROM purchases p
JOIN products pr ON p.product_id = pr.product_id
GROUP BY pr.product_id
ORDER BY total_purchases DESC;

-- 3. Sellers with revenue > ₹1,00,000
SELECT s.seller_name, SUM(p.quantity * pr.price) AS revenue
FROM purchases p
JOIN products pr ON p.product_id = pr.product_id
JOIN sellers s ON pr.seller_id = s.seller_id
GROUP BY s.seller_id
HAVING revenue > 100000;

-- 4. LEFT JOIN: sellers and their products
SELECT s.seller_name, pr.product_name
FROM sellers s
LEFT JOIN products pr ON s.seller_id = pr.seller_id;

-- 5. SELF JOIN: sellers from the same city
SELECT s1.seller_name AS Seller1, s2.seller_name AS Seller2, s1.city
FROM sellers s1
JOIN sellers s2 ON s1.city = s2.city AND s1.seller_id < s2.seller_id;
