-- Project 19: School Subject Enrollment
CREATE DATABASE IF NOT EXISTS school_enrollment_db;
USE school_enrollment_db;

CREATE TABLE IF NOT EXISTS subject_enrollments (
    enroll_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100),
    subject VARCHAR(50),
    grade INT,
    status VARCHAR(20)
);

-- Insert sample data
INSERT INTO subject_enrollments (student_name, subject, grade, status) VALUES
('Alice Johnson', 'Math', 85, 'Passed'),
('Aarav Mehta', 'English', 92, 'Passed'),
('Ritika Sharma', 'Science', 76, 'Passed'),
('Mohammed Ali', 'Math', 88, NULL),
('Anjali Rao', 'History', 81, 'Passed'),
('David Thomas', 'English', 59, NULL),
('Karan Kapoor', 'Math', 45, 'Failed'),
('Anaya Pillai', 'Biology', 79, 'Passed'),
('Ravi Teja', 'Math', 82, 'Passed'),
('Akshita Nair', 'English', 87, NULL);

-- 1. Students with grades >= 80 in Math or English
SELECT student_name, grade, subject
FROM subject_enrollments
WHERE grade >= 80 AND subject IN ('Math', 'English');

-- 2. LIKE search on student_name
SELECT * FROM subject_enrollments
WHERE student_name LIKE '%a%';

-- 3. NULL check for status
SELECT * FROM subject_enrollments
WHERE status IS NULL;

-- 4. List all subjects
SELECT DISTINCT subject FROM subject_enrollments;

-- 5. Sort by grade descending
SELECT * FROM subject_enrollments
ORDER BY grade DESC;
