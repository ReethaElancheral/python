--  4. University Student Performance Warehouse 
-- Requirements: 
--  OLTP: students, grades, subjects, exams. 
--  Star Schema: fact_scores, dim_student, dim_subject, dim_time. 
--  ETL transforms inconsistent grading formats. 
--  Reports: average score by semester, subject-wise failure rate. 
--  Use OLAP to slice/dice performance by department, batch. 

-- Create Database
CREATE DATABASE IF NOT EXISTS UniversityWarehouse;
USE UniversityWarehouse;

-- Dimension Tables
CREATE TABLE dim_student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    department VARCHAR(50),
    batch_year INT
);

CREATE TABLE dim_subject (
    subject_id INT PRIMARY KEY,
    subject_name VARCHAR(100),
    department VARCHAR(50)
);

CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    exam_date DATE,
    semester VARCHAR(10),
    year INT
);

-- Fact Table
CREATE TABLE fact_scores (
    score_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject_id INT,
    time_id INT,
    marks DECIMAL(5,2),
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES dim_student(student_id),
    FOREIGN KEY (subject_id) REFERENCES dim_subject(subject_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);

-- Sample Dimension Data
INSERT INTO dim_student VALUES
(1,'Alice','Computer Science',2023),
(2,'Bob','Computer Science',2023),
(3,'Charlie','Electronics',2022);

INSERT INTO dim_subject VALUES
(1,'Data Structures','Computer Science'),
(2,'Algorithms','Computer Science'),
(3,'Digital Circuits','Electronics');

INSERT INTO dim_time VALUES
(1,'2025-05-10','Semester 1',2025),
(2,'2025-12-15','Semester 2',2025);

-- Sample Fact Data (after ETL normalizing grades)
INSERT INTO fact_scores (student_id, subject_id, time_id, marks, grade)
VALUES
(1,1,1,85,'A'),
(1,2,1,78,'B'),
(2,1,1,92,'A'),
(2,2,1,88,'A'),
(3,3,1,65,'C');

-- OLAP Queries

-- Average Score by Semester
SELECT t.semester, AVG(f.marks) AS avg_marks
FROM fact_scores f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.semester;

-- Subject-wise Failure Rate (marks < 40)
SELECT s.subject_name,
       COUNT(CASE WHEN f.marks < 40 THEN 1 END) AS failures,
       COUNT(*) AS total_students,
       (COUNT(CASE WHEN f.marks < 40 THEN 1 END)/COUNT(*))*100 AS failure_percentage
FROM fact_scores f
JOIN dim_subject s ON f.subject_id = s.subject_id
GROUP BY s.subject_name;

-- Department-wise Average Marks (OLAP slice/dice)
SELECT st.department, t.semester, AVG(f.marks) AS avg_marks
FROM fact_scores f
JOIN dim_student st ON f.student_id = st.student_id
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY st.department, t.semester;

-- Top 5 Students per Batch (using window function)
SELECT student_id, student_name, batch_year, AVG(marks) AS avg_marks,
       RANK() OVER (PARTITION BY batch_year ORDER BY AVG(marks) DESC) AS rank_in_batch
FROM fact_scores f
JOIN dim_student s ON f.student_id = s.student_id
GROUP BY student_id, student_name, batch_year
HAVING rank_in_batch <= 5
ORDER BY batch_year, rank_in_batch;
