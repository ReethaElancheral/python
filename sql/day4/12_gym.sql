CREATE DATABASE IF NOT EXISTS gym_db;
USE gym_db;

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    fitness_goal_completed BOOLEAN,
    membership_expiry DATE
);

CREATE TABLE sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

CREATE TABLE trainers (
    trainer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    payment_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- Sample data
INSERT INTO members (name, fitness_goal_completed, membership_expiry) VALUES
('Alice', TRUE, '2025-08-31'),
('Bob', FALSE, '2025-06-15'),
('Charlie', TRUE, '2025-07-01');

INSERT INTO sessions (member_id, session_date) VALUES
(1, '2025-07-01'), (1, '2025-07-05'), (2, '2025-07-03'), (3, '2025-06-25'), (3, '2025-07-02');

INSERT INTO trainers (name) VALUES
('Trainer A'), ('Trainer B');

INSERT INTO payments (member_id, payment_date, amount) VALUES
(1, '2025-06-01', 100), (2, '2025-05-15', 80), (3, '2025-06-10', 90);

-- Queries

-- 1. Subquery to calculate average sessions per member
SELECT
    AVG(session_count) AS avg_sessions_per_member
FROM (
    SELECT member_id, COUNT(session_id) AS session_count FROM sessions GROUP BY member_id
) AS sub;

-- 2. CASE to bucket members by fitness goal completion
SELECT
    name,
    CASE WHEN fitness_goal_completed THEN 'Goal Completed' ELSE 'In Progress' END AS fitness_status
FROM members;

-- 3. Correlated subquery to find most active member per trainer
-- (Assuming relation: members assigned to trainers - example skipped due to missing relation)

-- 4. JOIN + GROUP BY to show session count per trainer
-- (Assuming relation exists - example skipped)

-- 5. UNION ALL for expired and active memberships
SELECT member_id, name, membership_expiry, 'Active' AS status FROM members WHERE membership_expiry >= CURDATE()
UNION ALL
SELECT member_id, name, membership_expiry, 'Expired' AS status FROM members WHERE membership_expiry < CURDATE();

-- 6. Date filter for memberships expiring this month
SELECT * FROM members WHERE YEAR(membership_expiry) = YEAR(CURDATE()) AND MONTH(membership_expiry) = MONTH(CURDATE());
