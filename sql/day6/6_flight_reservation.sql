--  6. Flight Reservation System 
-- Requirements: 
--  Tables: flights, passengers, bookings, airlines, airports 
--  Design in 3NF (airlines and airports in separate tables). 
--  Index flight_date, departure_airport, passenger_id. 
--  Use EXPLAIN on searches by airport and date. 
--  Subquery to find passengers with the most flights. 
--  Create a denormalized table for frequent flyer reporting. 
--  Use LIMIT to display next 5 upcoming flights.

CREATE DATABASE IF NOT EXISTS FlightDB;
USE FlightDB;

-- Airlines
CREATE TABLE airlines (
    airline_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

-- Airports
CREATE TABLE airports (
    airport_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    city VARCHAR(100)
);

-- Flights
CREATE TABLE flights (
    flight_id INT PRIMARY KEY AUTO_INCREMENT,
    airline_id INT,
    departure_airport INT,
    arrival_airport INT,
    flight_date DATE,
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id),
    FOREIGN KEY (departure_airport) REFERENCES airports(airport_id),
    FOREIGN KEY (arrival_airport) REFERENCES airports(airport_id)
);

-- Passengers
CREATE TABLE passengers (
    passenger_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    passport_no VARCHAR(50) UNIQUE
);

-- Bookings
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    passenger_id INT,
    flight_id INT,
    booking_date DATE,
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

-- Indexing
CREATE INDEX idx_flight_date ON flights(flight_date);
CREATE INDEX idx_departure_airport ON flights(departure_airport);
CREATE INDEX idx_passenger_id ON bookings(passenger_id);

-- EXPLAIN for airport + date
EXPLAIN SELECT * FROM flights WHERE departure_airport = 1 AND flight_date = '2025-08-01';

-- Passengers with most flights
SELECT p.name, COUNT(b.booking_id) AS total_flights
FROM passengers p
JOIN bookings b ON p.passenger_id = b.passenger_id
GROUP BY p.passenger_id
ORDER BY total_flights DESC;

-- Denormalized frequent flyer
CREATE TABLE frequent_flyers (
    passenger_id INT,
    total_flights INT
);

-- Next 5 flights
SELECT * FROM flights WHERE flight_date > CURDATE() ORDER BY flight_date ASC LIMIT 5;
