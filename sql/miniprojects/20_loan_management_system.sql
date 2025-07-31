-- Project 20: Loan Management System

CREATE DATABASE IF NOT EXISTS loan_db;
USE loan_db;

CREATE TABLE borrowers (
    borrower_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE loan_types (
    loan_type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50),
    interest_rate DECIMAL(5,2)
);

CREATE TABLE loans (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    borrower_id INT,
    loan_type_id INT,
    amount DECIMAL(10,2),
    disbursement_date DATE,
    due_date DATE,
    FOREIGN KEY (borrower_id) REFERENCES borrowers(borrower_id),
    FOREIGN KEY (loan_type_id) REFERENCES loan_types(loan_type_id)
);

CREATE TABLE repayments (
    repayment_id INT PRIMARY KEY AUTO_INCREMENT,
    loan_id INT,
    amount_paid DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);

INSERT INTO loan_types (type_name, interest_rate) VALUES
('Personal Loan', 12.5),
('Home Loan', 8.0),
('Car Loan', 10.0);

INSERT INTO borrowers (name, email, phone) VALUES
('Anjali Verma', 'anjali@example.com', '9876543210'),
('Rahul Singh', 'rahul@example.com', '8765432109'),
('Priya Sharma', 'priya@example.com', '7654321098');

INSERT INTO loans (borrower_id, loan_type_id, amount, disbursement_date, due_date) VALUES
(1, 1, 50000.00, '2024-01-15', '2025-01-15'),
(2, 2, 200000.00, '2024-03-10', '2026-03-10'),
(3, 3, 150000.00, '2024-05-20', '2025-05-20');

INSERT INTO repayments (loan_id, amount_paid, payment_date) VALUES
(1, 10000.00, '2024-02-15'),
(1, 15000.00, '2024-04-15'),
(2, 50000.00, '2024-05-10'),
(2, 30000.00, '2024-07-10'),
(3, 25000.00, '2024-06-15');

-- Total amount repaid per borrower
SELECT 
    b.name AS borrower_name,
    SUM(r.amount_paid) AS total_repaid
FROM borrowers b
JOIN loans l ON b.borrower_id = l.borrower_id
JOIN repayments r ON l.loan_id = r.loan_id
GROUP BY b.borrower_id;

-- Upcoming repayment schedule
SELECT 
    b.name AS borrower_name,
    l.loan_id,
    l.due_date,
    DATEDIFF(l.due_date, CURDATE()) AS days_left
FROM loans l
JOIN borrowers b ON l.borrower_id = b.borrower_id
WHERE l.due_date > CURDATE()
ORDER BY l.due_date ASC;