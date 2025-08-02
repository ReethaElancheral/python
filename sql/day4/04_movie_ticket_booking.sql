-- Project 4: Movie Ticket Booking Analytics

CREATE DATABASE IF NOT EXISTS MovieAnalyticsDB;
USE MovieAnalyticsDB;

-- Create tables
CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50),
    release_year INT
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE theatres (
    theatre_id INT PRIMARY KEY,
    theatre_name VARCHAR(100),
    location VARCHAR(100)
);

CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    customer_id INT,
    movie_id INT,
    theatre_id INT,
    booking_time DATETIME,
    tickets INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (theatre_id) REFERENCES theatres(theatre_id)
);

-- Insert sample data
INSERT INTO movies VALUES
(1, 'Avengers', 'Action', 2019),
(2, 'Batman', 'Action', 2021),
(3, 'Interstellar', 'Sci-Fi', 2014),
(4, 'Joker', 'Drama', 2019);

INSERT INTO customers VALUES
(1, 'Amit', 'amit@mail.com'),
(2, 'Sara', 'sara@mail.com'),
(3, 'Karan', 'karan@mail.com');

INSERT INTO theatres VALUES
(1, 'PVR Cinemas', 'Mumbai'),
(2, 'INOX', 'Delhi');

INSERT INTO bookings VALUES
(1, 1, 1, 1, '2025-07-20 10:00:00', 2),
(2, 2, 2, 2, '2025-07-20 15:00:00', 3),
(3, 3, 1, 1, '2025-07-21 18:00:00', 1),
(4, 1, 2, 2, '2025-07-22 21:00:00', 4),
(5, 2, 3, 1, '2025-07-23 11:00:00', 2),
(6, 3, 4, 2, '2025-07-24 17:00:00', 1);

-- Subquery: movies with bookings above average
SELECT m.title, COUNT(b.booking_id) AS total_bookings
FROM bookings b
JOIN movies m ON b.movie_id = m.movie_id
GROUP BY m.movie_id, m.title
HAVING COUNT(b.booking_id) > (
    SELECT AVG(total_count)
    FROM (
        SELECT COUNT(*) AS total_count
        FROM bookings
        GROUP BY movie_id
    ) AS sub
);

-- JOIN bookings ↔ movies ↔ customers
SELECT b.booking_id, c.name AS customer, m.title AS movie, b.booking_time, b.tickets
FROM bookings b
JOIN customers c ON b.customer_id = c.customer_id
JOIN movies m ON b.movie_id = m.movie_id;

-- CASE to classify booking time
SELECT booking_id, booking_time,
    CASE
        WHEN HOUR(booking_time) BETWEEN 6 AND 11 THEN 'Morning'
        WHEN HOUR(booking_time) BETWEEN 12 AND 17 THEN 'Afternoon'
        WHEN HOUR(booking_time) BETWEEN 18 AND 23 THEN 'Evening'
        ELSE 'Late Night'
    END AS booking_period
FROM bookings;

-- INTERSECT: customers who watched both Avengers and Batman
SELECT customer_id FROM bookings WHERE movie_id = 1
INTERSECT
SELECT customer_id FROM bookings WHERE movie_id = 2;

-- UNION ALL: weekend and weekday ticket sales
SELECT * FROM bookings
WHERE DAYOFWEEK(booking_time) IN (1, 7) -- Sunday (1), Saturday (7)
UNION ALL
SELECT * FROM bookings
WHERE DAYOFWEEK(booking_time) BETWEEN 2 AND 6;

-- Correlated subquery: top customer per theatre
SELECT c.name, t.theatre_name
FROM customers c
JOIN bookings b ON c.customer_id = b.customer_id
JOIN theatres t ON b.theatre_id = t.theatre_id
WHERE c.customer_id = (
    SELECT customer_id
    FROM bookings
    WHERE theatre_id = t.theatre_id
    GROUP BY customer_id
    ORDER BY SUM(tickets) DESC
    LIMIT 1
);
