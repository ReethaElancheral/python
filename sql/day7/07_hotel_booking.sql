--  7. Hotel Booking System 
-- Requirements: 
--  View view_available_rooms that hides internal maintenance schedules. 
--  Procedure book_room() to handle multiple insertions atomically. 
--  Function calculate_stay_cost() based on room rate and duration. 
--  Trigger after_booking to update room availability. 
--  Receptionists use restricted views instead of base tables.


CREATE DATABASE IF NOT EXISTS HotelDB;
USE HotelDB;

-- Table: rooms
CREATE TABLE rooms (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10),
    room_type VARCHAR(50),
    rate_per_night DECIMAL(10, 2),
    is_available BOOLEAN DEFAULT TRUE,
    under_maintenance BOOLEAN DEFAULT FALSE
);

-- Table: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    contact VARCHAR(15)
);

-- Table: bookings
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    room_id INT,
    check_in_date DATE,
    check_out_date DATE,
    total_cost DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

-- ✅ View: view_available_rooms (hides maintenance info)
CREATE OR REPLACE VIEW view_available_rooms AS
SELECT room_id, room_number, room_type, rate_per_night
FROM rooms
WHERE is_available = TRUE AND under_maintenance = FALSE;

-- ✅ Function: calculate_stay_cost(room_id, check_in, check_out)
DELIMITER //
CREATE FUNCTION calculate_stay_cost(r_id INT, in_date DATE, out_date DATE)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE rate DECIMAL(10,2);
    DECLARE nights INT;
    DECLARE cost DECIMAL(10,2);

    SELECT rate_per_night INTO rate FROM rooms WHERE room_id = r_id;
    SET nights = DATEDIFF(out_date, in_date);
    SET cost = rate * nights;

    RETURN cost;
END;
//
DELIMITER ;

-- ✅ Procedure: book_room(cust_id, r_id, in_date, out_date)
DELIMITER //
CREATE PROCEDURE book_room (
    IN cust_id INT,
    IN r_id INT,
    IN in_date DATE,
    IN out_date DATE
)
BEGIN
    DECLARE total DECIMAL(10,2);

    START TRANSACTION;

    SET total = calculate_stay_cost(r_id, in_date, out_date);

    INSERT INTO bookings (customer_id, room_id, check_in_date, check_out_date, total_cost)
    VALUES (cust_id, r_id, in_date, out_date, total);

    UPDATE rooms SET is_available = FALSE WHERE room_id = r_id;

    COMMIT;
END;
//
DELIMITER ;

-- ✅ Trigger: after_booking (automatically update room availability)
DELIMITER //
CREATE TRIGGER after_booking
AFTER INSERT ON bookings
FOR EACH ROW
BEGIN
    UPDATE rooms SET is_available = FALSE WHERE room_id = NEW.room_id;
END;
//
DELIMITER ;

-- ✅ Restricted View for Receptionists (hides sensitive info)
CREATE OR REPLACE VIEW view_receptionist_bookings AS
SELECT 
    b.booking_id,
    c.name AS customer_name,
    r.room_number,
    b.check_in_date,
    b.check_out_date
FROM bookings b
JOIN customers c ON b.customer_id = c.customer_id
JOIN rooms r ON b.room_id = r.room_id;

-- ✅ Sample Data
INSERT INTO rooms (room_number, room_type, rate_per_night, is_available, under_maintenance)
VALUES 
('101', 'Deluxe', 3000.00, TRUE, FALSE),
('102', 'Suite', 5000.00, TRUE, TRUE),
('103', 'Standard', 2000.00, TRUE, FALSE);

INSERT INTO customers (name, contact)
VALUES ('Rajesh Kumar', '9998887770'), ('Nisha Patel', '9887766554');

-- ✅ Sample Usage
-- CALL book_room(1, 1, '2025-08-10', '2025-08-13');
-- SELECT * FROM view_available_rooms;
-- SELECT calculate_stay_cost(1, '2025-08-10', '2025-08-13');
-- SELECT * FROM view_receptionist_bookings;
