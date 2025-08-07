--  6. Airline Booking and Delay Insights 
-- Requirements: 
--  OLTP for bookings, flights, customers. 
--  Warehouse: Star Schema with fact_flights, dim_route, dim_aircraft. 
--  ETL includes delay calculation and flight duration. 
--  OLAP reports on average delays by route, carrier ranking. 
--  Compare OLTP system used for check-in vs warehouse used for analytics. 

-- Create Database
CREATE DATABASE IF NOT EXISTS AirlineWarehouse;
USE AirlineWarehouse;

-- Dimension Tables

-- Time dimension
CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    flight_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT
);

-- Route dimension
CREATE TABLE dim_route (
    route_id INT PRIMARY KEY,
    departure_airport VARCHAR(50),
    arrival_airport VARCHAR(50),
    distance_km INT
);

-- Aircraft dimension
CREATE TABLE dim_aircraft (
    aircraft_id INT PRIMARY KEY,
    aircraft_type VARCHAR(50),
    carrier_name VARCHAR(100)
);

-- Customer dimension
CREATE TABLE dim_customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    frequent_flyer_status VARCHAR(20)
);

-- Fact Table
CREATE TABLE fact_flights (
    flight_id INT PRIMARY KEY AUTO_INCREMENT,
    time_id INT,
    route_id INT,
    aircraft_id INT,
    customer_id INT,
    scheduled_departure TIME,
    actual_departure TIME,
    scheduled_arrival TIME,
    actual_arrival TIME,
    flight_duration_minutes INT,
    delay_minutes INT,
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (route_id) REFERENCES dim_route(route_id),
    FOREIGN KEY (aircraft_id) REFERENCES dim_aircraft(aircraft_id),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id)
);

-- Sample Dimension Data
INSERT INTO dim_time VALUES
(1,'2025-08-01',1,8,3,2025),
(2,'2025-08-02',2,8,3,2025);

INSERT INTO dim_route VALUES
(1,'Doha','London',6700),
(2,'Doha','Paris',5200);

INSERT INTO dim_aircraft VALUES
(1,'Boeing 777','Qatar Airways'),
(2,'Airbus A350','Qatar Airways');

INSERT INTO dim_customer VALUES
(1,'Alice','Gold'),
(2,'Bob','Silver');

-- Sample Fact Data (after ETL, delay calculation)
INSERT INTO fact_flights (time_id, route_id, aircraft_id, customer_id, scheduled_departure, actual_departure, scheduled_arrival, actual_arrival, flight_duration_minutes, delay_minutes)
VALUES
(1,1,1,1,'08:00:00','08:15:00','12:00:00','12:10:00',250,10),
(1,2,2,2,'09:00:00','09:05:00','13:00:00','13:20:00',240,20),
(2,1,1,2,'14:00:00','14:10:00','18:00:00','18:15:00',240,15);

-- OLAP Queries

-- Average Delay by Route
SELECT r.departure_airport, r.arrival_airport, AVG(f.delay_minutes) AS avg_delay
FROM fact_flights f
JOIN dim_route r ON f.route_id = r.route_id
GROUP BY r.departure_airport, r.arrival_airport
ORDER BY avg_delay DESC;

-- Carrier Ranking by Average Delay
SELECT a.carrier_name, AVG(f.delay_minutes) AS avg_delay
FROM fact_flights f
JOIN dim_aircraft a ON f.aircraft_id = a.aircraft_id
GROUP BY a.carrier_name
ORDER BY avg_delay ASC;

-- Flights per Customer (frequent flyer insights)
SELECT c.customer_name, COUNT(f.flight_id) AS total_flights, AVG(f.delay_minutes) AS avg_delay
FROM fact_flights f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.customer_name
ORDER BY total_flights DESC;

-- Daily Flight Summary
SELECT t.flight_date, COUNT(f.flight_id) AS total_flights, AVG(f.delay_minutes) AS avg_daily_delay
FROM fact_flights f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.flight_date
ORDER BY t.flight_date;

-- OLAP vs OLTP comparison:
-- OLTP table: bookings
-- SELECT flight_id, customer_id, scheduled_departure, actual_departure,
-- TIMESTAMPDIFF(MINUTE, scheduled_departure, actual_departure) AS delay_minutes
-- FROM bookings;
-- Fact table aggregates allow faster delay analytics per route, carrier, day.
