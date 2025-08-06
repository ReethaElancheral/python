--  6. Gym Member Attendance System 
-- Requirements: 
--  View view_attendance_summary for trainers (hide member contact info). 
--  Procedure log_attendance(member_id, session_id). 
--  Function get_monthly_visits(member_id) to return visit count. 
--  Trigger after_attendance awards points to members. 
--  Create view_active_members as secure interface for public dashboard.

-- Create Database
CREATE DATABASE IF NOT EXISTS GymDB;
USE GymDB;

-- Table: members
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    contact VARCHAR(15),
    join_date DATE,
    points INT DEFAULT 0
);

-- Table: trainers
CREATE TABLE trainers (
    trainer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

-- Table: sessions
CREATE TABLE sessions (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    trainer_id INT,
    session_name VARCHAR(100),
    session_date DATE,
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id)
);

-- Table: attendance
CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    session_id INT,
    attendance_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (session_id) REFERENCES sessions(session_id)
);

-- Sample Data
INSERT INTO members (name, contact, join_date) VALUES
('Anjali Mehra', '9876543210', '2024-01-01'),
('Ramesh Gupta', '9123456789', '2024-02-15');

INSERT INTO trainers (name) VALUES
('Coach Karan'), ('Trainer Priya');

INSERT INTO sessions (trainer_id, session_name, session_date) VALUES
(1, 'Morning Cardio', '2025-08-01'),
(2, 'Strength Training', '2025-08-02');

-- ✅ View: view_attendance_summary (hide contact info)
CREATE OR REPLACE VIEW view_attendance_summary AS
SELECT 
    m.name AS member_name,
    s.session_name,
    s.session_date,
    a.attendance_date
FROM attendance a
JOIN members m ON a.member_id = m.member_id
JOIN sessions s ON a.session_id = s.session_id;

-- ✅ Procedure: log_attendance(member_id, session_id, attendance_date)
DELIMITER //
CREATE PROCEDURE log_attendance(
    IN mem_id INT,
    IN sess_id INT,
    IN att_date DATE
)
BEGIN
    INSERT INTO attendance (member_id, session_id, attendance_date)
    VALUES (mem_id, sess_id, att_date);
END;
//
DELIMITER ;

-- ✅ Function: get_monthly_visits(member_id, month_val)
DELIMITER //
CREATE FUNCTION get_monthly_visits(mem_id INT, month_val INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE visit_count INT;
    SELECT COUNT(*) INTO visit_count
    FROM attendance
    WHERE member_id = mem_id AND MONTH(attendance_date) = month_val;
    RETURN visit_count;
END;
//
DELIMITER ;

-- ✅ Trigger: after_attendance to award points
DELIMITER //
CREATE TRIGGER award_points_after_attendance
AFTER INSERT ON attendance
FOR EACH ROW
BEGIN
    UPDATE members
    SET points = points + 10
    WHERE member_id = NEW.member_id;
END;
//
DELIMITER ;

-- ✅ Public View: view_active_members (hides contact)
CREATE OR REPLACE VIEW view_active_members AS
SELECT 
    member_id,
    name,
    points
FROM members
WHERE points > 0;

-- ✅ Test Examples:
-- CALL log_attendance(1, 1, '2025-08-01');
-- SELECT * FROM view_attendance_summary;
-- SELECT get_monthly_visits(1, 8);
-- SELECT * FROM view_active_members;
