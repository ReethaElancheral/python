--  1. Employee Promotion Tracker 
-- Requirements: 
--  Maintain employee history with promotions. 
--  Use ROW_NUMBER() to list promotions chronologically. 
--  Use LEAD() to compare previous and current roles/salaries. 
--  Create a report showing the time between promotions. 
--  Build a recursive hierarchy showing manager → employee chain. 
--  Use RANK() to identify fastest-promoted employees. 
--  Use CTEs to modularize query logic.


CREATE DATABASE IF NOT EXISTS EmployeePromotionDB;
USE EmployeePromotionDB;

-- Employee table with history
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT,
    joining_date DATE
);

CREATE TABLE promotions (
    promo_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_id INT,
    promotion_date DATE,
    role VARCHAR(100),
    salary DECIMAL(10,2),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

-- Sample Data
INSERT INTO employees VALUES
(1, 'Alice', NULL, '2015-01-01'),
(2, 'Bob', 1, '2016-06-01'),
(3, 'Charlie', 1, '2017-03-15'),
(4, 'David', 2, '2018-11-20');

INSERT INTO promotions(emp_id, promotion_date, role, salary) VALUES
(2, '2017-01-01', 'Junior Dev', 40000),
(2, '2018-01-01', 'Mid Dev', 50000),
(2, '2020-06-01', 'Senior Dev', 65000),
(3, '2018-03-15', 'Junior Analyst', 42000),
(3, '2021-01-01', 'Analyst', 52000),
(4, '2020-01-01', 'Trainee', 30000),
(4, '2023-01-01', 'Jr Developer', 40000);

-- ROW_NUMBER(): Promotions chronologically per employee
SELECT *,
       ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY promotion_date) AS promo_order
FROM promotions;

-- LEAD(): Compare current and next role/salary
SELECT *,
       LEAD(role) OVER (PARTITION BY emp_id ORDER BY promotion_date) AS next_role,
       LEAD(salary) OVER (PARTITION BY emp_id ORDER BY promotion_date) AS next_salary
FROM promotions;

-- Report: Time between promotions using LEAD()
SELECT emp_id,
       promotion_date AS current_promo_date,
       LEAD(promotion_date) OVER (PARTITION BY emp_id ORDER BY promotion_date) AS next_promo_date,
       DATEDIFF(
           LEAD(promotion_date) OVER (PARTITION BY emp_id ORDER BY promotion_date),
           promotion_date
       ) AS days_between_promotions
FROM promotions;

-- Recursive CTE: Manager → Employee chain
WITH RECURSIVE emp_hierarchy AS (
    SELECT emp_id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id, eh.level + 1
    FROM employees e
    JOIN emp_hierarchy eh ON e.manager_id = eh.emp_id
)
SELECT * FROM emp_hierarchy;

-- RANK(): Fastest promoted employees (least average days between promotions)
WITH promo_diff AS (
    SELECT emp_id,
           promotion_date,
           LEAD(promotion_date) OVER (PARTITION BY emp_id ORDER BY promotion_date) AS next_promo_date
    FROM promotions
),
avg_promo_days AS (
    SELECT emp_id,
           AVG(DATEDIFF(next_promo_date, promotion_date)) AS avg_days
    FROM promo_diff
    WHERE next_promo_date IS NOT NULL
    GROUP BY emp_id
)
SELECT *,
       RANK() OVER (ORDER BY avg_days ASC) AS promotion_speed_rank
FROM avg_promo_days;

-- Final: CTE-based modular report combining everything
WITH promo_cte AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY promotion_date) AS promo_order,
           LEAD(role) OVER (PARTITION BY emp_id ORDER BY promotion_date) AS next_role,
           LEAD(salary) OVER (PARTITION BY emp_id ORDER BY promotion_date) AS next_salary,
           LEAD(promotion_date) OVER (PARTITION BY emp_id ORDER BY promotion_date) AS next_promo_date
    FROM promotions
),
hierarchy_cte AS (
    SELECT emp_id, name, manager_id FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.emp_id, e.name, e.manager_id
    FROM employees e
    JOIN hierarchy_cte h ON e.manager_id = h.emp_id
)
SELECT p.*, e.name, h.manager_id, DATEDIFF(p.next_promo_date, p.promotion_date) AS days_between
FROM promo_cte p
JOIN employees e ON p.emp_id = e.emp_id
JOIN hierarchy_cte h ON e.emp_id = h.emp_id;
