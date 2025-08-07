--  7. Bank Loan Analytics Warehouse 
-- Requirements: 
--  OLTP: loans, payments, customers, branches. 
--  Snowflake Schema for normalized customer and loan details. 
--  ETL to extract repayment history, transform statuses. 
--  Reports: default rate by branch, loan product performance. 
--  OLAP reports to support risk assessment and audit. 

-- Create Database
CREATE DATABASE IF NOT EXISTS BankLoanWarehouse;
USE BankLoanWarehouse;

-- Dimension Tables

-- Customer dimension
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    region VARCHAR(50)
);

-- Branch dimension
CREATE TABLE dim_branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(100),
    city VARCHAR(50)
);

-- Loan Product dimension
CREATE TABLE dim_loan_product (
    loan_product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    interest_rate DECIMAL(5,2)
);

-- Time dimension
CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    payment_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT
);

-- Fact Table
CREATE TABLE fact_loans (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    branch_id INT,
    loan_product_id INT,
    time_id INT,
    loan_amount DECIMAL(12,2),
    repayment_amount DECIMAL(12,2),
    repayment_status VARCHAR(20),
    overdue_days INT,
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (branch_id) REFERENCES dim_branch(branch_id),
    FOREIGN KEY (loan_product_id) REFERENCES dim_loan_product(loan_product_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);

-- Sample Dimension Data
INSERT INTO dim_customer VALUES
(1,'Alice','Doha','West'),
(2,'Bob','Al Wakrah','South'),
(3,'Charlie','Doha','West');

INSERT INTO dim_branch VALUES
(1,'Main Branch','Doha'),
(2,'City Branch','Al Wakrah');

INSERT INTO dim_loan_product VALUES
(1,'Home Loan',6.5),
(2,'Car Loan',7.0),
(3,'Personal Loan',9.0);

INSERT INTO dim_time VALUES
(1,'2025-08-01',1,8,3,2025),
(2,'2025-08-02',2,8,3,2025);

-- Sample Fact Data (after ETL)
INSERT INTO fact_loans (customer_id, branch_id, loan_product_id, time_id, loan_amount, repayment_amount, repayment_status, overdue_days)
VALUES
(1,1,1,1,500000,5000,'On Time',0),
(2,2,2,2,200000,2000,'Late',5),
(3,1,3,1,100000,1500,'Default',30);

-- OLAP Queries

-- Default Rate by Branch
SELECT b.branch_name,
       COUNT(CASE WHEN f.repayment_status='Default' THEN 1 END) AS defaults,
       COUNT(f.loan_id) AS total_loans,
       ROUND(COUNT(CASE WHEN f.repayment_status='Default' THEN 1 END)/COUNT(f.loan_id)*100,2) AS default_rate_percentage
FROM fact_loans f
JOIN dim_branch b ON f.branch_id = b.branch_id
GROUP BY b.branch_name;

-- Loan Product Performance
SELECT lp.product_name,
       COUNT(f.loan_id) AS total_loans,
       SUM(f.loan_amount) AS total_disbursed,
       AVG(f.repayment_amount) AS avg_repayment,
       COUNT(CASE WHEN f.repayment_status='Default' THEN 1 END) AS defaults
FROM fact_loans f
JOIN dim_loan_product lp ON f.loan_product_id = lp.loan_product_id
GROUP BY lp.product_name
ORDER BY total_loans DESC;

-- Overdue Analysis (customers with overdue loans)
SELECT c.customer_name, b.branch_name, f.loan_amount, f.repayment_amount, f.overdue_days
FROM fact_loans f
JOIN dim_customer c ON f.customer_id = c.customer_id
JOIN dim_branch b ON f.branch_id = b.branch_id
WHERE f.overdue_days > 0
ORDER BY f.overdue_days DESC;

-- Monthly Repayment Summary
SELECT t.month, t.year, SUM(f.repayment_amount) AS total_repayments
FROM fact_loans f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.year, t.month
ORDER BY t.year, t.month;
