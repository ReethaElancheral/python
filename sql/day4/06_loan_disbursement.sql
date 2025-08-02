-- Project 6: Loan Disbursement and Repayment Tracker

CREATE DATABASE IF NOT EXISTS loan_db;
USE loan_db;

-- Tables
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE loan_types (
    loan_type_id INT PRIMARY KEY,
    type_name VARCHAR(50)
);

CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    customer_id INT,
    loan_type_id INT,
    amount DECIMAL(12,2),
    disbursement_date DATE,
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (loan_type_id) REFERENCES loan_types(loan_type_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    loan_id INT,
    payment_date DATE,
    amount_paid DECIMAL(12,2),
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);

-- Insert data
INSERT INTO customers VALUES
(1, 'Ravi Kumar', 'Delhi'),
(2, 'Anita Singh', 'Mumbai'),
(3, 'Sunil Patel', 'Chennai'),
(4, 'Priya Sharma', 'Bangalore'),
(5, 'Amit Joshi', 'Hyderabad');

INSERT INTO loan_types VALUES
(1, 'Home'),
(2, 'Education'),
(3, 'Personal');

INSERT INTO loans VALUES
(1, 1, 1, 500000, '2024-01-15', 'On Track'),
(2, 2, 2, 200000, '2023-06-20', 'Delayed'),
(3, 3, 3, 150000, '2024-02-10', 'Closed'),
(4, 4, 1, 750000, '2023-09-01', 'On Track'),
(5, 5, 3, 300000, '2024-03-05', 'On Track');

INSERT INTO payments VALUES
(1, 1, '2024-02-15', 50000),
(2, 1, '2024-03-15', 60000),
(3, 2, '2023-07-25', 40000),
(4, 2, '2023-08-30', 30000),
(5, 3, '2024-03-10', 150000),
(6, 4, '2023-10-10', 100000),
(7, 5, '2024-04-10', 50000);

-- Subquery in SELECT to calculate outstanding loan balance
SELECT l.loan_id, c.name, l.amount,
       l.amount - IFNULL((
           SELECT SUM(amount_paid) FROM payments p WHERE p.loan_id = l.loan_id
       ), 0) AS outstanding_balance
FROM loans l
JOIN customers c ON l.customer_id = c.customer_id;

-- JOIN + GROUP BY to calculate total repayments per loan type
SELECT lt.type_name, SUM(p.amount_paid) AS total_repayments
FROM loan_types lt
JOIN loans l ON lt.loan_type_id = l.loan_type_id
JOIN payments p ON l.loan_id = p.loan_id
GROUP BY lt.type_name;

-- CASE to categorize loans as "Closed", "On Track", "Delayed"
SELECT loan_id, status,
    CASE
        WHEN status = 'Closed' THEN 'Closed'
        WHEN status = 'On Track' THEN 'On Track'
        WHEN status = 'Delayed' THEN 'Delayed'
        ELSE 'Unknown'
    END AS loan_category
FROM loans;

-- UNION ALL to combine active and closed loans
SELECT loan_id, customer_id, amount, 'Active' AS loan_status
FROM loans WHERE status != 'Closed'
UNION ALL
SELECT loan_id, customer_id, amount, 'Closed' AS loan_status
FROM loans WHERE status = 'Closed';

-- Correlated subquery to find customers whose payments are above their own loan average
SELECT c.customer_id, c.name, l.loan_id, loan_avg.avg_payment, total_paid.total_payment
FROM customers c
JOIN loans l ON c.customer_id = l.customer_id
JOIN (
    SELECT loan_id, AVG(amount_paid) AS avg_payment
    FROM payments
    GROUP BY loan_id
) AS loan_avg ON loan_avg.loan_id = l.loan_id
JOIN (
    SELECT loan_id, SUM(amount_paid) AS total_payment
    FROM payments
    GROUP BY loan_id
) AS total_paid ON total_paid.loan_id = l.loan_id
WHERE total_paid.total_payment > loan_avg.avg_payment;

-- Use DATEDIFF to calculate delay in payments
SELECT l.loan_id, p.payment_id, p.payment_date, DATEDIFF(CURDATE(), p.payment_date) AS days_delayed
FROM loans l
JOIN payments p ON l.loan_id = p.loan_id
WHERE DATEDIFF(CURDATE(), p.payment_date) > 0;
