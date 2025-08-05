--  2. Employee Payroll System 
-- Requirements: 
--  Tables: employees, salaries, departments 
--  INSERT employees with UNIQUE email and mandatory department (NOT 
-- NULL). 
--  UPDATE salary records for promotions. 
--  DELETE employees who have resigned. 
--  PRIMARY KEY on employee_id, FOREIGN KEY to departments. 
--  Add CHECK (salary > 10000) to salaries. 
--  Modify a constraint on email length, then drop it. 
--  Use a transaction to handle bulk bonus insertion: SAVEPOINT → ROLLBACK 
-- on failure.


CREATE DATABASE IF NOT EXISTS PayrollDB;
USE PayrollDB;


CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);


CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    department_id INT NOT NULL,
    status ENUM('Active', 'Resigned') DEFAULT 'Active',
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);


CREATE TABLE salaries (
    salary_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    salary DECIMAL(10,2) NOT NULL CHECK (salary > 10000),
    effective_date DATE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
);


INSERT INTO departments (department_name) VALUES
('HR'), ('Finance'), ('Engineering'), ('Marketing');

-- Insert employees with UNIQUE email and mandatory department_id
INSERT INTO employees (employee_name, email, department_id) VALUES
('Alice Johnson', 'alice.johnson@example.com', 3),
('Bob Williams', 'bob.williams@example.com', 2),
('Carol Davis', 'carol.davis@example.com', 1);

-- salary records
INSERT INTO salaries (employee_id, salary, effective_date) VALUES
(1, 50000.00, '2024-01-01'),
(2, 45000.00, '2024-01-01'),
(3, 48000.00, '2024-01-01');

-- Update salary records for promotions 
UPDATE salaries
SET salary = salary * 1.10, effective_date = '2025-01-01'
WHERE employee_id = 1;

-- Delete employees who have resigned

UPDATE employees SET status = 'Resigned' WHERE employee_id = 2;

-- Delete resigned employees and cascade delete their salaries
DELETE FROM employees WHERE status = 'Resigned';

-- Modify a constraint on email length, then drop it
-- MySQL does not support direct CHECK modification easily, so simulate:
-- Let's assume there was a CHECK constraint on email length (this is an example)

-- Step 1: Add a CHECK constraint on email length (simulate with generated column)
ALTER TABLE employees
ADD COLUMN email_length INT GENERATED ALWAYS AS (CHAR_LENGTH(email)) STORED;

ALTER TABLE employees
ADD CONSTRAINT chk_email_length CHECK (email_length <= 255);

-- Step 2: Drop the CHECK constraint
ALTER TABLE employees
DROP CHECK chk_email_length;

-- Drop the generated column too
ALTER TABLE employees DROP COLUMN email_length;

-- Transaction to handle bulk bonus insertion: SAVEPOINT → ROLLBACK on failure
-- Assuming a bonuses table for this example

CREATE TABLE bonuses (
    bonus_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    bonus_amount DECIMAL(10,2) NOT NULL CHECK (bonus_amount > 0),
    bonus_date DATE NOT NULL,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

START TRANSACTION;

SAVEPOINT before_bonus_insert;

-- Insert multiple bonuses
INSERT INTO bonuses (employee_id, bonus_amount, bonus_date) VALUES
(1, 2000.00, '2025-07-01'),
(3, 1500.00, '2025-07-01');

-- Simulate failure by inserting a negative bonus to cause CHECK failure
-- Uncomment next line to simulate failure and rollback
-- INSERT INTO bonuses (employee_id, bonus_amount, bonus_date) VALUES (1, -500.00, '2025-07-01');

-- If no error, commit
COMMIT;

-- ROLLBACK TO SAVEPOINT before_bonus_insert;
