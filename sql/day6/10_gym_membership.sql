--  10. Gym Membership and Attendance 
-- Requirements: 
--  Tables: members, trainers, sessions, payments, plans 
--  Normalize plans and trainer associations. 
--  Index session_date, member_id, trainer_id. 
--  Use EXPLAIN to improve trainer performance reports. 
--  Subquery to identify members with highest attendance. 
--  Denormalize into a trainer-wise session summary. 
--  Use LIMIT to return top 5 most consistent members. 

CREATE DATABASE IF NOT EXISTS GymAttendance;
USE GymAttendance;

-- Members Table
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    join_date DATE,
    plan_id INT,
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id)
);

-- Trainers Table
CREATE TABLE trainers (
    trainer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    specialization VARCHAR(100)
);

-- Plans Table
CREATE TABLE plans (
    plan_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_name VARCHAR(100),
    duration_months INT,
    monthly_fee DECIMAL(10,2)
);

-- Payments Table
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- Sessions Table
CREATE TABLE sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    session_date DATE,
    member_id INT,
    trainer_id INT,
    duration_minutes INT,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id)
);

-- Normalize: plans and trainer associations are separated (3NF)

-- Indexing for optimization
CREATE INDEX idx_session_date ON sessions(session_date);
CREATE INDEX idx_member_id ON sessions(member_id);
CREATE INDEX idx_trainer_id ON sessions(trainer_id);

-- EXPLAIN: optimize trainer performance report
EXPLAIN
SELECT trainer_id, COUNT(*) AS total_sessions, SUM(duration_minutes) AS total_minutes
FROM sessions
GROUP BY trainer_id;

-- Subquery: Identify members with the highest attendance
SELECT member_id, COUNT(*) AS total_sessions
FROM sessions
GROUP BY member_id
ORDER BY total_sessions DESC
LIMIT 1;

-- Denormalized summary: Trainer-wise session summary
CREATE TABLE trainer_session_summary (
    trainer_id INT,
    trainer_name VARCHAR(100),
    total_sessions INT,
    total_minutes INT
);

-- Populate summary table
INSERT INTO trainer_session_summary (trainer_id, trainer_name, total_sessions, total_minutes)
SELECT 
    t.trainer_id,
    t.name,
    COUNT(s.session_id) AS total_sessions,
    SUM(s.duration_minutes) AS total_minutes
FROM trainers t
LEFT JOIN sessions s ON t.trainer_id = s.trainer_id
GROUP BY t.trainer_id, t.name;

-- LIMIT to return top 5 most consistent members (by sessions)
SELECT m.name, COUNT(s.session_id) AS attendance_count
FROM members m
JOIN sessions s ON m.member_id = s.member_id
GROUP BY m.member_id
ORDER BY attendance_count DESC
LIMIT 5;
