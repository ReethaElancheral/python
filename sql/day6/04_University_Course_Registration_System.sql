-- 4. University Course Registration System 
-- Requirements: 
--  Tables: students, courses, enrollments, departments, faculty 
--  Normalize data: move department and course dependencies to separate 
-- tables. 
--  Index student_id, course_id, faculty_id. 
--  Use EXPLAIN to analyze joins for student performance reports. 
--  Optimize queries retrieving students enrolled in more than 3 courses 
-- (subquery). 
--  Denormalize data into a student performance summary. 
--  Use LIMIT for paginated course lists.

CREATE DATABASE IF NOT EXISTS UniversityDB;
USE UniversityDB;

-- Normalized tables
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100)
);

CREATE TABLE faculty (
    faculty_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    major_id INT,
    FOREIGN KEY (major_id) REFERENCES departments(department_id)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    department_id INT,
    faculty_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty(faculty_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Indexing
CREATE INDEX idx_student_id ON enrollments(student_id);
CREATE INDEX idx_course_id ON enrollments(course_id);
CREATE INDEX idx_faculty_id ON courses(faculty_id);

-- Analyze join performance
EXPLAIN SELECT s.name, c.course_name FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id;

-- Subquery: students in more than 3 courses
SELECT student_id FROM enrollments
GROUP BY student_id
HAVING COUNT(course_id) > 3;

-- Denormalized performance summary
CREATE VIEW student_performance AS
SELECT s.student_id, s.name, COUNT(e.course_id) AS course_count
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_id;

-- Paginated course list
SELECT * FROM courses LIMIT 0, 10;