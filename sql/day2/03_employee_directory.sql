
-- 3. Employee Directory

-- Create table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    email VARCHAR(100),
    hire_date DATE,
    manager_id INT
);
INSERT INTO employees (emp_id, name, department, salary, email, hire_date, manager_id) VALUES
(1, 'John Smith', 'Sales', 60000, 'john.smith@example.com', '2020-01-15', NULL),
(2, 'Jane Doe', 'Marketing', 65000, 'jane.doe@example.com', '2019-07-30', 1),
(3, 'Michael Brown', 'Sales', 58000, 'michael.brown@example.com', '2021-03-10', 1),
(4, 'Emily Davis', 'HR', 55000, 'emily.davis@example.com', '2018-05-20', NULL),
(5, 'David Wilson', 'Marketing', 70000, 'david.wilson@example.com', '2017-11-02', 2),
(6, 'Sarah Johnson', 'IT', 75000, 'sarah.johnson@example.com', '2019-09-25', NULL),
(7, 'Chris Lee', 'IT', 72000, 'chris.lee@example.com', '2020-12-01', 6),
(8, 'Anna Kim', 'Finance', 68000, 'anna.kim@example.com', '2018-08-16', NULL),
(9, 'Mark Taylor', 'Sales', 62000, 'mark.taylor@example.com', '2021-06-22', 1),
(10, 'Sophia Martinez', 'Finance', 64000, 'sophia.martinez@example.com', '2019-10-11', 8);


-- Select employees with salary > 50,000 in Sales or Marketing
SELECT name, salary, department FROM employees
WHERE salary > 50000 AND department IN ('Sales', 'Marketing');

-- List all unique departments
SELECT DISTINCT department FROM employees;

-- Find employees with names ending in 'an'
SELECT * FROM employees
WHERE name LIKE '%an';

-- Identify employees with no manager
SELECT * FROM employees
WHERE manager_id IS NULL;

-- Use BETWEEN for salaries between 40,000 and 80,000
SELECT * FROM employees
WHERE salary BETWEEN 40000 AND 80000;

-- Sort by department ASC, salary DESC
SELECT * FROM employees
ORDER BY department ASC, salary DESC;
