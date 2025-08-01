-- Project 6: Hotel Room Booking System

CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

-- Tables

CREATE TABLE rooms (
    room_id INT PRIMARY KEY,
    room_type VARCHAR(50)
);

CREATE TABLE guests (
    guest_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    booking_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Insert sample data

INSERT INTO rooms (room_id, room_type) VALUES
(1, 'Single'),
(2, 'Double'),
(3, 'Suite');

INSERT INTO guests (guest_id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

INSERT INTO bookings (booking_id, guest_id, room_id, check_in, check_out) VALUES
(1, 1, 1, '2025-07-01', '2025-07-05'),
(2, 1, 2, '2025-07-10', '2025-07-15'),
(3, 2, 1, '2025-07-03', '2025-07-04'),
(4, 2, 3, '2025-07-20', '2025-07-22'),
(5, 3, 2, '2025-07-05', '2025-07-10'),
(6, 3, 1, '2025-07-11', '2025-07-12'),
(7, 3, 1, '2025-07-15', '2025-07-16'),
(8, 1, 3, '2025-07-18', '2025-07-19');

INSERT INTO payments (payment_id, booking_id, amount, payment_date) VALUES
(1, 1, 5000, '2025-07-01'),
(2, 2, 8000, '2025-07-10'),
(3, 3, 1000, '2025-07-03'),
(4, 4, 12000, '2025-07-20'),
(5, 5, 7500, '2025-07-05'),
(6, 6, 1500, '2025-07-11'),
(7, 7, 1600, '2025-07-15'),
(8, 8, 11000, '2025-07-18');

-- Queries

-- 1. Total amount paid per guest
SELECT 
    g.name,
    SUM(p.amount) AS total_paid
FROM guests g
JOIN bookings b ON g.guest_id = b.guest_id
JOIN payments p ON b.booking_id = p.booking_id
GROUP BY g.guest_id, g.name;

-- 2. Rooms booked more than 5 times (COUNT, HAVING)
SELECT 
    r.room_type,
    COUNT(b.booking_id) AS bookings_count
FROM rooms r
JOIN bookings b ON r.room_id = b.room_id
GROUP BY r.room_id, r.room_type
HAVING bookings_count > 5;

-- 3. Group bookings by room type and calculate average stay duration (in days)
SELECT 
    r.room_type,
    AVG(DATEDIFF(b.check_out, b.check_in)) AS avg_stay_duration
FROM rooms r
JOIN bookings b ON r.room_id = b.room_id
GROUP BY r.room_type;

-- 4. INNER JOIN: guests ↔ bookings ↔ rooms
SELECT 
    g.name AS guest_name,
    r.room_type,
    b.check_in,
    b.check_out
FROM guests g
INNER JOIN bookings b ON g.guest_id = b.guest_id
INNER JOIN rooms r ON b.room_id = r.room_id;

-- 5. FULL OUTER JOIN: rooms and bookings
-- MySQL does not support FULL OUTER JOIN directly.
-- Use UNION of LEFT JOIN and RIGHT JOIN to simulate FULL OUTER JOIN.

SELECT 
    r.room_id,
    r.room_type,
    b.booking_id,
    b.check_in,
    b.check_out
FROM rooms r
LEFT JOIN bookings b ON r.room_id = b.room_id

UNION

SELECT 
    r.room_id,
    r.room_type,
    b.booking_id,
    b.check_in,
    b.check_out
FROM rooms r
RIGHT JOIN bookings b ON r.room_id = b.room_id;

-- 6. SELF JOIN to find guests who booked same room multiple times
SELECT 
    g1.name AS guest1,
    g2.name AS guest2,
    b1.room_id,
    r.room_type
FROM bookings b1
JOIN bookings b2 ON b1.room_id = b2.room_id AND b1.booking_id <> b2.booking_id AND b1.guest_id = b2.guest_id
JOIN guests g1 ON b1.guest_id = g1.guest_id
JOIN guests g2 ON b2.guest_id = g2.guest_id
JOIN rooms r ON b1.room_id = r.room_id
ORDER BY b1.room_id;
