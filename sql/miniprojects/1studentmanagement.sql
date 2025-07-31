CREATE DATABASE school_db;
USE school_db;

CREATE TABLE students(
student_id INT PRIMARY KEY auto_increment,
name VARCHAR(100),
age INT,
email VARCHAR(100)
);

CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    subject VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);



INSERT INTO students (name, age, email) VALUES
('Aditi Sharma', 15, 'aditi@gmail.com'),
('Rohan Mehta', 14, 'rohan@gmail.com'),
('Simran Kaur', 16, 'simran@gmail.com'),
('Aman Joshi', 15, 'aman@gmail.com'),
('Nisha Reetha', 17, 'nisha@gmail.com'),
('Karan Patel', 16, 'karan@gmail.com'),
('Priya Sen', 14, 'priya@gmail.com'),
('Deepak Reddy', 15, 'deepak@gmail.com'),
('Neha Desai', 16, 'neha@gmail.com'),
('Rahul Gupta', 14, 'rahul@gmail.com');

INSERT INTO teachers (name, subject) VALUES
('Dr. Suresh', 'Math'),
('Ms. Anita', 'Science'),
('Mr. Rajeev', 'History'),
('Mrs. Nair', 'English');


INSERT INTO courses (course_name, teacher_id) VALUES
('Algebra', 1),
('Physics', 2),
('World History', 3),
('Literature', 4),
('Geometry', 1);

INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1), (1, 2),
(2, 1), (2, 3),
(3, 2), (3, 4),
(4, 3),
(5, 1), (5, 4),
(6, 2), (6, 5),
(7, 5),
(8, 2),
(9, 3),
(10, 1);

INSERT INTO students (name, age, email) VALUES ('Meera Nair', 15, 'meera@gmail.com');

INSERT INTO enrollments (student_id, course_id) VALUES (11, 2);

UPDATE teachers SET subject = 'Advanced History' WHERE teacher_id = 3;

DELETE FROM students WHERE student_id = 11;

-- List Students Per Course
SELECT c.course_name, s.name AS student_name
FROM enrollments e
JOIN students s ON e.student_id = s.student_id
JOIN courses c ON e.course_id = c.course_id
ORDER BY c.course_name;

-- Count Students by Course
SELECT c.course_name, COUNT(e.student_id) AS total_students
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- Students With No Enrollments
SELECT s.name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.enrollment_id IS NULL;

-- select * from students;
-- select * from enrollments;

