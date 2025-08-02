-- Project 7: Online Course Completion Analytics

CREATE DATABASE IF NOT EXISTS course_db;
USE course_db;

-- Tables
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    title VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE completion (
    completion_id INT PRIMARY KEY,
    enrollment_id INT,
    completion_date DATE,
    score DECIMAL(5,2),
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);

-- Insert data
INSERT INTO courses VALUES
(1, 'SQL Basics', 'Tech'),
(2, 'Python Programming', 'Tech'),
(3, 'Business Communication', 'Business');

INSERT INTO students VALUES
(1, 'Rahul Sharma'),
(2, 'Anita Patel'),
(3, 'Sunil Kumar'),
(4, 'Priya Singh');

INSERT INTO enrollments VALUES
(1, 1, 1, '2024-01-10'),
(2, 2, 1, '2024-01-15'),
(3, 3, 2, '2024-02-01'),
(4, 4, 3, '2024-02-10'),
(5, 1, 2, '2024-02-15');

INSERT INTO completion VALUES
(1, 1, '2024-03-01', 85.00),
(2, 2, '2024-03-05', 75.50),
(3, 3, '2024-03-10', 90.00),
(4, 4, '2024-03-15', 65.00);

-- Subquery in FROM to get completion rate per course
SELECT c.course_id, c.title, completion_stats.completion_rate
FROM courses c
JOIN (
    SELECT e.course_id,
           COUNT(c.completion_id) / COUNT(e.enrollment_id) * 100 AS completion_rate
    FROM enrollments e
    LEFT JOIN completion c ON e.enrollment_id = c.enrollment_id
    GROUP BY e.course_id
) AS completion_stats ON c.course_id = completion_stats.course_id;

-- INTERSECT to find students who completed both "SQL Basics" and "Python Programming"
-- Note: MySQL does not support INTERSECT directly, emulate with INNER JOIN

SELECT s.student_id, s.name
FROM students s
JOIN enrollments e1 ON s.student_id = e1.student_id
JOIN completion c1 ON e1.enrollment_id = c1.enrollment_id
JOIN courses cr1 ON e1.course_id = cr1.course_id AND cr1.title = 'SQL Basics'
JOIN enrollments e2 ON s.student_id = e2.student_id
JOIN completion c2 ON e2.enrollment_id = c2.enrollment_id
JOIN courses cr2 ON e2.course_id = cr2.course_id AND cr2.title = 'Python Programming';

-- UNION to list all students from two course batches (SQL Basics and Business Communication)

SELECT s.student_id, s.name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.title = 'SQL Basics'

UNION

SELECT s.student_id, s.name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.title = 'Business Communication';

-- CASE for grading: A/B/C/F based on score thresholds

SELECT s.name, c.title, comp.score,
CASE
    WHEN comp.score >= 90 THEN 'A'
    WHEN comp.score >= 80 THEN 'B'
    WHEN comp.score >= 70 THEN 'C'
    ELSE 'F'
END AS grade
FROM completion comp
JOIN enrollments e ON comp.enrollment_id = e.enrollment_id
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id;

-- Correlated subquery to find student with highest grade in each course

SELECT c.course_id, c.title,
       (SELECT s.name
        FROM completion comp2
        JOIN enrollments e2 ON comp2.enrollment_id = e2.enrollment_id
        JOIN students s ON e2.student_id = s.student_id
        WHERE e2.course_id = c.course_id
        ORDER BY comp2.score DESC LIMIT 1) AS top_student
FROM courses c;

-- Use DATE functions to show completion trends over months

SELECT DATE_FORMAT(completion_date, '%Y-%m') AS month, COUNT(*) AS completions
FROM completion
GROUP BY month
ORDER BY month;
