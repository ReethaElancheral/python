
-- 1. Student Performance Tracker

-- Create table
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    grade INT,
    attendance DECIMAL(5,2),
    subject VARCHAR(50),
    email VARCHAR(100)
);

-- Inserting into students table
INSERT INTO students (student_id, name, grade, attendance, subject, email) VALUES
(1, 'Ananya R', 92, 96, 'Math', 'ananya@example.com'),
(2, 'Akhil M', 85, 91, 'Science', 'akhil@example.com'),
(3, 'Bhavna K', 78, 88, 'Math', NULL),
(4, 'Arjun S', 81, 95, 'English', 'arjun.s@example.com'),
(5, 'Diya N', 67, 72, 'Science', 'diya@example.com'),
(6, 'Aarthi V', 88, 93, 'Math', NULL),
(7, 'Kiran J', 90, 99, 'English', 'kiran.j@example.com'),
(8, 'Aditya R', 95, 98, 'Science', 'aditya.r@example.com'),
(9, 'Riya L', 79, 85, 'Math', 'riya@example.com'),
(10, 'Abhinav C', 82, 94, 'English', 'abhinav.c@example.com');

-- Retrieve students with grades above 80 and attendance > 90%
SELECT name, grade FROM students
WHERE grade > 80 AND attendance > 90;

-- List all distinct subjects offered
SELECT DISTINCT subject FROM students;

-- Filter students whose name starts with "A"
SELECT * FROM students
WHERE name LIKE 'A%';

-- Use IN for specific subjects (Math, Science)
SELECT * FROM students
WHERE subject IN ('Math', 'Science');

-- Find students with NULL email addresses
SELECT * FROM students
WHERE email IS NULL;

-- Sort results by grade DESC, then name ASC
SELECT * FROM students
ORDER BY grade DESC, name ASC;
