-- 8. School Student & Grade Management 
-- Requirements: 
--  Tables: students, subjects, grades 
--  Insert new grades with FOREIGN KEY to student and subject. 
--  Update grade when a retest occurs.
--  Delete failing grades on student withdrawal. 
--  CHECK (grade BETWEEN 0 AND 100), NOT NULL on subject name. 
--  Modify constraint to expand grade scale (0-150). 
--  Use transactions to insert or update grades in batch with rollback.

-- Create Database
CREATE DATABASE IF NOT EXISTS SchoolDB;
USE SchoolDB;

-- Create Students Table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- Create Subjects Table
CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL
);

-- Create Grades Table
CREATE TABLE grades (
    grade_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade INT CHECK (grade BETWEEN 0 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Insert Sample Students
INSERT INTO students (name, email) VALUES
('Rehan Mehra', 'rehan@example.com'),
('Kavya Das', 'kavya@example.com'),
('Aarav Patel', 'aarav@example.com');

-- Insert Sample Subjects
INSERT INTO subjects (subject_name) VALUES
('Mathematics'), ('Physics'), ('Chemistry');

-- Insert Initial Grades
INSERT INTO grades (student_id, subject_id, grade) VALUES
(1, 1, 85),
(1, 2, 90),
(2, 1, 70),
(3, 3, 60);

-- UPDATE Grade after retest
UPDATE grades SET grade = 95 WHERE student_id = 1 AND subject_id = 1;

-- DELETE failing grades on withdrawal
DELETE FROM students WHERE student_id = 3;

-- Modify CHECK constraint for expanded grading scale (0–150)
-- Drop old CHECK constraint first (MySQL limitation workaround)
ALTER TABLE grades DROP CHECK grades_chk_1;

-- Recreate new CHECK constraint for wider range
ALTER TABLE grades ADD CONSTRAINT chk_grade_range CHECK (grade BETWEEN 0 AND 150);

-- Transaction for batch grade insert/update
START TRANSACTION;

-- Insert or update grades
INSERT INTO grades (student_id, subject_id, grade) VALUES (2, 2, 88)
ON DUPLICATE KEY UPDATE grade = VALUES(grade);

INSERT INTO grades (student_id, subject_id, grade) VALUES (1, 3, 91)
ON DUPLICATE KEY UPDATE grade = VALUES(grade);

-- Simulate error
-- INSERT INTO grades (student_id, subject_id, grade) VALUES (99, 1, 80); -- Invalid student_id (fails)

-- If all good
COMMIT;

-- If any error occurs
-- ROLLBACK;

-- View All Grades
SELECT * FROM grades;
