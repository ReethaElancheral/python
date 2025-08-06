-- 8. Online Learning Platform 
-- Requirements: 
--  Tables: courses, users, enrollments, completions, instructors 
--  Normalize course and instructor relationships to 3NF. 
--  Index course_id, user_id, and completion_date. 
--  Use EXPLAIN to improve course completion reports. 
--  Subquery to find users who completed more than 3 courses. 
--  Denormalize into a course completion leaderboard table. 
--  Use LIMIT for displaying top 5 trending courses.

CREATE DATABASE IF NOT EXISTS OnlineLearning;
USE OnlineLearning;

-- Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    registration_date DATE
);

-- Instructors Table
CREATE TABLE instructors (
    instructor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    expertise VARCHAR(100)
);

-- Courses Table
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150),
    instructor_id INT,
    category VARCHAR(50),
    FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id)
);

-- Enrollments Table
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Completions Table
CREATE TABLE completions (
    completion_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    course_id INT,
    completion_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Normalize: courses + instructors already separated = 3NF

-- Indexing
CREATE INDEX idx_course_id ON courses(course_id);
CREATE INDEX idx_user_id ON users(user_id);
CREATE INDEX idx_completion_date ON completions(completion_date);

-- EXPLAIN for course completion reports
EXPLAIN SELECT * FROM completions WHERE completion_date >= '2025-01-01';

-- Subquery: Users who completed more than 3 courses
SELECT user_id
FROM completions
GROUP BY user_id
HAVING COUNT(course_id) > 3;

-- Denormalized Leaderboard Table
CREATE TABLE leaderboard (
    user_id INT,
    user_name VARCHAR(100),
    completed_courses INT
);

-- Populate leaderboard
INSERT INTO leaderboard (user_id, user_name, completed_courses)
SELECT u.user_id, u.name, COUNT(c.course_id) AS completed_courses
FROM users u
JOIN completions c ON u.user_id = c.user_id
GROUP BY u.user_id, u.name;

-- Top 5 trending courses (LIMIT + most completions)
SELECT co.title, COUNT(c.course_id) AS completions
FROM completions c
JOIN courses co ON c.course_id = co.course_id
GROUP BY co.course_id
ORDER BY completions DESC
LIMIT 5;
