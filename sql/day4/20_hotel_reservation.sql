CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

-- Tables

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10),
    room_type ENUM('Economy', 'Deluxe', 'Suite'),
    price_per_night DECIMAL(10,2)
);

CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in DATE,
    check_out DATE,
    status ENUM('Completed', 'Upcoming'),
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    amount_paid DECIMAL(10,2),
    payment_date DATE,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);

-- Sample data

INSERT INTO rooms (room_number, room_type, price_per_night) VALUES
('101', 'Economy', 1500),
('102', 'Deluxe', 3000),
('201', 'Suite', 5000),
('202', 'Deluxe', 3200),
('301', 'Economy', 1400);

INSERT INTO guests (name, city) VALUES
('Alice', 'CityA'),
('Bob', 'CityB'),
('Charlie', 'CityA'),
('David', 'CityC');

INSERT INTO bookings (guest_id, room_id, check_in, check_out, status) VALUES
(1, 1, '2025-07-01', '2025-07-05', 'Completed'),
(2, 2, '2025-07-10', '2025-07-12', 'Upcoming'),
(3, 3, '2025-07-15', '2025-07-20', 'Upcoming'),
(1, 4, '2025-06-20', '2025-06-25', 'Completed'),
(4, 5, '2025-07-18', '2025-07-22', 'Upcoming'),
(2, 1, '2025-05-01', '2025-05-03', 'Completed');

INSERT INTO payments (booking_id, amount_paid, payment_date) VALUES
(1, 6000, '2025-07-05'),
(4, 16000, '2025-06-25'),
(6, 3000, '2025-05-03');

-- Queries

-- 1. Subquery in SELECT to show bill summary (total amount paid) per guest
SELECT
    g.guest_id,
    g.name,
    (SELECT IFNULL(SUM(p.amount_paid), 0)
     FROM bookings b
     LEFT JOIN payments p ON b.booking_id = p.booking_id
     WHERE b.guest_id = g.guest_id) AS total_amount_paid
FROM guests g;

-- 2. CASE to label room types (already ENUM, but example query to categorize)
SELECT
    room_id,
    room_number,
    room_type,
    CASE
        WHEN room_type = 'Economy' THEN 'Economy'
        WHEN room_type = 'Deluxe' THEN 'Deluxe'
        WHEN room_type = 'Suite' THEN 'Suite'
        ELSE 'Unknown'
    END AS room_category
FROM rooms;

-- 3. UNION to combine completed and upcoming bookings
SELECT booking_id, guest_id, room_id, check_in, check_out, status
FROM bookings
WHERE status = 'Completed'
UNION
SELECT booking_id, guest_id, room_id, check_in, check_out, status
FROM bookings
WHERE status = 'Upcoming';

-- 4. Correlated subquery to find most frequent guest per room type
SELECT
    r.room_type,
    (SELECT g.name
     FROM bookings b2
     JOIN guests g ON b2.guest_id = g.guest_id
     WHERE b2.room_id = r.room_id
     GROUP BY g.guest_id
     ORDER BY COUNT(*) DESC
     LIMIT 1) AS most_frequent_guest
FROM rooms r
GROUP BY r.room_type;

-- 5. JOIN + GROUP BY for revenue per room type
SELECT
    r.room_type,
    IFNULL(SUM(p.amount_paid), 0) AS total_revenue
FROM rooms r
LEFT JOIN bookings b ON r.room_id = b.room_id
LEFT JOIN payments p ON b.booking_id = p.booking_id
GROUP BY r.room_type;

-- 6. Date filtering for check-in/check-out analytics (e.g., bookings in last 30 days)
SELECT *
FROM bookings
WHERE check_in BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE()
   OR check_out BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();
