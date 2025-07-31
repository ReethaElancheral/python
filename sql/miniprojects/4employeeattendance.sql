CREATE DATABASE company_hr;
USE company_hr;

CREATE TABLE departments (
  dept_id INT AUTO_INCREMENT PRIMARY KEY,
  dept_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE employees (
  emp_id INT AUTO_INCREMENT PRIMARY KEY,
  emp_name VARCHAR(100) NOT NULL,
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE attendance (
  att_id INT AUTO_INCREMENT PRIMARY KEY,
  emp_id INT,
  date DATE,
  in_time TIME,
  out_time TIME,
  FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

INSERT INTO departments (dept_name) VALUES 
('HR'), ('Finance'), ('IT'), ('Sales'), ('Marketing');

INSERT INTO employees (emp_name, dept_id) VALUES
('Alice', 1), ('Bob', 2), ('Carol', 3), ('David', 4), ('Eva', 5),
('Farhan', 1), ('Gita', 2), ('Hari', 3), ('Indira', 4), ('Jay', 5),
('Kiran', 1), ('Lakshmi', 2), ('Manoj', 3), ('Nita', 4), ('Om', 5);

INSERT INTO attendance (emp_id, date, in_time, out_time) VALUES
(1, '2025-07-29', '09:00:00', '17:00:00'),
(1, '2025-07-30', '09:15:00', '17:05:00'),
(2, '2025-07-29', '09:10:00', '17:10:00'),
(2, '2025-07-30', '09:00:00', '16:55:00'),
(3, '2025-07-29', '09:05:00', '17:20:00'),
(4, '2025-07-29', '09:00:00', '17:00:00'),
(4, '2025-07-30', '09:20:00', '17:30:00'),
(5, '2025-07-30', '09:00:00', '16:50:00'),
(6, '2025-07-29', '08:55:00', '17:00:00'),
(6, '2025-07-30', '09:00:00', '17:15:00'),
(7, '2025-07-29', '09:05:00', '16:50:00'),
(8, '2025-07-30', '09:10:00', '17:10:00'),
(9, '2025-07-30', '09:00:00', '17:00:00'),
(10, '2025-07-29', '09:20:00', '17:00:00'),
(11, '2025-07-30', '09:00:00', '17:00:00'),
(12, '2025-07-30', '09:00:00', '17:00:00');

-- Calculate Working Hours

SELECT 
  e.emp_name,
  a.date,
  a.in_time,
  a.out_time,
  TIMEDIFF(a.out_time, a.in_time) AS working_hours
FROM attendance a
JOIN employees e ON a.emp_id = e.emp_id;

-- Total Working Hours for Each Employee

SELECT 
  e.emp_name,
  SEC_TO_TIME(SUM(TIME_TO_SEC(TIMEDIFF(a.out_time, a.in_time)))) AS total_worked
FROM attendance a
JOIN employees e ON a.emp_id = e.emp_id
GROUP BY e.emp_id;

-- Count Present Days (days they attended)

SELECT 
  e.emp_name,
  COUNT(a.att_id) AS present_days
FROM employees e
LEFT JOIN attendance a ON e.emp_id = a.emp_id
GROUP BY e.emp_id;

-- Count Absent Days (Assume total working days is 2 in example)

SELECT 
  e.emp_name,
  2 - COUNT(a.att_id) AS absent_days
FROM employees e
LEFT JOIN attendance a ON e.emp_id = a.emp_id
GROUP BY e.emp_id;

