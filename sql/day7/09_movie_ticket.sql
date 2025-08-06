--  9. Movie Ticket Booking 
-- Requirements: 
--  View view_now_showing for app frontend (hide backend seat hold logic). 
--  Procedure book_ticket() to reserve seat and update availability. 
--  Function get_available_seats(show_id). 
--  Trigger before_booking to prevent booking if houseful. 
--  Only allow public access via abstracted views.

-- Create Database
CREATE DATABASE IF NOT EXISTS MovieBookingDB;
USE MovieBookingDB;

-- Table: shows
CREATE TABLE shows (
    show_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_name VARCHAR(100),
    show_time DATETIME,
    total_seats INT,
    seats_booked INT DEFAULT 0,
    seat_hold_logic TEXT
);

-- Table: customers
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Table: bookings
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    show_id INT,
    customer_id INT,
    seats_reserved INT,
    booking_date DATE,
    FOREIGN KEY (show_id) REFERENCES shows(show_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- ✅ View: view_now_showing (hides backend seat_hold_logic)
CREATE OR REPLACE VIEW view_now_showing AS
SELECT 
    show_id,
    movie_name,
    show_time,
    total_seats,
    seats_booked
FROM shows;

-- ✅ Function: get_available_seats(show_id)
DELIMITER //
CREATE FUNCTION get_available_seats(s_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE available INT;
    SELECT total_seats - seats_booked INTO available
    FROM shows
    WHERE show_id = s_id;
    RETURN available;
END;
//
DELIMITER ;

-- ✅ Procedure: book_ticket(customer_id, show_id, seats, booking_date)
DELIMITER //
CREATE PROCEDURE book_ticket(
    IN c_id INT,
    IN s_id INT,
    IN seat_count INT,
    IN book_date DATE
)
BEGIN
    DECLARE available INT;

    SELECT total_seats - seats_booked INTO available
    FROM shows
    WHERE show_id = s_id;

    IF available >= seat_count THEN
        INSERT INTO bookings (show_id, customer_id, seats_reserved, booking_date)
        VALUES (s_id, c_id, seat_count, book_date);

        UPDATE shows
        SET seats_booked = seats_booked + seat_count
        WHERE show_id = s_id;
    ELSE
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Not enough seats available';
    END IF;
END;
//
DELIMITER ;

-- ✅ Trigger: before_booking (prevent booking if houseful)
DELIMITER //
CREATE TRIGGER before_booking
BEFORE INSERT ON bookings
FOR EACH ROW
BEGIN
    DECLARE available INT;

    SELECT total_seats - seats_booked INTO available
    FROM shows
    WHERE show_id = NEW.show_id;

    IF available < NEW.seats_reserved THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Cannot book. Show is houseful or insufficient seats.';
    END IF;
END;
//
DELIMITER ;

-- ✅ Public view only (restrict access to internal logic)
CREATE OR REPLACE VIEW view_public_shows AS
SELECT movie_name, show_time, total_seats - seats_booked AS available_seats
FROM shows;

-- ✅ Sample Data
INSERT INTO shows (movie_name, show_time, total_seats, seats_booked, seat_hold_logic)
VALUES 
('Avengers', '2025-08-10 18:00:00', 5, 0, 'Hold 2 VIP seats'),
('Inception', '2025-08-11 20:00:00', 3, 1, 'Maintenance reserve 1 seat');

INSERT INTO customers (name, email)
VALUES ('Nisha Reetha', 'nisha@example.com'),
       ('Ravi Kumar', 'ravi@example.com');

-- ✅ Sample Usage
-- CALL book_ticket(1, 1, 2, '2025-08-07');
-- SELECT get_available_seats(1);
-- SELECT * FROM view_now_showing;
-- SELECT * FROM view_public_shows;
