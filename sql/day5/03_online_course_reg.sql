--  3. Online Course Registration 
-- Requirements: 
--  Tables: students, courses, enrollments 
--  Enroll students using INSERT INTO with FOREIGN KEY checks. 
--  UPDATE course availability based on enrollments. 
--  DELETE students and use ON DELETE CASCADE to remove enrollments. 
--  CHECK to ensure grade is between 0 and 100. 
--  Drop and recreate the CHECK constraint for grade scale update. 
--  Use a transaction for bulk enrollment, use COMMIT/ROLLBACK. 
--  Highlight consistency when partially updating multiple tables.


CREATE DATABASE IF NOT EXISTS CourseRegistrationDB;
USE CourseRegistrationDB;


CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);


CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(150) NOT NULL,
    total_seats INT NOT NULL CHECK (total_seats >= 0),
    available_seats INT NOT NULL CHECK (available_seats >= 0)
);


CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    grade INT CHECK (grade BETWEEN 0 AND 100),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);


INSERT INTO students (student_name, email) VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Carol Lee', 'carol@example.com');


INSERT INTO courses (course_name, total_seats, available_seats) VALUES
('Math 101', 30, 30),
('History 201', 25, 25),
('Physics 301', 20, 20);

-- Enroll students using INSERT with FOREIGN KEY checks
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 1, CURDATE(), 85),
(2, 2, CURDATE(), 90),
(3, 3, CURDATE(), NULL);

-- Update course availability based on enrollments
-- Decrease available_seats by 1 for each enrollment
UPDATE courses c
JOIN (
    SELECT course_id, COUNT(*) AS enrolled_count
    FROM enrollments
    GROUP BY course_id
) e ON c.course_id = e.course_id
SET c.available_seats = c.total_seats - e.enrolled_count;

-- Demonstrate DELETE student with ON DELETE CASCADE on enrollments
DELETE FROM students WHERE student_id = 3;

-- Drop and recreate CHECK constraint for grade scale update
-- MySQL requires recreating table or workaround as CHECK constraints can't be dropped easily

-- Step 1: Drop old CHECK constraint by recreating table (workaround)
ALTER TABLE enrollments
DROP CHECK grade;

-- Step 2: Add new CHECK constraint for updated grade scale (0-10 scale)
ALTER TABLE enrollments
ADD CONSTRAINT chk_grade_new CHECK (grade BETWEEN 0 AND 10);

-- Use a transaction for bulk enrollment with COMMIT/ROLLBACK

START TRANSACTION;

-- Insert bulk enrollments
INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES
(1, 2, CURDATE(), 9),
(2, 1, CURDATE(), 8);

-- Simulate failure (uncomment to test rollback)
-- INSERT INTO enrollments (student_id, course_id, enrollment_date, grade) VALUES (99, 1, CURDATE(), 7);

-- Update available seats after bulk enrollments
UPDATE courses c
JOIN (
    SELECT course_id, COUNT(*) AS enrolled_count
    FROM enrollments
    GROUP BY course_id
) e ON c.course_id = e.course_id
SET c.available_seats = c.total_seats - e.enrolled_count;

COMMIT;


-- Highlight consistency when partially updating multiple tables:
-- For example, enrollments and courses seat update are done within a single transaction above to maintain consistency
