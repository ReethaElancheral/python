--  8. Organization Tree & Reporting Levels 
-- Requirements: 
--  Show full employee → manager → director structure. 
--  Use WITH RECURSIVE to generate full org chart. 
--  Use ROW_NUMBER() to order direct reports. 
--  Rank managers by number of subordinates. 
--  Compare leadership changes using LAG()/LEAD(). 

-- Create Database
CREATE DATABASE IF NOT EXISTS OrganizationDB;
USE OrganizationDB;

-- Tables
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(50),
    manager_id INT NULL,
    hire_date DATE,
    FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

-- Sample Data
INSERT INTO employees VALUES
(1,'Alice','Director',NULL,'2020-01-01'),
(2,'Bob','Manager',1,'2021-01-01'),
(3,'Charlie','Manager',1,'2021-06-01'),
(4,'Diana','Lead',2,'2022-01-01'),
(5,'Eve','Lead',2,'2022-03-01'),
(6,'Frank','Staff',4,'2023-01-01'),
(7,'Grace','Staff',5,'2023-02-01');

-- Recursive CTE to generate full org chart
WITH RECURSIVE org_chart AS (
    SELECT employee_id, name, position, manager_id, hire_date, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.employee_id, e.name, e.position, e.manager_id, e.hire_date, oc.level + 1
    FROM employees e
    INNER JOIN org_chart oc ON e.manager_id = oc.employee_id
)
SELECT * FROM org_chart
ORDER BY level, manager_id, employee_id;

-- ROW_NUMBER() to order direct reports under each manager
WITH direct_reports AS (
    SELECT employee_id, name, position, manager_id,
           ROW_NUMBER() OVER (PARTITION BY manager_id ORDER BY hire_date) AS report_no
    FROM employees
)
SELECT * FROM direct_reports
ORDER BY manager_id, report_no;

-- Rank managers by number of subordinates
WITH sub_count AS (
    SELECT manager_id, COUNT(*) AS num_subordinates
    FROM employees
    WHERE manager_id IS NOT NULL
    GROUP BY manager_id
)
SELECT e.employee_id AS manager_id, e.name AS manager_name, sc.num_subordinates,
       RANK() OVER (ORDER BY sc.num_subordinates DESC) AS rank_by_subordinates
FROM sub_count sc
JOIN employees e ON sc.manager_id = e.employee_id;

-- LAG() / LEAD() to compare hire dates for leadership changes
WITH leadership_change AS (
    SELECT employee_id, name, position, manager_id, hire_date,
           LAG(hire_date) OVER (PARTITION BY manager_id ORDER BY hire_date) AS prev_hire,
           LEAD(hire_date) OVER (PARTITION BY manager_id ORDER BY hire_date) AS next_hire
    FROM employees
)
SELECT * FROM leadership_change
ORDER BY manager_id, hire_date;
