-- 8. University Course Enrollment Dashboard
-- Requirements:
-- Tables: departments, students, courses, enrollments.
-- Use GROUP BY to get enrollment count per course.
-- Use subquery in FROM to find courses with highest dropout.
-- Use LEFT JOIN to find students not enrolled in any course.
-- Use CASE for pass/fail grade mapping.
-- Use IN for filtering courses by a list of codes.
-- Use INTERSECT to find students who completed both Python and SQL.

CREATE DATABASE IF NOT EXISTS UniversityDashboardDB;
USE UniversityDashboardDB;


CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    code VARCHAR(10),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    grade CHAR(1), -- A/B/C/D/F
    status VARCHAR(20), -- Active, Dropped
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


INSERT INTO departments (name) VALUES
('Computer Science'),
('Mathematics'),
('Physics');

INSERT INTO students (name, department_id) VALUES
('Amit Kumar', 1),
('Riya Sharma', 1),
('Kunal Verma', 2),
('Sneha Das', 2),
('Nikhil Mehra', 3),
('Pooja Nair', 1);

INSERT INTO courses (title, code, department_id) VALUES
('Intro to Python', 'CS101', 1),
('Advanced SQL', 'CS201', 1),
('Linear Algebra', 'MTH101', 2),
('Quantum Physics', 'PHY101', 3),
('Data Structures', 'CS102', 1),
('Discrete Math', 'MTH201', 2);

INSERT INTO enrollments (student_id, course_id, grade, status) VALUES
(1, 1, 'A', 'Active'),
(1, 2, 'B', 'Active'),
(2, 1, 'C', 'Active'),
(3, 3, 'B', 'Dropped'),
(3, 6, 'A', 'Active'),
(4, 3, 'F', 'Dropped'),
(5, 4, 'A', 'Active'),
(6, 2, 'A', 'Active'),
(6, 5, 'B', 'Active'),
(2, 5, 'A', 'Active');

-- Queries

-- 1. GROUP BY to get enrollment count per course
SELECT c.title, COUNT(e.enrollment_id) AS total_enrolled
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id AND e.status = 'Active'
GROUP BY c.course_id;

-- 2. Subquery in FROM to find courses with highest dropout
SELECT title, dropout_count
FROM (
    SELECT c.title, COUNT(e.enrollment_id) AS dropout_count
    FROM courses c
    JOIN enrollments e ON c.course_id = e.course_id
    WHERE e.status = 'Dropped'
    GROUP BY c.course_id
) AS drops
ORDER BY dropout_count DESC;

-- 3. LEFT JOIN to find students not enrolled in any course
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.student_id IS NULL;

-- 4. CASE for pass/fail grade mapping
SELECT s.name, c.title, e.grade,
       CASE
           WHEN e.grade IN ('A', 'B', 'C') THEN 'Pass'
           ELSE 'Fail'
       END AS result
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;

-- 5. IN for filtering courses by a list of codes
SELECT title, code FROM courses
WHERE code IN ('CS101', 'MTH201', 'PHY101');

-- 6. INTERSECT simulation: students who completed both Python and SQL
-- MySQL doesn't support INTERSECT, use INNER JOIN on subqueries
SELECT s.name FROM students s
JOIN (
    SELECT student_id FROM enrollments e
    JOIN courses c ON e.course_id = c.course_id
    WHERE c.title = 'Intro to Python' AND e.grade IN ('A', 'B', 'C')
) AS python_passed ON s.student_id = python_passed.student_id
JOIN (
    SELECT student_id FROM enrollments e
    JOIN courses c ON e.course_id = c.course_id
    WHERE c.title = 'Advanced SQL' AND e.grade IN ('A', 'B', 'C')
) AS sql_passed ON s.student_id = sql_passed.student_id;
