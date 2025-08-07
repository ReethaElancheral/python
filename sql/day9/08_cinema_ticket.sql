--  8. Cinema Ticket Sales and Trends 
-- Requirements: 
--  OLTP: bookings, customers, shows, theaters. 
--  Star Schema: fact_bookings, dim_movie, dim_time, dim_customer. 
--  ETL includes timestamp conversion, currency standardization. 
--  Reporting: occupancy rates by movie, genre-based trend analysis. 
--  Compare real-time OLTP check-ins with OLAP historical insights. 

-- Create Database
CREATE DATABASE IF NOT EXISTS CinemaWarehouse;
USE CinemaWarehouse;

-- Dimension Tables

-- Movie dimension
CREATE TABLE dim_movie (
    movie_id INT PRIMARY KEY,
    movie_name VARCHAR(100),
    genre VARCHAR(50),
    duration_minutes INT
);

-- Time dimension
CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    show_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT
);

-- Customer dimension
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    membership_level VARCHAR(20)
);

-- Theater dimension
CREATE TABLE dim_theater (
    theater_id INT PRIMARY KEY,
    theater_name VARCHAR(100),
    city VARCHAR(50)
);

-- Fact Table
CREATE TABLE fact_bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    customer_id INT,
    theater_id INT,
    time_id INT,
    seats_booked INT,
    ticket_price DECIMAL(10,2),
    total_amount DECIMAL(12,2),
    FOREIGN KEY (movie_id) REFERENCES dim_movie(movie_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (theater_id) REFERENCES dim_theater(theater_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);

-- Sample Dimension Data
INSERT INTO dim_movie VALUES
(1,'The Space Odyssey','Sci-Fi',150),
(2,'Romantic Sunset','Romance',120);

INSERT INTO dim_customer VALUES
(1,'Alice','Gold'),
(2,'Bob','Silver');

INSERT INTO dim_time VALUES
(1,'2025-08-01',1,8,3,2025),
(2,'2025-08-02',2,8,3,2025);

INSERT INTO dim_theater VALUES
(1,'CinemaCity Doha','Doha'),
(2,'StarTheater Al Wakrah','Al Wakrah');

-- Sample Fact Data (ETL applied: total_amount = seats * ticket_price)
INSERT INTO fact_bookings (movie_id, customer_id, theater_id, time_id, seats_booked, ticket_price, total_amount)
VALUES
(1,1,1,1,2,50.00,100.00),
(2,2,2,2,3,45.00,135.00),
(1,2,1,2,1,50.00,50.00);

-- OLAP Queries

-- Occupancy rate per movie
SELECT m.movie_name, SUM(f.seats_booked) AS total_seats_sold, COUNT(f.booking_id) AS total_bookings
FROM fact_bookings f
JOIN dim_movie m ON f.movie_id = m.movie_id
GROUP BY m.movie_name
ORDER BY total_seats_sold DESC;

-- Revenue by Genre
SELECT m.genre, SUM(f.total_amount) AS total_revenue
FROM fact_bookings f
JOIN dim_movie m ON f.movie_id = m.movie_id
GROUP BY m.genre
ORDER BY total_revenue DESC;

-- Customer Booking Trends
SELECT c.membership_level, COUNT(f.booking_id) AS total_bookings, SUM(f.total_amount) AS total_spent
FROM fact_bookings f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.membership_level
ORDER BY total_spent DESC;

-- Daily Booking Summary
SELECT t.show_date, COUNT(f.booking_id) AS total_bookings, SUM(f.total_amount) AS total_revenue
FROM fact_bookings f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.show_date
ORDER BY t.show_date;

-- Compare OLTP real-time check-ins vs OLAP historical sales
-- Example: OLTP query (real-time)
-- SELECT * FROM bookings WHERE show_time = '2025-08-01 20:00:00';
-- OLAP query aggregates allow trend insights by movie/genre/date
