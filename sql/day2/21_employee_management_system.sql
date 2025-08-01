--  1. Employee Management System 
-- Requirements: 
--  Tables: employees, departments 
--  Show average salary per department (GROUP BY) 
--  Count employees per department (COUNT) 
--  Find departments with more than 5 employees (HAVING) 
--  INNER JOIN to show employees and their department names 
--  LEFT JOIN to find departments without employees 
--  SELF JOIN to show each employee with their manager name 
--  Use aliases like e1, e2 in SELF JOIN



CREATE DATABASE IF NOT EXISTS employee_management_db;
USE employee_management_db;


CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);


CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    department_id INT,
    manager_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
);


INSERT INTO departments (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'IT'),
(4, 'HR'),
(5, 'Finance');


INSERT INTO employees (emp_id, name, salary, department_id, manager_id) VALUES
(1, 'John Smith', 75000, 1, NULL),
(2, 'Jane Doe', 68000, 1, 1),
(3, 'Michael Brown', 72000, 2, 1),
(4, 'Emily Davis', 65000, 2, 3),
(5, 'David Wilson', 80000, 3, NULL),
(6, 'Sarah Johnson', 60000, 3, 5),
(7, 'Chris Lee', 62000, 4, NULL),
(8, 'Anna Kim', 58000, NULL, NULL),
(9, 'Mark Taylor', 55000, 5, NULL),
(10, 'Sophia Martinez', 57000, 5, 9);

-- Query 1: Average salary per department
SELECT d.department_name, AVG(e.salary) AS avg_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;

-- Query 2: Count employees per department
SELECT d.department_name, COUNT(e.emp_id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;

-- Query 3: Departments with more than 5 employees (HAVING)
SELECT d.department_name, COUNT(e.emp_id) AS employee_count
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING employee_count > 5;

-- Query 4: INNER JOIN to show employees with their department names
SELECT e.name AS employee_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;

-- Query 5: LEFT JOIN to find departments without employees
SELECT d.department_name
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
WHERE e.emp_id IS NULL;

-- Query 6: SELF JOIN to show each employee with their manager name
SELECT e1.name AS employee_name, e2.name AS manager_name
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.emp_id;
