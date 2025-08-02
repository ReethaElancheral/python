-- 10. Bank Transactions and Customer Profiles
-- Requirements:
-- Tables: customers, accounts, transactions.
-- Use IS NULL to find accounts with no transactions.
-- Use INNER JOIN to combine account and customer info.
-- Use SUM() to get total deposits per customer.
-- Use CASE for risk-level classification based on balance.
-- Use subquery in FROM to compute daily balance change.
-- Use UNION ALL to combine savings and current account statements.

CREATE DATABASE IF NOT EXISTS BankDB;
USE BankDB;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    account_type ENUM('Savings', 'Current'),
    balance DECIMAL(15,2),
    opened_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    transaction_date DATE,
    amount DECIMAL(15,2),
    transaction_type ENUM('Deposit', 'Withdrawal'),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Insert Sample Data

INSERT INTO customers (name, email, phone) VALUES
('Amit Singh', 'amit@example.com', '9876543210'),
('Riya Sharma', 'riya@example.com', '9123456789'),
('Karan Patel', 'karan@example.com', '9012345678');

INSERT INTO accounts (customer_id, account_type, balance, opened_date) VALUES
(1, 'Savings', 50000.00, '2023-01-15'),
(1, 'Current', 150000.00, '2023-02-10'),
(2, 'Savings', 70000.00, '2023-03-05'),
(3, 'Savings', 20000.00, '2023-04-20');

INSERT INTO transactions (account_id, transaction_date, amount, transaction_type) VALUES
(1, '2025-07-01', 10000.00, 'Deposit'),
(1, '2025-07-05', 5000.00, 'Withdrawal'),
(2, '2025-07-02', 50000.00, 'Deposit'),
(2, '2025-07-10', 10000.00, 'Withdrawal'),
(3, '2025-07-03', 20000.00, 'Deposit');

-- Queries

-- 1. IS NULL to find accounts with no transactions
SELECT a.account_id, c.name AS customer_name
FROM accounts a
JOIN customers c ON a.customer_id = c.customer_id
LEFT JOIN transactions t ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;

-- 2. INNER JOIN to combine account and customer info
SELECT c.name, a.account_id, a.account_type, a.balance
FROM customers c
INNER JOIN accounts a ON c.customer_id = a.customer_id;

-- 3. SUM() to get total deposits per customer
SELECT c.name, SUM(t.amount) AS total_deposits
FROM customers c
JOIN accounts a ON c.customer_id = a.customer_id
JOIN transactions t ON a.account_id = t.account_id
WHERE t.transaction_type = 'Deposit'
GROUP BY c.customer_id;

-- 4. CASE for risk-level classification based on balance
SELECT c.name, a.account_id, a.balance,
       CASE
           WHEN a.balance >= 100000 THEN 'Low Risk'
           WHEN a.balance BETWEEN 50000 AND 99999 THEN 'Medium Risk'
           ELSE 'High Risk'
       END AS risk_level
FROM accounts a
JOIN customers c ON a.customer_id = c.customer_id;

-- 5. Subquery in FROM to compute daily balance change
SELECT daily_changes.account_id, daily_changes.transaction_date, SUM(daily_changes.amount_change) AS daily_balance_change
FROM (
    SELECT account_id, transaction_date,
           CASE 
               WHEN transaction_type = 'Deposit' THEN amount
               ELSE -amount
           END AS amount_change
    FROM transactions
) AS daily_changes
GROUP BY daily_changes.account_id, daily_changes.transaction_date;

-- 6. UNION ALL to combine savings and current account statements
SELECT a.account_id, c.name AS customer_name, 'Savings' AS account_type, t.transaction_date, t.amount, t.transaction_type
FROM accounts a
JOIN customers c ON a.customer_id = c.customer_id
JOIN transactions t ON a.account_id = t.account_id
WHERE a.account_type = 'Savings'

UNION ALL

SELECT a.account_id, c.name, 'Current', t.transaction_date, t.amount, t.transaction_type
FROM accounts a
JOIN customers c ON a.customer_id = c.customer_id
JOIN transactions t ON a.account_id = t.account_id
WHERE a.account_type = 'Current'
ORDER BY transaction_date;
