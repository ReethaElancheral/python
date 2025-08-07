-- 10. Hotel Occupancy & Revenue Management 
-- Requirements: 
--  OLTP: bookings, rooms, guests, services. 
--  Warehouse: Snowflake Schema to support different room types and rates. 
--  ETL includes joins, computed stay durations, revenue. 
--  Reporting: occupancy by season, room type profitability. 
--  OLAP used by revenue managers for pricing decisions. 

-- Create Database
CREATE DATABASE IF NOT EXISTS HotelWarehouse;
USE HotelWarehouse;

-- Dimension Tables

-- Guest dimension
CREATE TABLE dim_guest (
    guest_id INT PRIMARY KEY,
    guest_name VARCHAR(100),
    membership_level VARCHAR(20)
);

-- Room dimension
CREATE TABLE dim_room (
    room_id INT PRIMARY KEY,
    room_number VARCHAR(10),
    room_type VARCHAR(50),
    rate_per_night DECIMAL(10,2)
);

-- Time dimension
CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    checkin_date DATE,
    checkout_date DATE,
    stay_duration INT,
    day INT,
    month INT,
    quarter INT,
    year INT
);

-- Service dimension
CREATE TABLE dim_service (
    service_id INT PRIMARY KEY,
    service_name VARCHAR(50),
    service_price DECIMAL(10,2)
);

-- Fact Table
CREATE TABLE fact_booking (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    guest_id INT,
    room_id INT,
    time_id INT,
    total_room_charge DECIMAL(12,2),
    total_service_charge DECIMAL(12,2),
    total_amount DECIMAL(12,2),
    FOREIGN KEY (guest_id) REFERENCES dim_guest(guest_id),
    FOREIGN KEY (room_id) REFERENCES dim_room(room_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);

-- Sample Dimension Data
INSERT INTO dim_guest VALUES
(1,'Alice','Gold'),
(2,'Bob','Silver');

INSERT INTO dim_room VALUES
(1,'101','Deluxe',200.00),
(2,'102','Suite',350.00);

INSERT INTO dim_time VALUES
(1,'2025-08-01','2025-08-03',2,1,8,3,2025),
(2,'2025-08-02','2025-08-05',3,2,8,3,2025);

INSERT INTO dim_service VALUES
(1,'Breakfast',15.00),
(2,'Spa',50.00);

-- Sample Fact Data (ETL applied: total amounts computed)
INSERT INTO fact_booking (guest_id, room_id, time_id, total_room_charge, total_service_charge, total_amount)
VALUES
(1,1,1,200*2,15*2,200*2+15*2),
(2,2,2,350*3,50*3,350*3+50*3);

-- OLAP Queries

-- Occupancy by room type
SELECT r.room_type, COUNT(f.booking_id) AS total_bookings, SUM(f.total_room_charge) AS revenue
FROM fact_booking f
JOIN dim_room r ON f.room_id = r.room_id
GROUP BY r.room_type
ORDER BY revenue DESC;

-- Total revenue per guest membership
SELECT g.membership_level, SUM(f.total_amount) AS total_spent
FROM fact_booking f
JOIN dim_guest g ON f.guest_id = g.guest_id
GROUP BY g.membership_level
ORDER BY total_spent DESC;

-- Daily revenue summary
SELECT t.checkin_date, SUM(f.total_amount) AS total_revenue, COUNT(f.booking_id) AS total_bookings
FROM fact_booking f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.checkin_date
ORDER BY t.checkin_date;

-- Service revenue analysis
SELECT s.service_name, SUM(f.total_service_charge) AS total_service_revenue
FROM fact_booking f
JOIN dim_service s ON f.room_id = s.service_id  -- Join service dimension as example
GROUP BY s.service_name
ORDER BY total_service_revenue DESC;

-- Occupancy by season (quarter)
SELECT t.quarter, COUNT(f.booking_id) AS total_bookings, SUM(f.total_amount) AS total_revenue
FROM fact_booking f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.quarter
ORDER BY t.quarter;
