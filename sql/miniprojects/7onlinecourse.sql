-- -----------------------------------------------
-- Project 7: Online Course Registration
-- Requirements:
-- • Create course_portal database
-- • Tables: courses, students, registrations, instructors
-- • Many-to-many between courses and students
-- • Add 5 courses, 8 students, 3 instructors
-- • Write queries to:
--    - Count how many students per course
--    - List students not registered for any course
-- -----------------------------------------------

-- Create database
CREATE DATABASE IF NOT EXISTS course_portal;
USE course_portal;

-- Create instructors table
CREATE TABLE instructorsnew (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

-- Create courses table
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- Create students table
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Many-to-many relationship table: registrations
CREATE TABLE registrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert instructors
INSERT INTO instructorsnew (name) VALUES
('Dr. Smith'), ('Prof. Johnson'), ('Ms. Lee');

-- Insert courses
INSERT INTO courses (title, instructor_id) VALUES
('Python for Beginners', 1),
('Web Development', 2),
('Data Structures', 2),
('Machine Learning', 3),
('Database Systems', 1);

-- Insert students
INSERT INTO students (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com'),
('Eva', 'eva@example.com'),
('Frank', 'frank@example.com'),
('Grace', 'grace@example.com'),
('Hannah', 'hannah@example.com');

-- Insert registrations
INSERT INTO registrations (student_id, course_id) VALUES
(1, 1), (1, 2),
(2, 2), (2, 3),
(3, 3),
(4, 1), (4, 5),
(5, 4),
(6, 1);



-- 1. Count how many students per course
SELECT 
    c.title AS course_title,
    COUNT(r.student_id) AS student_count
FROM courses c
LEFT JOIN registrations r ON c.course_id = r.course_id
GROUP BY c.course_id;

-- 2. List students not registered for any course
SELECT 
    s.name AS student_name,
    s.email
FROM students s
LEFT JOIN registrations r ON s.student_id = r.student_id
WHERE r.registration_id IS NULL;
