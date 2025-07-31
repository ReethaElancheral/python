CREATE DATABASE gym_db;
USE gym_db;

CREATE TABLE plans (
  plan_id INT AUTO_INCREMENT PRIMARY KEY,
  plan_name VARCHAR(50) NOT NULL UNIQUE,
  duration_months INT NOT NULL,
  price DECIMAL(10,2) NOT NULL
);

CREATE TABLE trainers (
  trainer_id INT AUTO_INCREMENT PRIMARY KEY,
  trainer_name VARCHAR(100) NOT NULL,
  specialty VARCHAR(100)
);

CREATE TABLE members (
  member_id INT AUTO_INCREMENT PRIMARY KEY,
  member_name VARCHAR(100) NOT NULL,
  trainer_id INT,
  FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id)
);

CREATE TABLE subscriptions (
  sub_id INT AUTO_INCREMENT PRIMARY KEY,
  member_id INT,
  plan_id INT,
  start_date DATE,
  end_date DATE,
  FOREIGN KEY (member_id) REFERENCES members(member_id),
  FOREIGN KEY (plan_id) REFERENCES plans(plan_id)
);

INSERT INTO plans (plan_name, duration_months, price) VALUES
('Basic', 1, 1200.00),
('Standard', 3, 3000.00),
('Premium', 6, 5500.00),
('Annual', 12, 10000.00),
('Flexi', 2, 2000.00);

INSERT INTO trainers (trainer_name, specialty) VALUES
('Ravi Kumar', 'Weight Loss'),
('Anjali Mehra', 'Strength Training'),
('Vikas Sharma', 'Cardio');

INSERT INTO members (member_name, trainer_id) VALUES
('Aman Verma', 1),
('Bhavna Singh', 2),
('Chetan Kumar', 3),
('Diksha Rao', 1),
('Eshan Patil', 2),
('Farah Khan', 3),
('Gaurav Shah', 1),
('Heena Bhatia', 2),
('Ishaan Sinha', 3),
('Jaya Pandey', 1);

SELECT * FROM members WHERE member_id IN (1,2,3,4,5,6,7,8,9,10);
SELECT * FROM plans WHERE plan_id IN (1,2,3,4,5);
-- SET FOREIGN_KEY_CHECKS = 0;

INSERT INTO subscriptions (member_id, plan_id, start_date, end_date) VALUES
(1, 1, '2025-07-01', '2025-07-31'),
(2, 2, '2025-06-01', '2025-08-31'),
(3, 3, '2025-01-01', '2025-06-30');

-- SET FOREIGN_KEY_CHECKS = 1;

-- Update a Member’s Plan
UPDATE subscriptions
SET plan_id = 3, start_date = '2025-08-01', end_date = '2026-01-31'
WHERE member_id = 1;

--  Delete Expired Subscriptions

DELETE FROM subscriptions
WHERE end_date < '2025-07-30';

-- List all active members and their plan
SELECT m.member_name, p.plan_name, s.start_date, s.end_date
FROM subscriptions s
JOIN members m ON s.member_id = m.member_id
JOIN plans p ON s.plan_id = p.plan_id
WHERE s.end_date >= CURDATE();

-- Show member with trainer and plan
SELECT m.member_name, t.trainer_name, p.plan_name
FROM members m
JOIN trainers t ON m.trainer_id = t.trainer_id
JOIN subscriptions s ON m.member_id = s.member_id
JOIN plans p ON s.plan_id = p.plan_id;

-- Count members on each plan
SELECT p.plan_name, COUNT(s.member_id) AS total_members
FROM plans p
LEFT JOIN subscriptions s ON p.plan_id = s.plan_id
GROUP BY p.plan_id;

