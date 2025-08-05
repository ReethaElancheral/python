
-- Project 17: Warehouse & Supply Chain Inventory

CREATE DATABASE IF NOT EXISTS WarehouseDB;
USE WarehouseDB;

CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact_info VARCHAR(255)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    total_stock INT DEFAULT 0
);

CREATE TABLE batches (
    batch_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    manufactured_date DATE NOT NULL,
    expiry_date DATE NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    CHECK (expiry_date > manufactured_date)
);

CREATE TABLE deliveries (
    delivery_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_id INT,
    product_id INT,
    quantity INT NOT NULL,
    delivery_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert with supplier validation
INSERT INTO suppliers (name, contact_info) VALUES 
('FreshSupplies Ltd', 'contact@freshsupplies.com');

INSERT INTO products (name, total_stock) VALUES 
('Wheat Flour', 0);

-- Transaction: register delivery and update stock
START TRANSACTION;
INSERT INTO deliveries (supplier_id, product_id, quantity) VALUES (1, 1, 100);
UPDATE products SET total_stock = total_stock + 100 WHERE product_id = 1;
COMMIT;

-- Delete expired batches
DELETE FROM batches WHERE expiry_date < CURDATE();

-- Drop and recreate FOREIGN KEY on deliveries
ALTER TABLE deliveries DROP FOREIGN KEY deliveries_ibfk_1;
ALTER TABLE deliveries ADD CONSTRAINT deliveries_fk_supplier FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id);
