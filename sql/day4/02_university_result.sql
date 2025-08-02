-- Project 2: University Academic Result Analyzer

CREATE DATABASE IF NOT EXISTS UniversityResultDB;
USE UniversityResultDB;

-- Create tables
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100),
    enrollment_date DATE
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE subjects (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100),
    course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE results (
    result_id INT PRIMARY KEY,
    student_id INT,
    subject_id INT,
    exam_type VARCHAR(20),
    marks INT,
    result_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Insert values
INSERT INTO students VALUES
(1, 'Ananya', '2024-09-01'),
(2, 'Ravi', '2024-10-15'),
(3, 'Meera', '2025-01-10'),
(4, 'Arjun', '2025-02-20');

INSERT INTO courses VALUES
(1, 'Computer Science'),
(2, 'Physics');

INSERT INTO subjects VALUES
(1, 'Data Structures', 1),
(2, 'DBMS', 1),
(3, 'Quantum Mechanics', 2);

INSERT INTO results VALUES
(1, 1, 1, 'Midterm', 80, '2025-03-01'),
(2, 1, 2, 'Midterm', 70, '2025-03-01'),
(3, 2, 1, 'Midterm', 60, '2025-03-01'),
(4, 3, 1, 'Final', 90, '2025-06-01'),
(5, 3, 2, 'Final', 85, '2025-06-01'),
(6, 4, 3, 'Final', 75, '2025-06-01');

-- Students who scored above the average in their subject
SELECT name, subject_name, marks
FROM students s
JOIN results r ON s.student_id = r.student_id
JOIN subjects sub ON r.subject_id = sub.subject_id
WHERE marks > (
    SELECT AVG(marks)
    FROM results
    WHERE subject_id = r.subject_id
);

-- Average marks per subject (FROM subquery)
SELECT sub.subject_name, avg_result.avg_marks
FROM (
    SELECT subject_id, AVG(marks) AS avg_marks
    FROM results
    GROUP BY subject_id
) AS avg_result
JOIN subjects sub ON sub.subject_id = avg_result.subject_id;

-- Combine two exam results (UNION ALL)
SELECT student_id, subject_id, marks, exam_type FROM results WHERE exam_type = 'Midterm'
UNION ALL
SELECT student_id, subject_id, marks, exam_type FROM results WHERE exam_type = 'Final';

-- Grade students using CASE
SELECT s.name, sub.subject_name, r.marks,
    CASE
        WHEN r.marks >= 90 THEN 'A'
        WHEN r.marks >= 75 THEN 'B'
        WHEN r.marks >= 60 THEN 'C'
        ELSE 'F'
    END AS grade
FROM results r
JOIN students s ON r.student_id = s.student_id
JOIN subjects sub ON r.subject_id = sub.subject_id;

-- JOIN and GROUP BY on course level
SELECT c.course_name, COUNT(r.result_id) AS total_results, AVG(r.marks) AS avg_marks
FROM students s
JOIN results r ON s.student_id = r.student_id
JOIN subjects sub ON r.subject_id = sub.subject_id
JOIN courses c ON sub.course_id = c.course_id
GROUP BY c.course_name;

-- Students enrolled within the last year
SELECT * FROM students
WHERE enrollment_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR);
