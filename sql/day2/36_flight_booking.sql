
CREATE DATABASE IF NOT EXISTS FlightDB;
USE FlightDB;

-- Airlines table
CREATE TABLE airlines (
    airline_id INT PRIMARY KEY,
    airline_name VARCHAR(100)
);

-- Flights table
CREATE TABLE flights (
    flight_id INT PRIMARY KEY,
    airline_id INT,
    route VARCHAR(100),
    capacity INT,
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id)
);

-- Passengers table
CREATE TABLE passengers (
    passenger_id INT PRIMARY KEY,
    passenger_name VARCHAR(100)
);

-- Bookings table
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    flight_id INT,
    passenger_id INT,
    seats_booked INT,
    booking_date DATE,
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id),
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id)
);

-- Sample Data
INSERT INTO airlines VALUES 
(1, 'Air India'),
(2, 'IndiGo'),
(3, 'SpiceJet');

INSERT INTO flights VALUES 
(101, 1, 'Delhi-Mumbai', 180),
(102, 2, 'Chennai-Bangalore', 150),
(103, 3, 'Mumbai-Kolkata', 200),
(104, 1, 'Delhi-Chennai', 160);

INSERT INTO passengers VALUES 
(201, 'Anjali Sharma'),
(202, 'Raj Verma'),
(203, 'Sneha Rao'),
(204, 'Karan Mehta');

INSERT INTO bookings VALUES 
(301, 101, 201, 2, '2025-07-01'),
(302, 101, 202, 1, '2025-07-01'),
(303, 102, 201, 3, '2025-07-02'),
(304, 103, 203, 2, '2025-07-03'),
(305, 104, 204, 2, '2025-07-04'),
(306, 101, 203, 1, '2025-07-05'),
(307, 102, 204, 2, '2025-07-06'),
(308, 103, 202, 1, '2025-07-07');

-- 1. Total bookings per airline
SELECT a.airline_name, COUNT(b.booking_id) AS total_bookings
FROM bookings b
JOIN flights f ON b.flight_id = f.flight_id
JOIN airlines a ON f.airline_id = a.airline_id
GROUP BY a.airline_id;

-- 2. Most frequent flyers
SELECT p.passenger_name, COUNT(b.booking_id) AS total_flights
FROM bookings b
JOIN passengers p ON b.passenger_id = p.passenger_id
GROUP BY p.passenger_id
ORDER BY total_flights DESC;

-- 3. Flights with avg occupancy > 80%
SELECT f.flight_id, f.route, 
       (SUM(b.seats_booked) / f.capacity) * 100 AS avg_occupancy_pct
FROM bookings b
JOIN flights f ON b.flight_id = f.flight_id
GROUP BY f.flight_id, f.capacity
HAVING avg_occupancy_pct > 80;

-- 4. INNER JOIN: bookings ↔ flights ↔ passengers
SELECT b.booking_id, f.route, p.passenger_name, b.seats_booked
FROM bookings b
JOIN flights f ON b.flight_id = f.flight_id
JOIN passengers p ON b.passenger_id = p.passenger_id;

-- 5. RIGHT JOIN: airlines ↔ flights (show all flights, even if no airline details exist)
SELECT a.airline_name, f.flight_id, f.route
FROM airlines a
RIGHT JOIN flights f ON a.airline_id = f.airline_id;

-- 6. SELF JOIN: passengers who flew the same route
SELECT p1.passenger_name AS Passenger1, p2.passenger_name AS Passenger2, f.route
FROM bookings b1
JOIN bookings b2 ON b1.flight_id = b2.flight_id AND b1.passenger_id < b2.passenger_id
JOIN passengers p1 ON b1.passenger_id = p1.passenger_id
JOIN passengers p2 ON b2.passenger_id = p2.passenger_id
JOIN flights f ON b1.flight_id = f.flight_id;
