CREATE DATABASE IF NOT EXISTS university_db;
USE university_db;

-- Tables
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100)
);

CREATE TABLE teachers (
    teacher_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    teacher_id INT,
    grade DECIMAL(5,2),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

-- Insert sample data for students
INSERT INTO students (student_id, name) VALUES
(1, 'Alice'), (2, 'Bob'), (3, 'Charlie'), (4, 'Diana');

-- Insert sample data for courses
INSERT INTO courses (course_id, course_name) VALUES
(1, 'Math'), (2, 'Science'), (3, 'History'), (4, 'Art');

-- Insert sample data for teachers
INSERT INTO teachers (teacher_id, name) VALUES
(1, 'Dr. Smith'), (2, 'Dr. Jones'), (3, 'Dr. Clark');

-- Insert sample data for enrollments
INSERT INTO enrollments (enrollment_id, student_id, course_id, teacher_id, grade) VALUES
(1, 1, 1, 1, 80),
(2, 2, 1, 1, 85),
(3, 3, 2, 2, 70),
(4, 4, 2, 2, 90),
(5, 1, 3, 3, 60),
(6, 2, 3, 3, 65);



-- Count enrollments per course
SELECT c.course_name, COUNT(e.enrollment_id) AS enrollment_count
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- Average grade per course
SELECT c.course_name, AVG(e.grade) AS avg_grade
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- HAVING: courses with avg grade > 75
SELECT c.course_name, AVG(e.grade) AS avg_grade
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
HAVING AVG(e.grade) > 75;

-- INNER JOIN students and their course grades
SELECT s.name AS student_name, c.course_name, e.grade
FROM enrollments e
INNER JOIN students s ON e.student_id = s.student_id
INNER JOIN courses c ON e.course_id = c.course_id;

-- LEFT JOIN to list courses without enrollments
SELECT c.course_name
FROM courses c
LEFT JOIN enrollments e ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;

-- SELF JOIN to show students with same course and grade (peer pairing)
SELECT s1.name AS student1, s2.name AS student2, c.course_name, e1.grade
FROM enrollments e1
INNER JOIN enrollments e2 ON e1.course_id = e2.course_id AND e1.grade = e2.grade AND e1.enrollment_id <> e2.enrollment_id
INNER JOIN students s1 ON e1.student_id = s1.student_id
INNER JOIN students s2 ON e2.student_id = s2.student_id
INNER JOIN courses c ON e1.course_id = c.course_id
ORDER BY c.course_name, e1.grade;
