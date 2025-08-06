--  5. Hotel Booking System 
-- Requirements: 
--  Tables: guests, rooms, bookings, payments, room_types 
--  Normalize bookings and guest details to 3NF. 
--  Index room_type, check_in, guest_id. 
--  Use EXPLAIN to analyze booking history queries. 
--  Optimize performance of join across 3+ tables: rooms + guests + payments. 
--  Create a denormalized table for daily revenue reporting. 
--  Use LIMIT to return top 10 highest-paying guests.

CREATE DATABASE IF NOT EXISTS HotelDB;
USE HotelDB;

-- Guests table
CREATE TABLE guests (
    guest_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20)
);

-- Room Types
CREATE TABLE room_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50),
    price DECIMAL(10,2)
);

-- Rooms
CREATE TABLE rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10),
    type_id INT,
    FOREIGN KEY (type_id) REFERENCES room_types(type_id)
);

-- Bookings
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    guest_id INT,
    room_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- Payments
CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    booking_id INT,
    amount DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Indexing
CREATE INDEX idx_room_type ON rooms(type_id);
CREATE INDEX idx_check_in ON bookings(check_in);
CREATE INDEX idx_guest_id ON bookings(guest_id);

-- EXPLAIN booking history
EXPLAIN SELECT * FROM bookings WHERE guest_id = 1 ORDER BY check_in DESC;

-- Join optimization (rooms + guests + payments)
EXPLAIN SELECT g.name, r.room_number, p.amount
FROM guests g
JOIN bookings b ON g.guest_id = b.guest_id
JOIN rooms r ON b.room_id = r.room_id
JOIN payments p ON b.booking_id = p.booking_id;

-- Denormalized revenue table
CREATE TABLE daily_revenue (
    date DATE,
    total_amount DECIMAL(10,2)
);

-- Top 10 highest-paying guests
SELECT g.name, SUM(p.amount) AS total_spent
FROM guests g
JOIN bookings b ON g.guest_id = b.guest_id
JOIN payments p ON b.booking_id = p.booking_id
GROUP BY g.guest_id
ORDER BY total_spent DESC
LIMIT 10;
