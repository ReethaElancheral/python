CREATE DATABASE IF NOT EXISTS rideshare_db;
USE rideshare_db;

CREATE TABLE drivers (
    driver_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE riders (
    rider_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE rides (
    ride_id INT AUTO_INCREMENT PRIMARY KEY,
    driver_id INT,
    rider_id INT,
    ride_type ENUM('Shared', 'Premium', 'Economy'),
    duration_minutes INT,
    status ENUM('Completed', 'Cancelled'),
    ride_time TIME,
    city VARCHAR(100),
    ride_date DATE,
    FOREIGN KEY (driver_id) REFERENCES drivers(driver_id),
    FOREIGN KEY (rider_id) REFERENCES riders(rider_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    ride_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (ride_id) REFERENCES rides(ride_id)
);

-- Sample data

INSERT INTO drivers (name, city) VALUES
('Driver A', 'CityX'), ('Driver B', 'CityY'), ('Driver C', 'CityX');

INSERT INTO riders (name, city) VALUES
('Rider 1', 'CityX'), ('Rider 2', 'CityY'), ('Rider 3', 'CityX');

INSERT INTO rides (driver_id, rider_id, ride_type, duration_minutes, status, ride_time, city, ride_date) VALUES
(1, 1, 'Shared', 30, 'Completed', '08:30:00', 'CityX', '2025-07-30'),
(1, 2, 'Premium', 45, 'Completed', '09:15:00', 'CityX', '2025-07-30'),
(2, 2, 'Economy', 20, 'Cancelled', '10:00:00', 'CityY', '2025-07-30'),
(3, 3, 'Shared', 25, 'Completed', '18:45:00', 'CityX', '2025-07-29');

INSERT INTO payments (ride_id, amount, payment_date) VALUES
(1, 100, '2025-07-30'), (2, 150, '2025-07-30'), (4, 80, '2025-07-29');

-- Queries

-- 1. Subquery to find average ride duration per driver
SELECT
    d.driver_id,
    d.name,
    (SELECT AVG(duration_minutes) FROM rides r WHERE r.driver_id = d.driver_id) AS avg_ride_duration
FROM drivers d;

-- 2. Correlated subquery to get rider with most rides per city
SELECT DISTINCT
    city,
    (SELECT rider_id
     FROM rides r2
     WHERE r2.city = r1.city
     GROUP BY rider_id
     ORDER BY COUNT(*) DESC
     LIMIT 1) AS top_rider_id
FROM rides r1;

-- 3. CASE to classify ride types
SELECT
    ride_id,
    ride_type,
    CASE ride_type
        WHEN 'Shared' THEN 'Shared'
        WHEN 'Premium' THEN 'Premium'
        WHEN 'Economy' THEN 'Economy'
        ELSE 'Other'
    END AS ride_category
FROM rides;

-- 4. UNION for completed and cancelled rides
SELECT ride_id, status FROM rides WHERE status = 'Completed'
UNION
SELECT ride_id, status FROM rides WHERE status = 'Cancelled';

-- 5. JOIN + GROUP BY for city-wise earnings
SELECT
    r.city,
    SUM(p.amount) AS total_earnings
FROM rides r
JOIN payments p ON r.ride_id = p.ride_id
GROUP BY r.city;

-- 6. Date range filter for peak hours (e.g., 7 AM to 10 AM)
SELECT *
FROM rides
WHERE TIME(ride_time) BETWEEN '07:00:00' AND '10:00:00';
