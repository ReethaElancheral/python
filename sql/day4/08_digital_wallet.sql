-- Project 8: Digital Wallet Transactions Monitor

-- Create database
CREATE DATABASE IF NOT EXISTS digital_wallet_db;
USE digital_wallet_db;

-- Create tables
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    account_type VARCHAR(50),
    balance DECIMAL(12,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE transactions (
    txn_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(10,2),
    txn_type VARCHAR(50),
    txn_date DATETIME,
    status VARCHAR(50),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Insert sample data

INSERT INTO users (name, city) VALUES
('Alice', 'New York'),
('Bob', 'Los Angeles'),
('Charlie', 'Chicago'),
('Diana', 'Houston'),
('Evan', 'Phoenix');

INSERT INTO accounts (user_id, account_type, balance) VALUES
(1, 'WalletA', 5000),
(2, 'WalletA', 3000),
(3, 'WalletB', 7000),
(4, 'WalletB', 2000),
(5, 'WalletA', 1000);

INSERT INTO transactions (account_id, amount, txn_type, txn_date, status) VALUES
(1, 100, 'Credit', '2025-07-20 10:00:00', 'Completed'),
(1, 50, 'Debit', '2025-07-21 11:30:00', 'Completed'),
(2, 200, 'Recharge', '2025-07-22 14:00:00', 'Pending'),
(3, 150, 'Credit', '2025-07-23 09:45:00', 'Completed'),
(4, 500, 'Debit', '2025-07-24 12:00:00', 'Failed'),
(5, 250, 'Refund', '2025-07-25 16:20:00', 'Completed');

-- Queries

-- 1. Subquery to calculate average transaction value per user
SELECT u.user_id, u.name,
  (SELECT AVG(t.amount)
   FROM transactions t
   JOIN accounts a ON t.account_id = a.account_id
   WHERE a.user_id = u.user_id) AS avg_transaction_value
FROM users u;

-- 2. JOIN + GROUP BY to show transaction totals by city
SELECT u.city, COUNT(t.txn_id) AS total_transactions, SUM(t.amount) AS total_amount
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
JOIN users u ON a.user_id = u.user_id
GROUP BY u.city;

-- 3. CASE for transaction types
SELECT txn_id, txn_type,
CASE
  WHEN txn_type LIKE '%Credit%' THEN 'Credit'
  WHEN txn_type LIKE '%Debit%' THEN 'Debit'
  WHEN txn_type LIKE '%Refund%' THEN 'Refund'
  ELSE 'Other'
END AS txn_category
FROM transactions;

-- 4. UNION to merge two different wallet systems (simulate with two selects)
SELECT user_id, account_type FROM accounts WHERE account_type = 'WalletA'
UNION
SELECT user_id, account_type FROM accounts WHERE account_type = 'WalletB';

-- 5. INTERSECT to find users active on both platforms
-- MySQL does not support INTERSECT directly, so emulate:
SELECT user_id FROM accounts WHERE account_type = 'WalletA'
AND user_id IN (SELECT user_id FROM accounts WHERE account_type = 'WalletB');

-- 6. Date filtering for transactions made this week or month
-- Transactions in current week
SELECT * FROM transactions
WHERE YEARWEEK(txn_date, 1) = YEARWEEK(CURDATE(), 1);

-- Transactions in current month
SELECT * FROM transactions
WHERE YEAR(txn_date) = YEAR(CURDATE())
AND MONTH(txn_date) = MONTH(CURDATE());

