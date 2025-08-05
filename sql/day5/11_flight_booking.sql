--  11. Flight Booking and Passenger Management 
-- Requirements: 
--  Tables: flights, passengers, tickets, payments 
--  Insert a ticket with FOREIGN KEY to passenger and flight. 
--  Update flight status and seat count. 
--  Delete unpaid tickets using date filter. 
--  Add CHECK (flight_date >= current_date). 
--  Drop and recreate NOT NULL on seat_no. 
--  Transaction: Insert ticket + payment; rollback if payment fails.

-- Create Database
CREATE DATABASE IF NOT EXISTS FlightBookingDB;
USE FlightBookingDB;

-- Create Flights Table
CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_name VARCHAR(100) NOT NULL,
    flight_date DATE NOT NULL,
    total_seats INT NOT NULL,
    available_seats INT NOT NULL,
    status VARCHAR(50),
    CHECK (flight_date >= CURRENT_DATE)
);

-- Create Passengers Table
CREATE TABLE passengers (
    passenger_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(15)
);

-- Create Tickets Table
CREATE TABLE tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_id INT,
    flight_id INT,
    seat_no VARCHAR(10),
    booking_date DATE DEFAULT CURDATE(),
    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
);

-- Create Payments Table
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT,
    amount DECIMAL(10,2),
    paid BOOLEAN DEFAULT FALSE,
    payment_date DATE DEFAULT CURDATE(),
    FOREIGN KEY (ticket_id) REFERENCES tickets(ticket_id)
);

-- ✅ Insert Sample Flights
INSERT INTO flights (flight_name, flight_date, total_seats, available_seats, status) VALUES
('Air India 123', CURDATE() + INTERVAL 2 DAY, 180, 180, 'Scheduled'),
('IndiGo 456', CURDATE() + INTERVAL 5 DAY, 150, 150, 'Scheduled');

-- ✅ Insert Sample Passengers
INSERT INTO passengers (full_name, email, phone) VALUES
('Ravi Kumar', 'ravi.kumar@email.com', '9876543210'),
('Ananya Sen', 'ananya.sen@email.com', '9123456789');

-- ✅ Ticket Booking + Payment Transaction (Manual)
START TRANSACTION;

-- Step 1: Insert ticket for passenger_id = 1, flight_id = 1
INSERT INTO tickets (passenger_id, flight_id, seat_no)
VALUES (1, 1, '12A');

-- Step 2: Savepoint
SAVEPOINT after_ticket;

-- Step 3: Insert payment
INSERT INTO payments (ticket_id, amount, paid)
VALUES (LAST_INSERT_ID(), 5500.00, TRUE);

-- Step 4: Update available seats in flights
UPDATE flights SET available_seats = available_seats - 1 WHERE flight_id = 1;

-- Optional rollback simulation
-- ROLLBACK TO after_ticket; -- Uncomment if payment failed
-- ROLLBACK;                 -- Full rollback
-- If all good
COMMIT;

-- ✅ Update Flight Status
UPDATE flights
SET status = 'Departed'
WHERE flight_id = 1;

-- ✅ Delete Unpaid Tickets Older Than 1 Day
DELETE t
FROM tickets t
LEFT JOIN payments p ON t.ticket_id = p.ticket_id
WHERE p.paid = FALSE AND t.booking_date < (CURDATE() - INTERVAL 1 DAY);

-- ✅ Drop and Recreate NOT NULL on seat_no
-- First drop NOT NULL
ALTER TABLE tickets MODIFY seat_no VARCHAR(10) NULL;

-- Reapply NOT NULL
ALTER TABLE tickets MODIFY seat_no VARCHAR(10) NOT NULL;

-- ✅ View Current Tables
SELECT * FROM flights;
SELECT * FROM tickets;
SELECT * FROM payments;
