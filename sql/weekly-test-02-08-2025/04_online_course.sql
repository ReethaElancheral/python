-- 4. Online Course Platform
-- Requirements:
-- Tables: students, courses, enrollments, grades.
-- Get list of students using SELECT, filter by course name.
-- Use INNER JOIN to show enrolled students with scores.
-- CASE to assign grade categories (A/B/C).
-- Use AVG() to get average marks per course.
-- Use GROUP BY + HAVING to show only courses with more than 50 students.
-- Use IN to get students enrolled in specific courses.
-- Use a correlated subquery to get top student in each course.


CREATE DATABASE IF NOT EXISTS OnlineCourseDB;
USE OnlineCourseDB;


CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    instructor VARCHAR(100)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT,
    marks INT,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);


INSERT INTO students (name, email, city) VALUES
('Amit Sharma', 'amit@example.com', 'Delhi'),
('Sneha Roy', 'sneha@example.com', 'Kolkata'),
('Rahul Mehra', 'rahul@example.com', 'Mumbai'),
('Pooja Nair', 'pooja@example.com', 'Bangalore'),
('David Paul', 'david@example.com', 'Chennai');

INSERT INTO courses (course_name, instructor) VALUES
('Python Programming', 'Mr. Kumar'),
('Data Science', 'Ms. Singh'),
('Web Development', 'Mr. Iqbal'),
('Machine Learning', 'Dr. Rao');

INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1), (2, 1), (3, 2), (4, 3), (1, 2),
(2, 3), (3, 3), (5, 1), (4, 2), (5, 4);

INSERT INTO grades (enrollment_id, marks) VALUES
(1, 85), (2, 90), (3, 78), (4, 88), (5, 95),
(6, 82), (7, 91), (8, 67), (9, 76), (10, 89);

-- Queries

-- 1. Get list of students using SELECT, filter by course name
SELECT s.name AS student_name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Python Programming';

-- 2. INNER JOIN to show enrolled students with scores
SELECT s.name AS student_name, c.course_name, g.marks
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
JOIN grades g ON e.enrollment_id = g.enrollment_id;

-- 3. CASE to assign grade categories (A/B/C)
SELECT s.name AS student_name, c.course_name, g.marks,
       CASE
           WHEN g.marks >= 90 THEN 'A'
           WHEN g.marks >= 75 THEN 'B'
           ELSE 'C'
       END AS grade_category
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
JOIN grades g ON e.enrollment_id = g.enrollment_id;

-- 4. AVG() to get average marks per course
SELECT c.course_name, AVG(g.marks) AS avg_marks
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
JOIN grades g ON e.enrollment_id = g.enrollment_id
GROUP BY c.course_id;

-- 5. GROUP BY + HAVING to show only courses with more than 2 students (you can adjust as needed)
SELECT c.course_name, COUNT(e.enrollment_id) AS total_students
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id
HAVING COUNT(e.enrollment_id) > 2;

-- 6. IN to get students enrolled in specific courses
SELECT s.name, c.course_name
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name IN ('Python Programming', 'Data Science');

-- 7. Correlated subquery to get top student in each course
SELECT c.course_name, s.name AS top_student, g.marks
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
JOIN students s ON e.student_id = s.student_id
JOIN grades g ON e.enrollment_id = g.enrollment_id
WHERE g.marks = (
    SELECT MAX(g2.marks)
    FROM enrollments e2
    JOIN grades g2 ON e2.enrollment_id = g2.enrollment_id
    WHERE e2.course_id = c.course_id
);
