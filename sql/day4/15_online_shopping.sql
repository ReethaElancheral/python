CREATE DATABASE IF NOT EXISTS shopping_cart_db;
USE shopping_cart_db;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE carts (
    cart_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    status ENUM('Completed', 'Abandoned'),
    created_at DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cart_items (
    cart_item_id INT AUTO_INCREMENT PRIMARY KEY,
    cart_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (cart_id) REFERENCES carts(cart_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert sample data

INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');

INSERT INTO products (name) VALUES ('Phone'), ('Laptop'), ('Headphones');

INSERT INTO carts (user_id, status, created_at) VALUES
(1, 'Abandoned', '2025-07-25'),
(2, 'Completed', '2025-07-20'),
(3, 'Abandoned', '2025-07-23'),
(1, 'Abandoned', '2025-07-27');

INSERT INTO orders (user_id, order_date) VALUES
(2, '2025-07-21');

INSERT INTO cart_items (cart_id, product_id, quantity) VALUES
(1, 1, 1), (1, 3, 2), (2, 2, 1), (3, 3, 1), (4, 1, 1);

-- Queries

-- 1. Subquery to find users who abandoned carts > 3 times
SELECT user_id, COUNT(cart_id) AS abandon_count
FROM carts
WHERE status = 'Abandoned'
GROUP BY user_id
HAVING abandon_count > 3;

-- 2. CASE to label cart status
SELECT cart_id, status,
CASE WHEN status = 'Completed' THEN 'Order Completed'
     WHEN status = 'Abandoned' THEN 'Order Abandoned'
     ELSE 'Unknown'
END AS cart_status_label
FROM carts;

-- 3. UNION for items added to cart and items purchased
SELECT ci.product_id, 'Added to Cart' AS status FROM cart_items ci
UNION
SELECT o.product_id, 'Purchased' AS status
FROM orders o
JOIN cart_items ci ON o.user_id = ci.cart_id;  -- Note: This join may need adjustment as no direct relation given

-- 4. Correlated subquery to find most abandoned product per user
SELECT
    user_id,
    (SELECT product_id
     FROM cart_items ci
     JOIN carts c ON ci.cart_id = c.cart_id
     WHERE c.user_id = u.user_id AND c.status = 'Abandoned'
     GROUP BY product_id ORDER BY COUNT(*) DESC LIMIT 1) AS most_abandoned_product
FROM users u;

-- 5. Date filtering for abandonments in the last week
SELECT * FROM carts WHERE status = 'Abandoned' AND created_at >= CURDATE() - INTERVAL 7 DAY;

-- 6. JOIN + GROUP BY to see cart conversion rate (example)
SELECT
    u.user_id,
    u.name,
    SUM(CASE WHEN c.status = 'Completed' THEN 1 ELSE 0 END) AS completed_carts,
    SUM(CASE WHEN c.status = 'Abandoned' THEN 1 ELSE 0 END) AS abandoned_carts
FROM users u
LEFT JOIN carts c ON u.user_id = c.user_id
GROUP BY u.user_id, u.name;
