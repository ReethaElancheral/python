-- 9. Movie Streaming Analytics 
-- Requirements: 
--  Tables: movies, genres, users, watch_history, subscriptions 
--  Normalize watch history and genre data. 
--  Index movie_id, user_id, watch_date. 
--  Use EXPLAIN to optimize query showing user watch time. 
--  Subquery for users watching the most movies in a week. 
--  Denormalize monthly user engagement report. 
--  Use LIMIT for top 10 most-watched movies. 

CREATE DATABASE IF NOT EXISTS MovieStreaming;
USE MovieStreaming;

-- Users Table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    subscription_id INT,
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(subscription_id)
);

-- Subscriptions Table
CREATE TABLE subscriptions (
    subscription_id INT PRIMARY KEY AUTO_INCREMENT,
    plan_name VARCHAR(50),
    start_date DATE,
    end_date DATE
);

-- Genres Table
CREATE TABLE genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(50)
);

-- Movies Table
CREATE TABLE movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150),
    genre_id INT,
    duration INT, -- in minutes
    release_year YEAR,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

-- Watch History Table
CREATE TABLE watch_history (
    watch_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    movie_id INT,
    watch_date DATE,
    watch_duration INT, -- in minutes
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);

-- Normalize: genre and watch_history already separated = 3NF

-- Indexing
CREATE INDEX idx_movie_id ON watch_history(movie_id);
CREATE INDEX idx_user_id ON watch_history(user_id);
CREATE INDEX idx_watch_date ON watch_history(watch_date);

-- EXPLAIN for total user watch time query
EXPLAIN SELECT user_id, SUM(watch_duration) AS total_minutes
FROM watch_history
GROUP BY user_id;

-- Subquery: Users who watched the most movies in a week (latest week example)
SELECT user_id, COUNT(*) AS movies_watched
FROM watch_history
WHERE watch_date BETWEEN CURDATE() - INTERVAL 7 DAY AND CURDATE()
GROUP BY user_id
ORDER BY movies_watched DESC
LIMIT 1;

-- Denormalized table: monthly user engagement
CREATE TABLE monthly_engagement (
    user_id INT,
    month_year VARCHAR(7),
    total_watch_time INT
);

-- Populate monthly engagement
INSERT INTO monthly_engagement (user_id, month_year, total_watch_time)
SELECT 
    user_id,
    DATE_FORMAT(watch_date, '%Y-%m') AS month_year,
    SUM(watch_duration)
FROM watch_history
GROUP BY user_id, month_year;

-- Top 10 most-watched movies
SELECT m.title, COUNT(w.watch_id) AS total_views
FROM watch_history w
JOIN movies m ON w.movie_id = m.movie_id
GROUP BY m.movie_id
ORDER BY total_views DESC
LIMIT 10;
