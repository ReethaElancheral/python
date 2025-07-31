-- -----------------------------------------------
-- Project 14: Online Event Registration
-- Requirements:
-- • Create event_portal database
-- • Tables: events, users, registrations
-- • Each user can register for multiple events
-- • SQL to:
--    - Show number of registrations per event
--    - List upcoming events
-- -----------------------------------------------

CREATE DATABASE IF NOT EXISTS event_portal;
USE event_portal;

-- Events table
CREATE TABLE events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,
    event_name VARCHAR(150) NOT NULL,
    event_date DATE NOT NULL,
    location VARCHAR(150)
);

-- Users table
CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Registrations table (many-to-many)
CREATE TABLE registrations (
    registration_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    event_id INT,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (event_id) REFERENCES events(event_id)
);

-- Insert sample events
INSERT INTO events (event_name, event_date, location) VALUES
('Tech Conference 2025', '2025-09-15', 'New York'),
('Music Festival', '2025-10-01', 'Los Angeles'),
('Art Expo', '2025-08-20', 'Chicago'),
('Health Summit', '2025-11-10', 'San Francisco'),
('Book Fair', '2025-07-25', 'Boston');

-- Insert sample users
INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com'),
('Eva', 'eva@example.com');

-- Insert registrations
INSERT INTO registrations (user_id, event_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 3),
(1, 4),
(2, 4),
(3, 5),
(4, 5),
(5, 1);


-- 1. Show number of registrations per event
SELECT 
    e.event_name,
    COUNT(r.registration_id) AS total_registrations
FROM events e
LEFT JOIN registrations r ON e.event_id = r.event_id
GROUP BY e.event_id
ORDER BY total_registrations DESC;

-- 2. List upcoming events (event date >= today)
SELECT 
    event_name,
    event_date,
    location
FROM events
WHERE event_date >= CURDATE()
ORDER BY event_date ASC;
