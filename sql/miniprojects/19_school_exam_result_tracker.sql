-- Project 19: School Exam Result Tracker

CREATE DATABASE IF NOT EXISTS exam_db;
USE exam_db;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(50)
);

CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE marks (
    mark_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject_id INT,
    teacher_id INT,
    marks_obtained INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

INSERT INTO students (name) VALUES 
('Aarav'), ('Diya'), ('Rohan');

INSERT INTO subjects (subject_name) VALUES 
('Math'), ('Science');

INSERT INTO teachers (name) VALUES 
('Mr. Sharma'), ('Mrs. Rao');

INSERT INTO marks (student_id, subject_id, teacher_id, marks_obtained) VALUES 
(1, 1, 1, 88),
(2, 1, 1, 75),
(3, 2, 2, 90),
(1, 2, 2, 85);

-- Average marks
SELECT s.name AS student_name, AVG(m.marks_obtained) AS average_marks
FROM marks m
JOIN students s ON m.student_id = s.student_id
GROUP BY m.student_id;

-- Rank students by subject
SELECT sub.subject_name, stu.name AS student_name, m.marks_obtained
FROM marks m
JOIN students stu ON m.student_id = stu.student_id
JOIN subjects sub ON m.subject_id = sub.subject_id
ORDER BY sub.subject_name, m.marks_obtained DESC;