--  Tables: loans, clients, officers, repayments 
--  Total loans issued per officer 
--  Clients with repayment > ₹1,00,000 
--  Officers approving more than 10 loans 
--  INNER JOIN: clients ↔ loans ↔ officers 
--  FULL OUTER JOIN: loans ↔ repayments 
--  SELF JOIN: clients from same city 

CREATE DATABASE IF NOT EXISTS LoanDB;
USE LoanDB;

-- Create tables
CREATE TABLE officers (
    officer_id INT PRIMARY KEY,
    officer_name VARCHAR(100)
);

CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    client_id INT,
    officer_id INT,
    amount DECIMAL(15,2),
    loan_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (officer_id) REFERENCES officers(officer_id)
);

CREATE TABLE repayments (
    repayment_id INT PRIMARY KEY,
    loan_id INT,
    amount DECIMAL(15,2),
    repayment_date DATE,
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);

-- Insert sample data into officers
INSERT INTO officers VALUES
(1, 'Officer A'),
(2, 'Officer B'),
(3, 'Officer C');

-- Insert sample data into clients
INSERT INTO clients VALUES
(101, 'Client X', 'Mumbai'),
(102, 'Client Y', 'Delhi'),
(103, 'Client Z', 'Mumbai'),
(104, 'Client W', 'Bangalore');

-- Insert sample data into loans
INSERT INTO loans VALUES
(201, 101, 1, 500000, '2025-01-10'),
(202, 102, 1, 750000, '2025-02-15'),
(203, 103, 2, 1200000, '2025-03-05'),
(204, 104, 3, 300000, '2025-04-10'),
(205, 101, 1, 200000, '2025-05-01'),
(206, 103, 2, 800000, '2025-06-12'),
(207, 102, 1, 650000, '2025-07-01'),
(208, 104, 3, 450000, '2025-07-15'),
(209, 101, 1, 550000, '2025-07-20'),
(210, 103, 2, 300000, '2025-07-22'),
(211, 102, 1, 900000, '2025-07-25'),
(212, 104, 3, 700000, '2025-07-30');

-- Insert sample data into repayments
INSERT INTO repayments VALUES
(301, 201, 120000, '2025-02-10'),
(302, 201, 100000, '2025-03-10'),
(303, 202, 750000, '2025-04-15'),
(304, 203, 500000, '2025-05-05'),
(305, 204, 300000, '2025-05-20'),
(306, 205, 200000, '2025-06-01'),
(307, 206, 300000, '2025-06-15'),
(308, 207, 650000, '2025-07-10'),
(309, 208, 450000, '2025-07-20'),
(310, 209, 550000, '2025-07-25'),
(311, 210, 300000, '2025-07-28'),
(312, 211, 900000, '2025-07-30'),
(313, 212, 700000, '2025-08-01');

SELECT o.officer_name, COUNT(l.loan_id) AS total_loans, SUM(l.amount) AS total_loan_amount
FROM officers o
JOIN loans l ON o.officer_id = l.officer_id
GROUP BY o.officer_id;

SELECT c.client_name, SUM(r.amount) AS total_repaid
FROM clients c
JOIN loans l ON c.client_id = l.client_id
JOIN repayments r ON l.loan_id = r.loan_id
GROUP BY c.client_id
HAVING total_repaid > 100000;

SELECT o.officer_name, COUNT(l.loan_id) AS loans_approved
FROM officers o
JOIN loans l ON o.officer_id = l.officer_id
GROUP BY o.officer_id
HAVING loans_approved > 10;

SELECT l.loan_id, c.client_name, o.officer_name, l.amount, l.loan_date
FROM loans l
JOIN clients c ON l.client_id = c.client_id
JOIN officers o ON l.officer_id = o.officer_id;

--  FULL OUTER JOIN loans ↔ repayments (MySQL simulation)

-- Left join loans with repayments
SELECT l.loan_id, l.amount AS loan_amount, r.amount AS repayment_amount, r.repayment_date
FROM loans l
LEFT JOIN repayments r ON l.loan_id = r.loan_id

UNION

-- Right join loans with repayments (rows in repayments without loans)
SELECT l.loan_id, l.amount AS loan_amount, r.amount AS repayment_amount, r.repayment_date
FROM loans l
RIGHT JOIN repayments r ON l.loan_id = r.loan_id
WHERE l.loan_id IS NULL;


SELECT c1.client_name AS Client1, c2.client_name AS Client2, c1.city
FROM clients c1
JOIN clients c2 ON c1.city = c2.city AND c1.client_id < c2.client_id;
