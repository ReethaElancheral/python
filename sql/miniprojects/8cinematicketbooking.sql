-- -----------------------------------------------
-- Project 9: Cinema Ticket Booking
-- Requirements:
-- • Create cinema_db
-- • Tables: movies, customers, bookings, screens
-- • Track movie showtimes and customer bookings
-- • Insert 5 movies, 3 screens, 8 customers, 15 bookings
-- • Use SQL to:
--     - Get booked seats per show
--     - Find top 3 most watched movies
-- -----------------------------------------------

-- Create the database
CREATE DATABASE IF NOT EXISTS cinema_db;
USE cinema_db;

-- Create movies table
CREATE TABLE movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    duration INT, -- in minutes
    genre VARCHAR(50)
);

-- Create screens table
CREATE TABLE screens (
    screen_id INT PRIMARY KEY AUTO_INCREMENT,
    screen_name VARCHAR(50) NOT NULL
);

-- Create customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Create bookings table
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    movie_id INT,
    screen_id INT,
    show_time DATETIME,
    seat_number VARCHAR(10),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (screen_id) REFERENCES screens(screen_id)
);

-- Insert sample movies
INSERT INTO movies (title, duration, genre) VALUES
('Inception', 148, 'Sci-Fi'),
('The Godfather', 175, 'Crime'),
('Avengers: Endgame', 181, 'Action'),
('Coco', 105, 'Animation'),
('Titanic', 195, 'Romance');

-- Insert sample screens
INSERT INTO screens (screen_name) VALUES
('Screen 1'),
('Screen 2'),
('Screen 3');

-- Insert customers
INSERT INTO customers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com'),
('Eva', 'eva@example.com'),
('Frank', 'frank@example.com'),
('Grace', 'grace@example.com'),
('Hannah', 'hannah@example.com');

-- Insert bookings (15 records with varying movies and screens)
INSERT INTO bookings (customer_id, movie_id, screen_id, show_time, seat_number) VALUES
(1, 1, 1, '2025-08-01 18:00:00', 'A1'),
(2, 1, 1, '2025-08-01 18:00:00', 'A2'),
(3, 2, 2, '2025-08-01 20:00:00', 'B1'),
(4, 3, 3, '2025-08-02 19:00:00', 'C1'),
(5, 3, 3, '2025-08-02 19:00:00', 'C2'),
(6, 3, 3, '2025-08-02 19:00:00', 'C3'),
(7, 4, 2, '2025-08-03 17:00:00', 'B2'),
(8, 5, 1, '2025-08-03 21:00:00', 'A3'),
(1, 1, 1, '2025-08-04 18:00:00', 'A4'),
(2, 3, 3, '2025-08-04 19:00:00', 'C4'),
(3, 2, 2, '2025-08-04 20:00:00', 'B3'),
(4, 5, 1, '2025-08-05 21:00:00', 'A5'),
(5, 3, 3, '2025-08-06 19:00:00', 'C5'),
(6, 3, 3, '2025-08-06 19:00:00', 'C6'),
(7, 4, 2, '2025-08-06 17:00:00', 'B4');


-- 1. Get booked seats per show (grouped by movie, show time)
SELECT 
    m.title AS movie_title,
    b.show_time,
    COUNT(*) AS total_booked_seats
FROM bookings b
JOIN movies m ON b.movie_id = m.movie_id
GROUP BY b.movie_id, b.show_time;

-- 2. Find top 3 most watched movies (by number of bookings)
SELECT 
    m.title AS movie_title,
    COUNT(b.booking_id) AS total_bookings
FROM bookings b
JOIN movies m ON b.movie_id = m.movie_id
GROUP BY m.movie_id
ORDER BY total_bookings DESC
LIMIT 3;
