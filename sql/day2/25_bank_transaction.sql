-- Project 5: Bank Transaction Tracker

CREATE DATABASE IF NOT EXISTS bank_db;
USE bank_db;

-- Tables

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    customer_id INT,
    account_type VARCHAR(50),
    balance DECIMAL(15,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    account_id INT,
    transaction_type ENUM('deposit', 'withdrawal'),
    amount DECIMAL(15,2),
    transaction_date DATE,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);



INSERT INTO customers (customer_id, name, city) VALUES
(1, 'Alice', 'New York'),
(2, 'Bob', 'Chicago'),
(3, 'Charlie', 'New York'),
(4, 'Diana', 'San Francisco');

INSERT INTO accounts (account_id, customer_id, account_type, balance) VALUES
(1, 1, 'Savings', 15000.00),
(2, 1, 'Checking', 5000.00),
(3, 2, 'Savings', 8000.00),
(4, 3, 'Checking', 12000.00);

INSERT INTO transactions (transaction_id, account_id, transaction_type, amount, transaction_date) VALUES
(1, 1, 'deposit', 10000.00, '2025-07-01'),
(2, 1, 'withdrawal', 2000.00, '2025-07-05'),
(3, 2, 'withdrawal', 6000.00, '2025-07-06'),
(4, 3, 'deposit', 7000.00, '2025-07-07'),
(5, 4, 'withdrawal', 12000.00, '2025-07-08'),
(6, 1, 'deposit', 5000.00, '2025-07-10');

-- Queries:

-- 1. Total deposits and withdrawals per account (SUM)
SELECT 
    a.account_id,
    SUM(CASE WHEN t.transaction_type = 'deposit' THEN t.amount ELSE 0 END) AS total_deposits,
    SUM(CASE WHEN t.transaction_type = 'withdrawal' THEN t.amount ELSE 0 END) AS total_withdrawals
FROM accounts a
LEFT JOIN transactions t ON a.account_id = t.account_id
GROUP BY a.account_id;

-- 2. Highest and lowest transaction amounts (MAX, MIN)
SELECT 
    a.account_id,
    MAX(t.amount) AS highest_transaction,
    MIN(t.amount) AS lowest_transaction
FROM accounts a
LEFT JOIN transactions t ON a.account_id = t.account_id
GROUP BY a.account_id;

-- 3. Filter accounts with total withdrawals > 10,000 (HAVING)
SELECT 
    a.account_id,
    SUM(CASE WHEN t.transaction_type = 'withdrawal' THEN t.amount ELSE 0 END) AS total_withdrawals
FROM accounts a
LEFT JOIN transactions t ON a.account_id = t.account_id
GROUP BY a.account_id
HAVING total_withdrawals > 10000;

-- 4. INNER JOIN customers and accounts
SELECT 
    c.name AS customer_name,
    a.account_id,
    a.account_type,
    a.balance
FROM customers c
INNER JOIN accounts a ON c.customer_id = a.customer_id;

-- 5. LEFT JOIN to show accounts with no transactions
SELECT 
    a.account_id,
    t.transaction_id
FROM accounts a
LEFT JOIN transactions t ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL;

-- 6. SELF JOIN to find customers from same city
SELECT 
    c1.name AS customer1,
    c2.name AS customer2,
    c1.city
FROM customers c1
INNER JOIN customers c2 ON c1.city = c2.city AND c1.customer_id <> c2.customer_id
ORDER BY c1.city, c1.name;
