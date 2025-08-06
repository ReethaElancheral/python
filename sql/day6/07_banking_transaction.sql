--  7. Banking and Transaction System 
-- Requirements: 
--  Tables: customers, accounts, transactions, branches 
--  Normalize to separate account and transaction details. 
--  Index account_no, transaction_date, branch_id. 
--  Use EXPLAIN to identify slow account balance checks. 
--  Use subqueries for calculating running balance. 
--  Create a denormalized statement view. 
--  Use LIMIT to display latest 10 transactions.

CREATE DATABASE IF NOT EXISTS BankSystem;
USE BankSystem;

-- Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    address TEXT,
    phone VARCHAR(15)
);

-- Branches Table
CREATE TABLE branches (
    branch_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_name VARCHAR(100),
    location VARCHAR(100)
);

-- Accounts Table
CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    branch_id INT,
    account_no VARCHAR(20) UNIQUE,
    balance DECIMAL(12,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

-- Transactions Table
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    transaction_date DATE,
    amount DECIMAL(10,2),
    type ENUM('credit', 'debit'),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- Indexing
CREATE INDEX idx_account_no ON accounts(account_no);
CREATE INDEX idx_transaction_date ON transactions(transaction_date);
CREATE INDEX idx_branch_id ON accounts(branch_id);

-- EXPLAIN to detect slow balance query
EXPLAIN SELECT balance FROM accounts WHERE account_no = 'AC0001';

-- Subquery for running balance
SELECT a.account_id, a.account_no,
       (SELECT SUM(CASE WHEN t.type = 'credit' THEN t.amount ELSE -t.amount END)
        FROM transactions t WHERE t.account_id = a.account_id) AS running_balance
FROM accounts a;

-- Denormalized View for Statement
CREATE VIEW account_statement AS
SELECT c.name, a.account_no, t.transaction_date, t.amount, t.type
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
JOIN customers c ON a.customer_id = c.customer_id;

-- LIMIT to display latest 10 transactions
SELECT * FROM transactions ORDER BY transaction_date DESC LIMIT 10;
