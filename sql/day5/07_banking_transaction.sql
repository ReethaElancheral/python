-- 7. Banking Transaction System 
-- Requirements: 
--  Tables: accounts, transactions, customers 
--  Insert account data with PRIMARY KEY, NOT NULL balance. 
--  Update balance after transactions. 
--  Delete closed accounts. 
--  Add a CHECK for balance >= 0. 
--  Drop a FOREIGN KEY to restructure relationships. 
--  Use transaction to transfer money (debit/credit), rollback if either fails. 
--  Demonstrate isolation by simulating concurrent transfers.

-- Create Database
CREATE DATABASE IF NOT EXISTS BankingDB;
USE BankingDB;

-- Create Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
);

-- Create Accounts Table
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    account_type ENUM('Savings', 'Current') NOT NULL,
    balance DECIMAL(15,2) NOT NULL CHECK (balance >= 0),
    status ENUM('Active', 'Closed') DEFAULT 'Active',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create Transactions Table
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    from_account INT,
    to_account INT,
    amount DECIMAL(10,2) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (from_account) REFERENCES accounts(account_id),
    FOREIGN KEY (to_account) REFERENCES accounts(account_id)
);

-- Insert Sample Customers
INSERT INTO customers (name, email, phone) VALUES
('Alice Sharma', 'alice@example.com', '9123456780'),
('Bob Verma', 'bob@example.com', '9988776655');

-- Insert Sample Accounts
INSERT INTO accounts (customer_id, account_type, balance) VALUES
(1, 'Savings', 50000.00),
(2, 'Savings', 20000.00);

-- Insert Initial Transactions
INSERT INTO transactions (from_account, to_account, amount)
VALUES (1, 2, 5000.00);

-- Update Balances After Transaction
UPDATE accounts SET balance = balance - 5000 WHERE account_id = 1;
UPDATE accounts SET balance = balance + 5000 WHERE account_id = 2;

-- Delete Closed Accounts
DELETE FROM accounts WHERE status = 'Closed';

-- Drop a FOREIGN KEY to restructure (example: remove from_account link)
ALTER TABLE transactions DROP FOREIGN KEY transactions_ibfk_1;

-- Simulate a fund transfer with transaction block
START TRANSACTION;

-- Debit from Account 1 (Alice)
UPDATE accounts
SET balance = balance - 10000
WHERE account_id = 1 AND balance >= 10000;

-- Credit to Account 2 (Bob)
UPDATE accounts
SET balance = balance + 10000
WHERE account_id = 2;

-- Record Transaction
INSERT INTO transactions (from_account, to_account, amount)
VALUES (1, 2, 10000);

-- Commit if all succeed
COMMIT;

-- If any step fails
-- ROLLBACK;

-- Simulate Isolation Test (basic):
-- While Alice transfers ₹15,000, another transaction should wait or use consistent reads
-- You can open two sessions in MySQL Workbench to test this

-- Durability Test:
-- After COMMIT, disconnect and reconnect → transaction remains persisted

-- View All Transactions
SELECT * FROM transactions;

-- View All Accounts
SELECT * FROM accounts;
