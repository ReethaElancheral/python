-- -------------------------------------------
-- Project 6: E-commerce Product Catalog
-- Requirements:
-- Create ecommerce_db.
-- Tables: products, brands, categories, users.
-- Each user can favorite products.
-- Use FOREIGN KEY constraints and insert dummy data.
-- SELECT queries:
--   - Get product details by category
--   - List products by brand
--   - Find most favorited products
-- -------------------------------------------

-- Create Database
CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

-- Create brands table
CREATE TABLE brands (
    brand_id INT PRIMARY KEY AUTO_INCREMENT,
    brand_name VARCHAR(100) NOT NULL UNIQUE
);

-- Create categories table
CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL UNIQUE
);

-- Create users table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    brand_id INT,
    category_id INT,
    FOREIGN KEY (brand_id) REFERENCES brands(brand_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- Create favorites table (many-to-many: users <-> products)
CREATE TABLE favorites (
    favorite_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    product_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert dummy brands
INSERT INTO brands (brand_name) VALUES
('Apple'), ('Samsung'), ('Nike'), ('Adidas');

-- Insert dummy categories
INSERT INTO categories (category_name) VALUES
('Electronics'), ('Footwear'), ('Clothing'), ('Accessories');

-- Insert dummy users
INSERT INTO users (username, email) VALUES
('alice', 'alice@example.com'),
('bob', 'bob@example.com'),
('carol', 'carol@example.com');

-- Insert dummy products
INSERT INTO products (product_name, price, brand_id, category_id) VALUES
('iPhone 14', 79999.00, 1, 1),
('Galaxy S23', 74999.00, 2, 1),
('Nike Air Max', 5999.00, 3, 2),
('Adidas Ultraboost', 6999.00, 4, 2),
('Apple Watch', 29999.00, 1, 4),
('Samsung Buds', 7999.00, 2, 4);

-- Insert dummy favorites
INSERT INTO favorites (user_id, product_id) VALUES
(1, 1), (1, 3), (2, 2), (2, 1), (3, 1), (3, 4), (3, 5);

-- -------------------------------------------
-- 📊 SELECT Queries
-- -------------------------------------------

-- 1. Get product details by category (e.g., Footwear)
SELECT 
    p.product_name, 
    c.category_name, 
    p.price
FROM products p
JOIN categories c ON p.category_id = c.category_id
WHERE c.category_name = 'Footwear';

-- 2. List products by brand (e.g., Apple)
SELECT 
    p.product_name, 
    b.brand_name, 
    p.price
FROM products p
JOIN brands b ON p.brand_id = b.brand_id
WHERE b.brand_name = 'Apple';

-- 3. Find most favorited products
SELECT 
    p.product_name, 
    COUNT(f.favorite_id) AS total_favorites
FROM products p
JOIN favorites f ON p.product_id = f.product_id
GROUP BY p.product_id
ORDER BY total_favorites DESC
LIMIT 5;
