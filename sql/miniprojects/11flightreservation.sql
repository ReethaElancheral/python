-- -----------------------------------------------
-- Project 11: Flight Reservation System
-- Requirements:
-- • Create airline_db
-- • Tables: flights, passengers, bookings, airports
-- • Insert 5 flights, 10 passengers, and link them with bookings
-- • Queries:
--    - List all flights between two airports
--    - Passenger manifest for a flight
-- -----------------------------------------------

CREATE DATABASE IF NOT EXISTS airline_db;
USE airline_db;

-- Create airports table
CREATE TABLE airports (
    airport_id INT PRIMARY KEY AUTO_INCREMENT,
    airport_code VARCHAR(10) UNIQUE NOT NULL,
    airport_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL
);

-- Create flights table
CREATE TABLE flights (
    flight_id INT PRIMARY KEY AUTO_INCREMENT,
    flight_number VARCHAR(20) NOT NULL UNIQUE,
    departure_airport_id INT,
    arrival_airport_id INT,
    departure_time DATETIME,
    arrival_time DATETIME,
    FOREIGN KEY (departure_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (arrival_airport_id) REFERENCES airports(airport_id)
);

-- Create passengers table
CREATE TABLE passengers (
    passenger_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create bookings table
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    passenger_id INT,
    flight_id INT,
    seat_number VARCHAR(10),
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

-- Insert airports
INSERT INTO airports (airport_code, airport_name, city) VALUES
('JFK', 'John F. Kennedy International Airport', 'New York'),
('LAX', 'Los Angeles International Airport', 'Los Angeles'),
('ORD', 'O\'Hare International Airport', 'Chicago'),
('ATL', 'Hartsfield-Jackson Atlanta International Airport', 'Atlanta'),
('DFW', 'Dallas/Fort Worth International Airport', 'Dallas');

-- Insert flights
INSERT INTO flights (flight_number, departure_airport_id, arrival_airport_id, departure_time, arrival_time) VALUES
('AA101', 1, 2, '2025-08-01 08:00:00', '2025-08-01 11:00:00'),
('UA202', 2, 3, '2025-08-01 09:30:00', '2025-08-01 13:30:00'),
('DL303', 3, 4, '2025-08-02 07:45:00', '2025-08-02 10:45:00'),
('SW404', 4, 5, '2025-08-02 14:00:00', '2025-08-02 16:30:00'),
('AA505', 1, 5, '2025-08-03 06:00:00', '2025-08-03 09:00:00');

-- Insert passengers
INSERT INTO passengers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com'),
('Eva', 'eva@example.com'),
('Frank', 'frank@example.com'),
('Grace', 'grace@example.com'),
('Hannah', 'hannah@example.com'),
('Ian', 'ian@example.com'),
('Jane', 'jane@example.com');

-- Insert bookings (link passengers with flights)
INSERT INTO bookings (passenger_id, flight_id, seat_number) VALUES
(1, 1, '12A'),
(2, 1, '12B'),
(3, 2, '14C'),
(4, 2, '14D'),
(5, 3, '10A'),
(6, 3, '10B'),
(7, 4, '16A'),
(8, 4, '16B'),
(9, 5, '18A'),
(10, 5, '18B');



-- 1. List all flights between two airports (e.g., JFK to LAX)
SELECT 
    f.flight_number,
    dep.airport_name AS departure_airport,
    arr.airport_name AS arrival_airport,
    f.departure_time,
    f.arrival_time
FROM flights f
JOIN airports dep ON f.departure_airport_id = dep.airport_id
JOIN airports arr ON f.arrival_airport_id = arr.airport_id
WHERE dep.airport_code = 'JFK' AND arr.airport_code = 'LAX';

-- 2. Passenger manifest for a flight (e.g., flight_number = 'AA101')
SELECT 
    p.name AS passenger_name,
    p.email,
    b.seat_number
FROM bookings b
JOIN passengers p ON b.passenger_id = p.passenger_id
JOIN flights f ON b.flight_id = f.flight_id
WHERE f.flight_number = 'AA101';
