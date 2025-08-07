-- 3. Student Academic Performance Monitor 
-- Requirements: 
--  Track student grades across semesters. 
--  Use RANK() to determine toppers in each subject. 
--  Use ROW_NUMBER() to show attempt order of exams. 
--  Use LEAD() and LAG() to compare marks between semesters. 
--  Create CTEs for subject-wise, semester-wise analysis. 
--  Use recursive CTE to navigate course prerequisites.

-- Create Database
CREATE DATABASE IF NOT EXISTS StudentPerformanceDB;
USE StudentPerformanceDB;

-- Tables
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE semesters (
    semester_id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    subject_id INT,
    prereq_course_id INT NULL,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    semester_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (semester_id) REFERENCES semesters(semester_id)
);

-- Sample Data
INSERT INTO students VALUES
(1,'Alice'),(2,'Bob'),(3,'Charlie'),(4,'Diana');

INSERT INTO subjects VALUES
(1,'Math'),(2,'Physics'),(3,'Chemistry');

INSERT INTO semesters VALUES
(1,'Sem1'),(2,'Sem2');

INSERT INTO courses VALUES
(1,1,NULL),(2,2,NULL),(3,3,NULL),(4,1,1),(5,2,2);

INSERT INTO grades (student_id, course_id, semester_id, marks) VALUES
(1,1,1,85),(1,2,1,78),(1,3,1,90),(1,4,2,88),(1,5,2,80),
(2,1,1,70),(2,2,1,75),(2,3,1,80),(2,4,2,72),(2,5,2,78),
(3,1,1,90),(3,2,1,85),(3,3,1,88),(3,4,2,92),(3,5,2,89),
(4,1,1,65),(4,2,1,60),(4,3,1,70),(4,4,2,68),(4,5,2,65);

-- CTE: Subject-wise topper ranking
WITH subject_ranks AS (
    SELECT g.student_id, s.name AS student_name, sub.name AS subject_name, g.marks,
           RANK() OVER (PARTITION BY g.course_id ORDER BY g.marks DESC) AS rank_in_subject
    FROM grades g
    JOIN students s ON g.student_id = s.student_id
    JOIN courses c ON g.course_id = c.course_id
    JOIN subjects sub ON c.subject_id = sub.subject_id
)
SELECT * FROM subject_ranks
ORDER BY subject_name, rank_in_subject;

-- CTE: Row number of exam attempts per student
WITH attempt_order AS (
    SELECT student_id, course_id, semester_id, marks,
           ROW_NUMBER() OVER (PARTITION BY student_id, course_id ORDER BY semester_id) AS attempt_no
    FROM grades
)
SELECT s.name AS student_name, sub.name AS subject_name, a.semester_id, a.marks, a.attempt_no
FROM attempt_order a
JOIN students s ON a.student_id = s.student_id
JOIN courses c ON a.course_id = c.course_id
JOIN subjects sub ON c.subject_id = sub.subject_id
ORDER BY student_name, subject_name, attempt_no;

-- CTE: Compare marks between semesters using LAG/LEAD
WITH semester_marks AS (
    SELECT student_id, course_id, semester_id, marks,
           LAG(marks) OVER (PARTITION BY student_id, course_id ORDER BY semester_id) AS prev_sem_marks,
           LEAD(marks) OVER (PARTITION BY student_id, course_id ORDER BY semester_id) AS next_sem_marks
    FROM grades
)
SELECT s.name AS student_name, sub.name AS subject_name, sm.semester_id, sm.marks, sm.prev_sem_marks, sm.next_sem_marks
FROM semester_marks sm
JOIN students s ON sm.student_id = s.student_id
JOIN courses c ON sm.course_id = c.course_id
JOIN subjects sub ON c.subject_id = sub.subject_id
ORDER BY student_name, subject_name, sm.semester_id;

-- Recursive CTE: Show course prerequisites chain
WITH RECURSIVE prereq_chain(course_id, subject_id, prereq_course_id, level) AS (
    SELECT course_id, subject_id, prereq_course_id, 1 AS level
    FROM courses
    WHERE prereq_course_id IS NOT NULL
    UNION ALL
    SELECT c.course_id, c.subject_id, c.prereq_course_id, pc.level + 1
    FROM courses c
    INNER JOIN prereq_chain pc ON c.prereq_course_id = pc.course_id
)
SELECT pc.course_id, sub.name AS subject_name, pc.prereq_course_id, psub.name AS prereq_subject, pc.level
FROM prereq_chain pc
JOIN subjects sub ON pc.course_id = sub.subject_id
LEFT JOIN subjects psub ON pc.prereq_course_id = psub.subject_id
ORDER BY level, course_id;
