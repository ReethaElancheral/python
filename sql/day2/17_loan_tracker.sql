-- Project 17: Loan Application Tracker
CREATE TABLE loans (
    loan_id INT PRIMARY KEY,
    applicant_name VARCHAR(100),
    amount DECIMAL(12,2),
    loan_type VARCHAR(50),
    status VARCHAR(20),
    approval_date DATE
);

INSERT INTO loans (loan_id, applicant_name, amount, loan_type, status, approval_date) VALUES
(1, 'Ramesh Kumar', 150000, 'Home', 'Approved', '2025-06-15'),
(2, 'Sunita Patel', 50000, 'Education', 'Pending', NULL),
(3, 'Amit Shah', 100000, 'Home', 'Rejected', '2025-06-20'),
(4, 'Priya Singh', 120000, 'Business', 'Approved', '2025-06-25'),
(5, 'Rahul Verma', 75000, 'Education', 'Approved', '2025-06-18');

SELECT applicant_name, amount, status FROM loans WHERE amount BETWEEN 50000 AND 200000 AND loan_type IN ('Home', 'Education');
SELECT * FROM loans WHERE approval_date IS NULL;
SELECT * FROM loans ORDER BY amount DESC;