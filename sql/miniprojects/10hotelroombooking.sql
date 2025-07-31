-- -----------------------------------------------
-- Project 10: Hotel Room Booking System
-- Requirements:
-- • Create hotel_db
-- • Tables: rooms, guests, bookings, services
-- • One guest can book multiple rooms, and order services
-- • Insert room types, services, 10 bookings
-- • Queries:
--    - Show booking duration
--    - Calculate total service charges per guest
-- -----------------------------------------------

CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

-- Create rooms table
CREATE TABLE rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    room_type VARCHAR(50) NOT NULL,
    price_per_night DECIMAL(10,2) NOT NULL
);

-- Create guests table
CREATE TABLE guests (
    guest_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create bookings table
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    guest_id INT,
    room_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- Create services table
CREATE TABLE services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    guest_id INT,
    service_name VARCHAR(100) NOT NULL,
    service_charge DECIMAL(10,2) NOT NULL,
    service_date DATE,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id)
);

-- Insert rooms
INSERT INTO rooms (room_number, room_type, price_per_night) VALUES
('101', 'Single', 2000.00),
('102', 'Double', 3500.00),
('103', 'Suite', 7000.00),
('104', 'Single', 2000.00),
('105', 'Double', 3500.00);

-- Insert guests
INSERT INTO guests (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com');

-- Insert bookings (10 bookings)
INSERT INTO bookings (guest_id, room_id, check_in, check_out) VALUES
(1, 1, '2025-07-20', '2025-07-25'),
(1, 2, '2025-07-20', '2025-07-22'),
(2, 3, '2025-07-21', '2025-07-24'),
(3, 4, '2025-07-22', '2025-07-23'),
(3, 5, '2025-07-23', '2025-07-28'),
(4, 1, '2025-07-25', '2025-07-29'),
(4, 2, '2025-07-26', '2025-07-27'),
(2, 4, '2025-07-28', '2025-07-30'),
(1, 3, '2025-07-29', '2025-08-02'),
(3, 5, '2025-07-30', '2025-08-01');

-- Insert services
INSERT INTO services (guest_id, service_name, service_charge, service_date) VALUES
(1, 'Room Service', 500.00, '2025-07-21'),
(1, 'Spa', 1200.00, '2025-07-22'),
(2, 'Laundry', 300.00, '2025-07-23'),
(3, 'Breakfast', 200.00, '2025-07-24'),
(3, 'Dinner', 600.00, '2025-07-25'),
(4, 'Gym', 400.00, '2025-07-26'),
(2, 'Room Service', 450.00, '2025-07-27');

-- -----------------------------------------------
-- Queries
-- -----------------------------------------------

-- 1. Show booking duration (in days) for each booking
SELECT 
    b.booking_id,
    g.name AS guest_name,
    r.room_number,
    b.check_in,
    b.check_out,
    DATEDIFF(b.check_out, b.check_in) AS duration_days
FROM bookings b
JOIN guests g ON b.guest_id = g.guest_id
JOIN rooms r ON b.room_id = r.room_id;

-- 2. Calculate total service charges per guest
SELECT 
    g.name AS guest_name,
    IFNULL(SUM(s.service_charge), 0) AS total_service_charges
FROM guests g
LEFT JOIN services s ON g.guest_id = s.guest_id
GROUP BY g.guest_id;
