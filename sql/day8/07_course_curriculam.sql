--  7. Course Curriculum Path Visualizer 
-- Requirements: 
--  Track course prerequisites. 
--  Use recursive CTE to list course paths. 
--  Use RANK() to prioritize required vs elective. 
--  Use LEAD() to suggest next recommended course. 
--  Build CTEs for each student's course progress.

-- Create Database
CREATE DATABASE IF NOT EXISTS CourseCurriculumDB;
USE CourseCurriculumDB;

-- Tables
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    name VARCHAR(100),
    type ENUM('Required','Elective') NOT NULL
);

CREATE TABLE prerequisites (
    course_id INT,
    prerequisite_id INT,
    PRIMARY KEY(course_id, prerequisite_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (prerequisite_id) REFERENCES courses(course_id)
);

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE student_courses (
    student_id INT,
    course_id INT,
    completion_date DATE,
    PRIMARY KEY(student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Sample Data
INSERT INTO courses VALUES
(1,'Math 101','Required'),
(2,'Physics 101','Required'),
(3,'Chemistry 101','Elective'),
(4,'Math 201','Required'),
(5,'Physics 201','Elective');

INSERT INTO prerequisites VALUES
(4,1),
(5,2);

INSERT INTO students VALUES
(1,'Alice'),
(2,'Bob');

INSERT INTO student_courses VALUES
(1,1,'2025-01-01'),
(1,2,'2025-01-02'),
(2,1,'2025-01-03');

-- Recursive CTE: List full course paths with prerequisites
WITH RECURSIVE course_path AS (
    SELECT c.course_id, c.name AS course_name, c.type, p.prerequisite_id
    FROM courses c
    LEFT JOIN prerequisites p ON c.course_id = p.course_id
    WHERE p.prerequisite_id IS NULL
    UNION ALL
    SELECT c.course_id, c.name, c.type, p.prerequisite_id
    FROM courses c
    INNER JOIN prerequisites p ON c.course_id = p.course_id
    INNER JOIN course_path cp ON p.prerequisite_id = cp.course_id
)
SELECT * FROM course_path
ORDER BY course_id;

-- RANK() to prioritize required vs elective courses
WITH course_rank AS (
    SELECT course_id, name, type,
           RANK() OVER (PARTITION BY type ORDER BY course_id) AS type_rank
    FROM courses
)
SELECT * FROM course_rank
ORDER BY type, type_rank;

-- LEAD() to suggest next recommended course for each student
WITH student_course_order AS (
    SELECT sc.student_id, s.name AS student_name, c.course_id, c.name AS course_name, sc.completion_date,
           LEAD(c.name) OVER (PARTITION BY sc.student_id ORDER BY sc.completion_date) AS next_course
    FROM student_courses sc
    JOIN students s ON sc.student_id = s.student_id
    JOIN courses c ON sc.course_id = c.course_id
)
SELECT * FROM student_course_order
ORDER BY student_id, completion_date;

-- CTE for each student’s course progress
WITH student_progress AS (
    SELECT s.student_id, s.name AS student_name, c.course_id, c.name AS course_name, sc.completion_date
    FROM students s
    LEFT JOIN student_courses sc ON s.student_id = sc.student_id
    LEFT JOIN courses c ON sc.course_id = c.course_id
)
SELECT * FROM student_progress
ORDER BY student_id, course_id;
