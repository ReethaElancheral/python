-- Project 14: Fitness Tracker Dashboard

CREATE DATABASE IF NOT EXISTS fitness_tracker_db;
USE fitness_tracker_db;



CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    goal VARCHAR(100)
);

CREATE TABLE trainers (
    trainer_id INT PRIMARY KEY,
    name VARCHAR(100),
    specialty VARCHAR(100)
);

CREATE TABLE workouts (
    workout_id INT PRIMARY KEY,
    user_id INT,
    trainer_id INT,
    session_date DATE,
    calories_burned INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (trainer_id) REFERENCES trainers(trainer_id)
);

CREATE TABLE goals (
    goal_id INT PRIMARY KEY,
    user_id INT,
    goal_description VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);



INSERT INTO users (user_id, name, age, goal) VALUES
(1, 'Amit Sharma', 29, 'Weight Loss'),
(2, 'Neha Verma', 35, 'Muscle Gain'),
(3, 'Ravi Menon', 42, 'Endurance'),
(4, 'Sneha Kapoor', 25, 'Weight Loss');

INSERT INTO trainers (trainer_id, name, specialty) VALUES
(1, 'Raj Malhotra', 'Cardio'),
(2, 'Meena Iyer', 'Strength'),
(3, 'Aditya Singh', 'Yoga');

INSERT INTO workouts (workout_id, user_id, trainer_id, session_date, calories_burned) VALUES
(1, 1, 1, '2024-06-01', 450),
(2, 1, 1, '2024-06-02', 460),
(3, 2, 2, '2024-06-01', 550),
(4, 2, 2, '2024-06-03', 540),
(5, 3, 3, '2024-06-04', 300),
(6, 4, 1, '2024-06-05', 480),
(7, 4, 1, '2024-06-06', 470),
(8, 4, 1, '2024-06-07', 500),
(9, 1, 1, '2024-06-08', 455),
(10, 1, 1, '2024-06-09', 460),
(11, 1, 1, '2024-06-10', 465),
(12, 1, 1, '2024-06-11', 470);

INSERT INTO goals (goal_id, user_id, goal_description) VALUES
(1, 1, 'Lose 10kg'),
(2, 2, 'Gain 5kg muscle'),
(3, 3, 'Run marathon'),
(4, 4, 'Lose 5kg');

-- Queries

-- 1. Average calories burned per workout
SELECT 
    AVG(calories_burned) AS avg_calories_burned
FROM workouts;

-- 2. Users with more than 10 sessions (HAVING)
SELECT 
    u.name,
    COUNT(w.workout_id) AS session_count
FROM users u
JOIN workouts w ON u.user_id = w.user_id
GROUP BY u.user_id, u.name
HAVING session_count > 10;

-- 3. INNER JOIN users ↔ workouts
SELECT 
    u.name AS user_name,
    w.session_date,
    w.calories_burned
FROM users u
INNER JOIN workouts w ON u.user_id = w.user_id;

-- 4. LEFT JOIN: trainers ↔ users (trainers and users they’ve trained)
SELECT 
    t.name AS trainer_name,
    u.name AS user_name
FROM trainers t
LEFT JOIN workouts w ON t.trainer_id = w.trainer_id
LEFT JOIN users u ON w.user_id = u.user_id;

-- 5. SELF JOIN to group users with similar goals
SELECT 
    u1.name AS user1,
    u2.name AS user2,
    u1.goal
FROM users u1
JOIN users u2 ON u1.goal = u2.goal AND u1.user_id < u2.user_id;
