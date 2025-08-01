-- Project 9: E-Learning Platform Performance Tracker

CREATE DATABASE IF NOT EXISTS elearning_db;
USE elearning_db;

-- Tables

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY,
    name VARCHAR(100),
    expertise VARCHAR(100)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    title VARCHAR(100),
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    user_id INT,
    course_id INT,
    completion_rate DECIMAL(5,2),
    completed BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Sample Data

INSERT INTO users (user_id, name, email) VALUES
(1, 'Amit', 'amit@example.com'),
(2, 'Priya', 'priya@example.com'),
(3, 'Ravi', 'ravi@example.com'),
(4, 'Sneha', 'sneha@example.com'),
(5, 'Kiran', 'kiran@example.com');

INSERT INTO instructors (instructor_id, name, expertise) VALUES
(1, 'Dr. Sharma', 'Data Science'),
(2, 'Prof. Mehta', 'Web Development'),
(3, 'Mrs. Kapoor', 'Design');

INSERT INTO courses (course_id, title, instructor_id) VALUES
(1, 'Data Science Bootcamp', 1),
(2, 'Full Stack Web Dev', 2),
(3, 'UI/UX Design Basics', 3);

INSERT INTO enrollments (enrollment_id, user_id, course_id, completion_rate, completed) VALUES
(1, 1, 1, 95.00, TRUE),
(2, 2, 1, 85.00, TRUE),
(3, 3, 1, 60.00, FALSE),
(4, 4, 2, 80.00, TRUE),
(5, 5, 2, 90.00, TRUE),
(6, 1, 3, 40.00, FALSE),
(7, 2, 2, 100.00, TRUE),
(8, 3, 2, 70.00, FALSE),
(9, 4, 3, 30.00, FALSE),
(10, 5, 3, 75.00, TRUE);

-- Queries

-- 1. Total enrollments per course
SELECT 
    c.title AS course_title,
    COUNT(e.enrollment_id) AS total_enrollments
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_id, c.title;

-- 2. Average completion rate per instructor
SELECT 
    i.name AS instructor_name,
    AVG(e.completion_rate) AS avg_completion_rate
FROM instructors i
JOIN courses c ON i.instructor_id = c.instructor_id
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY i.instructor_id, i.name;

-- 3. Courses with more than 20 completions
SELECT 
    c.title,
    COUNT(e.enrollment_id) AS completions
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
WHERE e.completed = TRUE
GROUP BY c.course_id, c.title
HAVING completions > 2;

-- 4. INNER JOIN users and courses
SELECT 
    u.name AS user_name,
    c.title AS course_title,
    e.completion_rate,
    e.completed
FROM users u
JOIN enrollments e ON u.user_id = e.user_id
JOIN courses c ON e.course_id = c.course_id;

-- 5. LEFT JOIN to list courses without enrollments
SELECT 
    c.title,
    e.enrollment_id
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;

-- 6. SELF JOIN to compare users who completed the same course
SELECT 
    u1.name AS user_1,
    u2.name AS user_2,
    c.title AS course_title
FROM enrollments e1
JOIN enrollments e2 ON e1.course_id = e2.course_id 
    AND e1.completed = TRUE AND e2.completed = TRUE 
    AND e1.user_id < e2.user_id
JOIN users u1 ON e1.user_id = u1.user_id
JOIN users u2 ON e2.user_id = u2.user_id
JOIN courses c ON e1.course_id = c.course_id;
