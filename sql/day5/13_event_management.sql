--  13. Event Management and Ticketing 
-- Requirements: 
--  Tables: events, attendees, tickets 
--  Insert new attendee registrations. 
--  Update ticket type or event date. 
--  Delete expired events and dependent tickets. 
--  Enforce CHECK (age >= 18) for age-restricted events. 
--  Modify a UNIQUE constraint on event title. 
--  Use transaction for bulk registrations; rollback if duplicates found.

CREATE DATABASE IF NOT EXISTS EventManagementDB;
USE EventManagementDB;

-- Create Events Table
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL UNIQUE,
    event_date DATE NOT NULL,
    age_restriction INT CHECK (age_restriction >= 18),
    location VARCHAR(255)
);

-- Create Attendees Table
CREATE TABLE attendees (
    attendee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL CHECK (age >= 18),
    email VARCHAR(100)
);

-- Create Tickets Table
CREATE TABLE tickets (
    ticket_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    attendee_id INT NOT NULL,
    ticket_type VARCHAR(50),
    purchase_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id)
);

-- Insert sample events
INSERT INTO events (title, event_date, age_restriction, location) VALUES
('Jazz Festival', CURDATE() + INTERVAL 30 DAY, 18, 'City Park'),
('Tech Expo', CURDATE() + INTERVAL 60 DAY, 18, 'Convention Center');

-- Insert sample attendees
INSERT INTO attendees (name, age, email) VALUES
('Suman Rao', 25, 'suman.rao@example.com'),
('Kiran Patel', 30, 'kiran.patel@example.com');

-- Update ticket type or event date
UPDATE tickets
SET ticket_type = 'VIP'
WHERE ticket_id = 1;

UPDATE events
SET event_date = event_date + INTERVAL 7 DAY
WHERE event_id = 1;

-- Delete expired events and dependent tickets
DELETE FROM events
WHERE event_date < CURDATE();

-- Modify UNIQUE constraint on event title:
-- Drop current UNIQUE index
ALTER TABLE events DROP INDEX title;

-- Add new UNIQUE index with different name
ALTER TABLE events ADD UNIQUE idx_unique_event_title (title);

-- Transaction for bulk registrations (example):
START TRANSACTION;

INSERT INTO attendees (name, age, email) VALUES
('Nisha Reetha', 28, 'nisha.reetha@example.com'),
('Rohit Singh', 24, 'rohit.singh@example.com');

-- Example ticket insertions for new attendees
INSERT INTO tickets (event_id, attendee_id, ticket_type) VALUES
(1, LAST_INSERT_ID() - 1, 'General'),
(1, LAST_INSERT_ID(), 'General');

-- If duplicates or error occurs, ROLLBACK
COMMIT;
