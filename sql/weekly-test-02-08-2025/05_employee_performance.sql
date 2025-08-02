-- 5. Employee Performance Review System
-- Requirements:
-- Tables: employees, reviews, departments.
-- Use SELF JOIN to compare employees with their managers.
-- Use ROW_NUMBER() (optional) to order review entries.
-- Aggregate average score per department.
-- Use CASE for rating conversion (Excellent/Good/Average).
-- Use IS NOT NULL to filter completed reviews.
-- Use subquery in SELECT to fetch latest review per employee.
-- Sort by review score and department.

CREATE DATABASE IF NOT EXISTS EmployeeReviewDB;
USE EmployeeReviewDB;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    manager_id INT,
    dept_id INT,
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id),
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE reviews (
    review_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    review_date DATE,
    score INT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

-- Insert Sample Data

INSERT INTO departments (name) VALUES
('HR'), ('IT'), ('Finance');

INSERT INTO employees (name, manager_id, dept_id) VALUES
('Priya Sharma', NULL, 1),     -- Manager
('Rohan Patel', 1, 1),
('Sneha Iyer', 1, 1),
('Anil Mehta', NULL, 2),       -- Manager
('Sara Khan', 4, 2),
('Vikram Rao', NULL, 3);       -- Manager

INSERT INTO reviews (emp_id, review_date, score) VALUES
(2, '2025-06-01', 85),
(3, '2025-06-02', 78),
(5, '2025-06-05', 92),
(2, '2025-07-01', 88),
(3, '2025-07-01', 80),
(5, '2025-07-01', 95);

-- 1. SELF JOIN to compare employees with their managers
SELECT e.name AS employee_name, m.name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;

-- 2. ROW_NUMBER() to order review entries (MySQL 8.0+ supports window functions)
SELECT emp_id, review_date, score,
       ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY review_date DESC) AS row_num
FROM reviews;

-- 3. Aggregate average score per department
SELECT d.name AS department, AVG(r.score) AS avg_score
FROM reviews r
JOIN employees e ON r.emp_id = e.emp_id
JOIN departments d ON e.dept_id = d.dept_id
GROUP BY d.dept_id;

-- 4. CASE for rating conversion (Excellent/Good/Average)
SELECT e.name, r.score,
       CASE
           WHEN r.score >= 90 THEN 'Excellent'
           WHEN r.score >= 75 THEN 'Good'
           ELSE 'Average'
       END AS rating
FROM reviews r
JOIN employees e ON r.emp_id = e.emp_id;

-- 5. IS NOT NULL to filter completed reviews
SELECT * FROM reviews
WHERE score IS NOT NULL;

-- 6. Subquery in SELECT to fetch latest review per employee
SELECT e.name,
       (SELECT r2.score
        FROM reviews r2
        WHERE r2.emp_id = e.emp_id
        ORDER BY r2.review_date DESC
        LIMIT 1) AS latest_score
FROM employees e;

-- 7. Sort by review score and department
SELECT e.name, d.name AS department, r.score
FROM reviews r
JOIN employees e ON r.emp_id = e.emp_id
JOIN departments d ON e.dept_id = d.dept_id
ORDER BY r.score DESC, d.name;
