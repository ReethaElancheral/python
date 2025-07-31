-- Project 18: Banking Transaction System

CREATE DATABASE IF NOT EXISTS bank_db;
USE bank_db;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE branches (
    branch_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    branch_id INT,
    balance DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    type ENUM('credit', 'debit'),
    amount DECIMAL(10,2),
    transaction_date DATE,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

INSERT INTO customers (name, email) VALUES 
('Amit Kumar', 'amit@example.com'),
('Sneha Reddy', 'sneha@example.com');

INSERT INTO branches (branch_name, location) VALUES 
('Main Branch', 'Mumbai'),
('City Branch', 'Delhi');

INSERT INTO accounts (customer_id, branch_id, balance) VALUES 
(1, 1, 10000.00),
(2, 2, 15000.00);

INSERT INTO transactions (account_id, type, amount, transaction_date) VALUES 
(1, 'credit', 5000.00, '2024-01-01'),
(1, 'debit', 2000.00, '2024-02-01'),
(2, 'credit', 7000.00, '2024-01-15');

-- Transaction history
SELECT c.name, t.type, t.amount, t.transaction_date 
FROM transactions t
JOIN accounts a ON t.account_id = a.account_id
JOIN customers c ON a.customer_id = c.customer_id;

-- Account balances
SELECT c.name, a.balance 
FROM accounts a
JOIN customers c ON a.customer_id = c.customer_id;