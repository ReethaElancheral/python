-- Project 7: Movie Streaming Platform Analytics

CREATE DATABASE IF NOT EXISTS streaming_db;
USE streaming_db;

-- Tables

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(100),
    subscription_plan VARCHAR(50)
);

CREATE TABLE subscriptions (
    sub_id INT PRIMARY KEY,
    plan_name VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50)
);

CREATE TABLE views (
    view_id INT PRIMARY KEY,
    user_id INT,
    movie_id INT,
    watch_time INT, -- in minutes
    view_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

-- Sample Data

INSERT INTO users (user_id, name, subscription_plan) VALUES
(1, 'Aisha', 'Premium'),
(2, 'Ravi', 'Standard'),
(3, 'Lina', 'Basic'),
(4, 'Tom', 'Premium');

INSERT INTO subscriptions (sub_id, plan_name, price) VALUES
(1, 'Basic', 199.00),
(2, 'Standard', 399.00),
(3, 'Premium', 599.00);

INSERT INTO movies (movie_id, title, genre) VALUES
(1, 'Sky High', 'Action'),
(2, 'Love Bloom', 'Romance'),
(3, 'The Chef', 'Drama'),
(4, 'Fast Wheels', 'Action');

INSERT INTO views (view_id, user_id, movie_id, watch_time, view_date) VALUES
(1, 1, 1, 120, '2025-07-01'),
(2, 1, 2, 90, '2025-07-02'),
(3, 2, 1, 110, '2025-07-03'),
(4, 2, 3, 60, '2025-07-03'),
(5, 3, 4, 130, '2025-07-04'),
(6, 4, 1, 100, '2025-07-05'),
(7, 4, 2, 85, '2025-07-06'),
(8, 1, 1, 140, '2025-07-07'),
(9, 2, 1, 100, '2025-07-08'),
(10, 3, 1, 95, '2025-07-08'),
(11, 1, 1, 150, '2025-07-09'),
(12, 4, 1, 105, '2025-07-10');

-- Queries

-- 1. Total views per movie
SELECT 
    m.title,
    COUNT(v.view_id) AS total_views
FROM movies m
JOIN views v ON m.movie_id = v.movie_id
GROUP BY m.movie_id, m.title;

-- 2. Average watch time per genre
SELECT 
    m.genre,
    AVG(v.watch_time) AS avg_watch_time
FROM movies m
JOIN views v ON m.movie_id = v.movie_id
GROUP BY m.genre;

-- 3. Movies with more than 500 views (HAVING)
-- (adjusted logic for current dataset to > 4 for demonstration)
SELECT 
    m.title,
    COUNT(v.view_id) AS total_views
FROM movies m
JOIN views v ON m.movie_id = v.movie_id
GROUP BY m.movie_id, m.title
HAVING total_views > 4;

-- 4. INNER JOIN views and movies
SELECT 
    v.view_id,
    u.name AS user_name,
    m.title AS movie_title,
    v.watch_time,
    v.view_date
FROM views v
INNER JOIN movies m ON v.movie_id = m.movie_id
INNER JOIN users u ON v.user_id = u.user_id;

-- 5. LEFT JOIN: users and subscriptions
SELECT 
    u.name,
    u.subscription_plan,
    s.price
FROM users u
LEFT JOIN subscriptions s ON u.subscription_plan = s.plan_name;

-- 6. SELF JOIN on users to find friends with the same subscription plan
SELECT 
    u1.name AS user1,
    u2.name AS user2,
    u1.subscription_plan
FROM users u1
JOIN users u2 ON u1.subscription_plan = u2.subscription_plan AND u1.user_id < u2.user_id;
