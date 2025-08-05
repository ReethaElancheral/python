-- 14. CRM System for Sales 
-- Requirements: 
--  Tables: leads, customers, sales, followups 
--  Insert lead records with UNIQUE phone/email. 
--  Update lead status after sales conversion. 
--  Delete old leads after 1 year. 
--  Add CHECK (followup_count <= 5).           
--    Drop and reapply FOREIGN KEY on sales. 
--  Use transaction to convert lead to customer + log sale.  

-- Create Database
CREATE DATABASE IF NOT EXISTS CRMDB;
USE CRMDB;

-- Leads Table
CREATE TABLE leads (
    lead_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE,
    email VARCHAR(100) UNIQUE,
    status ENUM('New', 'Contacted', 'Converted', 'Lost') DEFAULT 'New',
    created_at DATE DEFAULT (CURDATE())
);

-- Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE,
    email VARCHAR(100) UNIQUE,
    joined_date DATE DEFAULT (CURDATE())
);

-- Sales Table
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    sale_date DATE DEFAULT (CURDATE()),
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Followups Table
CREATE TABLE followups (
    followup_id INT AUTO_INCREMENT PRIMARY KEY,
    lead_id INT,
    followup_date DATE DEFAULT (CURDATE()),
    notes TEXT,
    followup_count INT DEFAULT 0 CHECK (followup_count <= 5),
    FOREIGN KEY (lead_id) REFERENCES leads(lead_id)
);

-- Sample Inserts - Leads
INSERT INTO leads (name, phone, email) VALUES
('Rohan Singh', '9876543210', 'rohan.singh@example.com'),
('Meera Sharma', '9123456789', 'meera.sharma@example.com');

-- Update lead status after sales conversion
UPDATE leads SET status = 'Converted' WHERE lead_id = 1;

-- Delete leads older than 1 year
DELETE FROM leads WHERE created_at < (CURDATE() - INTERVAL 1 YEAR);

-- Drop and reapply FOREIGN KEY on sales.customer_id
ALTER TABLE sales DROP FOREIGN KEY sales_ibfk_1;

ALTER TABLE sales
ADD CONSTRAINT fk_sales_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- Transaction: Convert lead to customer + log sale
START TRANSACTION;

-- Step 1: Insert into customers from leads (simulate)
INSERT INTO customers (name, phone, email)
SELECT name, phone, email FROM leads WHERE lead_id = 2;

-- Get last inserted customer ID
SET @cust_id = LAST_INSERT_ID();

-- Step 2: Log sale for new customer
INSERT INTO sales (customer_id, amount) VALUES (@cust_id, 15000.00);

-- Step 3: Update lead status
UPDATE leads SET status = 'Converted' WHERE lead_id = 2;

-- Commit all if success
COMMIT;

-- Rollback in case of errors (manually if needed)
-- ROLLBACK;

-- View customers and sales
SELECT * FROM customers;
SELECT * FROM sales;
