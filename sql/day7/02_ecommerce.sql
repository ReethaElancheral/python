--  2. E-Commerce Order System 
-- Requirements: 
--  Create a view view_order_summary showing order_id, customer_name, 
-- total_amount (hiding discount logic). 
--  Use a stored procedure place_order() that inserts into multiple tables. 
--  Use a function get_order_total(order_id) to calculate total cost. 
--  Trigger after_order_insert logs new orders in order_audit. 
--  Limit employee access using read-only views of customer info. 

-- Create Database
CREATE DATABASE IF NOT EXISTS ecommerce_order_db;
USE ecommerce_order_db;

-- Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255)
);

-- Products Table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
);

-- Orders Table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    order_date DATE DEFAULT (CUR_DATE()),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order Items Table
CREATE TABLE order_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Discounts Table (hidden from summary view)
CREATE TABLE discounts (
    discount_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    discount_percent DECIMAL(5,2),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Order Audit Table
CREATE TABLE order_audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    log_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ========================
-- VIEW: view_order_summary
-- ========================
CREATE VIEW view_order_summary AS
SELECT 
    o.order_id,
    c.customer_name,
    SUM(p.price * oi.quantity) AS total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY o.order_id, c.customer_name;

-- ==========================
-- FUNCTION: get_order_total()
-- ==========================
DELIMITER //
CREATE FUNCTION get_order_total(input_order_id INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE total DECIMAL(10,2);
    SELECT SUM(p.price * oi.quantity)
    INTO total
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    WHERE oi.order_id = input_order_id;
    RETURN total;
END //
DELIMITER ;

-- ==================================
-- PROCEDURE: place_order()
-- ==================================
DELIMITER //
CREATE PROCEDURE place_order(
    IN input_customer_id INT,
    IN input_product_id INT,
    IN input_quantity INT
)
BEGIN
    DECLARE new_order_id INT;

    -- Insert new order
    INSERT INTO orders (customer_id) VALUES (input_customer_id);
    SET new_order_id = LAST_INSERT_ID();

    -- Insert order item
    INSERT INTO order_items (order_id, product_id, quantity)
    VALUES (new_order_id, input_product_id, input_quantity);

    -- Deduct stock
    UPDATE products 
    SET stock = stock - input_quantity
    WHERE product_id = input_product_id;
END //
DELIMITER ;

-- ============================================
-- TRIGGER: after_order_insert logs to order_audit
-- ============================================
DELIMITER //
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    INSERT INTO order_audit (order_id) VALUES (NEW.order_id);
END //
DELIMITER ;

-- ======================================
-- READ-ONLY VIEW for employee access
-- ======================================
CREATE VIEW view_customer_info AS
SELECT customer_id, customer_name, email
FROM customers
WITH CHECK OPTION;

-- Grant example (replace 'readonly_user' with actual user)
-- GRANT SELECT ON view_customer_info TO 'readonly_user'@'localhost';
-- REVOKE ALL PRIVILEGES ON customers FROM 'readonly_user'@'localhost';

-- =====================
-- SAMPLE INSERTS
-- =====================
INSERT INTO customers (customer_name, email, address)
VALUES ('Ravi Kumar', 'ravi@example.com', 'Mumbai'),
       ('Asha Mehta', 'asha@example.com', 'Delhi');

INSERT INTO products (product_name, price, stock)
VALUES ('Laptop', 60000, 20),
       ('Headphones', 2000, 100),
       ('Keyboard', 1500, 50);
