--  8. Flight Reservation System 
-- Requirements: 
--  View view_flight_schedule (excludes internal notes and employee info). 
--  Procedure book_flight() handles insert and returns PNR. 
--  Function get_passenger_count(flight_id) for admin dashboard. 
--  Trigger after_checkin marks passenger as boarded. 
--  Use secure views for customer-facing apps.

-- Create Database
CREATE DATABASE IF NOT EXISTS FlightDB;
USE FlightDB;

-- Table: flights
CREATE TABLE flights (
    flight_id INT PRIMARY KEY AUTO_INCREMENT,
    flight_number VARCHAR(20),
    departure VARCHAR(50),
    arrival VARCHAR(50),
    departure_time DATETIME,
    arrival_time DATETIME,
    total_seats INT,
    notes TEXT,
    employee_notes TEXT
);

-- Table: passengers
CREATE TABLE passengers (
    passenger_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    passport_no VARCHAR(20)
);

-- Table: reservations
CREATE TABLE reservations (
    reservation_id INT PRIMARY KEY AUTO_INCREMENT,
    flight_id INT,
    passenger_id INT,
    booking_date DATE,
    status VARCHAR(20) DEFAULT 'booked',
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id),
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id)
);

-- ✅ View: view_flight_schedule (excludes internal notes)
CREATE OR REPLACE VIEW view_flight_schedule AS
SELECT 
    flight_id,
    flight_number,
    departure,
    arrival,
    departure_time,
    arrival_time,
    total_seats
FROM flights;

-- ✅ Function: get_passenger_count(flight_id)
DELIMITER //
CREATE FUNCTION get_passenger_count(f_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE count_passengers INT;
    SELECT COUNT(*) INTO count_passengers
    FROM reservations
    WHERE flight_id = f_id AND status = 'booked';
    RETURN count_passengers;
END;
//
DELIMITER ;

-- ✅ Procedure: book_flight(passenger_id, flight_id, booking_date)
DELIMITER //
CREATE PROCEDURE book_flight(
    IN p_id INT,
    IN f_id INT,
    IN book_date DATE
)
BEGIN
    DECLARE total_booked INT;
    DECLARE total_allowed INT;

    SELECT COUNT(*) INTO total_booked
    FROM reservations
    WHERE flight_id = f_id AND status = 'booked';

    SELECT total_seats INTO total_allowed
    FROM flights
    WHERE flight_id = f_id;

    IF total_booked < total_allowed THEN
        INSERT INTO reservations (flight_id, passenger_id, booking_date)
        VALUES (f_id, p_id, book_date);
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Flight is fully booked';
    END IF;
END;
//
DELIMITER ;

-- ✅ Trigger: after_checkin (marks passenger as boarded)
DELIMITER //
CREATE TRIGGER after_checkin
AFTER UPDATE ON reservations
FOR EACH ROW
BEGIN
    IF NEW.status = 'checked_in' THEN
        UPDATE reservations
        SET status = 'boarded'
        WHERE reservation_id = NEW.reservation_id;
    END IF;
END;
//
DELIMITER ;

-- ✅ Secure view for customer-facing apps (no notes)
CREATE OR REPLACE VIEW view_customer_flights AS
SELECT flight_number, departure, arrival, departure_time, arrival_time
FROM flights;

-- ✅ Sample Data
INSERT INTO flights (flight_number, departure, arrival, departure_time, arrival_time, total_seats, notes, employee_notes)
VALUES 
('AI101', 'Delhi', 'Mumbai', '2025-08-15 08:00:00', '2025-08-15 10:30:00', 3, 'Regular', 'Internal crew only'),
('AI202', 'Bangalore', 'Chennai', '2025-08-16 09:00:00', '2025-08-16 10:15:00', 2, 'Short trip', 'Pilot rest');

INSERT INTO passengers (name, passport_no)
VALUES ('Rahul Verma', 'P1234567'), ('Sita Menon', 'P9876543'), ('Aman Joshi', 'P1928374');

-- ✅ Sample Usage
-- CALL book_flight(1, 1, '2025-08-12');
-- SELECT get_passenger_count(1);
-- SELECT * FROM view_flight_schedule;
-- SELECT * FROM view_customer_flights;
