--  16. Loan Application Processing System 
-- Requirements: 
--  Tables: applicants, loans, documents, disbursements 
--  Insert applications with required fields and constraints. 
--  Update status through stages. 
--  Delete unverified applications. 
--  Add CHECK (amount <= 1,000,000). 
--  Use SAVEPOINT before disbursement step. 
--  Transaction to verify docs, approve, disburse – rollback if any fail.

-- Create Database
CREATE DATABASE IF NOT EXISTS LoanProcessingDB;
USE LoanProcessingDB;

-- Applicants Table
CREATE TABLE applicants (
    applicant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) UNIQUE,
    application_date DATE DEFAULT (CURDATE()),
    status ENUM('Pending', 'Verified', 'Approved', 'Rejected') DEFAULT 'Pending'
);

-- Loans Table
CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT,
    amount DECIMAL(15,2) CHECK (amount <= 1000000),
    loan_date DATE DEFAULT (CURDATE()),
    status ENUM('Processing', 'Disbursed', 'Closed') DEFAULT 'Processing',
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id)
);

-- Documents Table
CREATE TABLE documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,
    applicant_id INT,
    document_name VARCHAR(100),
    verified BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id)
);

-- Disbursements Table
CREATE TABLE disbursements (
    disbursement_id INT AUTO_INCREMENT PRIMARY KEY,
    loan_id INT,
    disbursement_date DATE DEFAULT (CURDATE()),
    amount DECIMAL(15,2),
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);

-- Sample Inserts
INSERT INTO applicants (name, email, phone) VALUES
('Vikram Patel', 'vikram.patel@example.com', '9876543210'),
('Sneha Joshi', 'sneha.joshi@example.com', '9123456789');

INSERT INTO loans (applicant_id, amount) VALUES
(1, 500000.00),
(2, 750000.00);

INSERT INTO documents (applicant_id, document_name, verified) VALUES
(1, 'ID Proof', TRUE),
(1, 'Income Proof', TRUE),
(2, 'ID Proof', FALSE);

-- Use SAVEPOINT before disbursement step in transaction
START TRANSACTION;

-- Step 1: Verify documents for applicant 1
UPDATE documents SET verified = TRUE WHERE applicant_id = 1;

-- Step 2: Update applicant status to Verified
UPDATE applicants SET status = 'Verified' WHERE applicant_id = 1;

-- Step 3: Approve loan
UPDATE loans SET status = 'Approved' WHERE applicant_id = 1;

-- Savepoint before disbursement
SAVEPOINT before_disbursement;

-- Step 4: Disburse amount
INSERT INTO disbursements (loan_id, amount) VALUES (1, 500000.00);

-- Simulate error condition (uncomment to test rollback)
-- ROLLBACK TO before_disbursement;

-- Step 5: Update loan status to Disbursed
UPDATE loans SET status = 'Disbursed' WHERE loan_id = 1;

COMMIT;

-- Delete unverified applicants (e.g., with status 'Pending' older than 1 year)
DELETE FROM applicants WHERE status = 'Pending' AND application_date < (CURDATE() - INTERVAL 1 YEAR);
