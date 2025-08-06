--  4. Online Food Delivery Platform 
-- Requirements: 
--  View view_menu_items for customers (hides supplier cost). 
--  Procedure place_food_order() to insert order, deduct stock, and return 
-- receipt. 
--  Function get_delivery_eta(order_id) for expected delivery. 
--  Trigger after_order_placed inserts into delivery_queue. 
--  Admins access full data; customers access limited view. 

-- Create Database
CREATE DATABASE IF NOT EXISTS FoodDeliveryDB;
USE FoodDeliveryDB;

-- Table: suppliers
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    contact VARCHAR(50)
);

-- Table: food_items
CREATE TABLE food_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT,
    supplier_cost DECIMAL(10,2),
    supplier_id INT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Table: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    address TEXT
);

-- Table: food_orders
CREATE TABLE food_orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATETIME,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Table: order_items
CREATE TABLE order_items (
    item_id INT,
    order_id INT,
    quantity INT,
    price DECIMAL(10,2),
    FOREIGN KEY (item_id) REFERENCES food_items(item_id),
    FOREIGN KEY (order_id) REFERENCES food_orders(order_id)
);

-- Table: delivery_queue
CREATE TABLE delivery_queue (
    queue_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    status VARCHAR(50),
    eta DATETIME,
    FOREIGN KEY (order_id) REFERENCES food_orders(order_id)
);

-- Sample Data
INSERT INTO suppliers (name, contact) VALUES 
('FreshFoods Co.', '9988776655'),
('Healthy Bites', '8877665544');

INSERT INTO food_items (name, price, stock, supplier_cost, supplier_id) VALUES
('Veg Burger', 80.00, 50, 30.00, 1),
('Paneer Pizza', 150.00, 20, 60.00, 1),
('Cold Coffee', 60.00, 40, 20.00, 2),
('Choco Cake', 100.00, 10, 45.00, 2);

INSERT INTO customers (name, address) VALUES
('Ritika Shah', 'Bandra, Mumbai'),
('Anil Kumar', 'Kormangala, Bangalore');

-- ✅ View: view_menu_items (hides supplier_cost)
CREATE OR REPLACE VIEW view_menu_items AS
SELECT item_id, name, price, stock
FROM food_items;

-- ✅ Function: get_delivery_eta(order_id)
DELIMITER //
CREATE FUNCTION get_delivery_eta(ord_id INT)
RETURNS DATETIME
DETERMINISTIC
BEGIN
    DECLARE delivery_time DATETIME;
    SELECT DATE_ADD(order_date, INTERVAL 45 MINUTE)
    INTO delivery_time
    FROM food_orders
    WHERE order_id = ord_id;

    RETURN delivery_time;
END;
//
DELIMITER ;

-- ✅ Procedure: place_food_order(customer_id, item_id, quantity)
DELIMITER //
CREATE PROCEDURE place_food_order(
    IN cust_id INT,
    IN food_id INT,
    IN qty INT
)
BEGIN
    DECLARE item_price DECIMAL(10,2);
    DECLARE total DECIMAL(10,2);
    DECLARE stock_now INT;
    DECLARE new_order_id INT;
    
    -- Get current stock and price
    SELECT price, stock INTO item_price, stock_now FROM food_items WHERE item_id = food_id;

    IF stock_now < qty THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Not enough stock.';
    END IF;

    SET total = item_price * qty;

    -- Create order
    INSERT INTO food_orders (customer_id, order_date, total_amount)
    VALUES (cust_id, '2025-08-06 12:00:00', total);

    SET new_order_id = LAST_INSERT_ID();

    -- Insert into order_items
    INSERT INTO order_items (item_id, order_id, quantity, price)
    VALUES (food_id, new_order_id, qty, item_price);

    -- Deduct stock
    UPDATE food_items SET stock = stock - qty WHERE item_id = food_id;

    -- Add to delivery queue (trigger will also do this)
    -- INSERT handled by trigger below
END;
//
DELIMITER ;

-- ✅ Trigger: after_order_placed inserts into delivery_queue
DELIMITER //
CREATE TRIGGER after_order_placed
AFTER INSERT ON food_orders
FOR EACH ROW
BEGIN
    DECLARE estimated DATETIME;
    SET estimated = DATE_ADD(NEW.order_date, INTERVAL 45 MINUTE);

    INSERT INTO delivery_queue (order_id, status, eta)
    VALUES (NEW.order_id, 'Queued', estimated);
END;
//
DELIMITER ;

-- ✅ Admins can access raw tables; customers use view_menu_items

-- ✅ Test Run:
-- CALL place_food_order(1, 1, 2);

-- ✅ View usage:
-- SELECT * FROM view_menu_items;

-- ✅ Check ETA:
-- SELECT get_delivery_eta(1);

-- ✅ Check delivery queue:
-- SELECT * FROM delivery_queue;
