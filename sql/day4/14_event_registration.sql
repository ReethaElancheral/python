CREATE DATABASE IF NOT EXISTS event_portal_db;
USE event_portal_db;

CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150),
    total_seats INT,
    registered_count INT,
    event_date DATE
);

CREATE TABLE attendees (
    attendee_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE registrations (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    attendee_id INT,
    registration_date DATE,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id)
);

CREATE TABLE feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    attendee_id INT,
    rating INT,
    comments TEXT,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (attendee_id) REFERENCES attendees(attendee_id)
);

-- Insert sample data

INSERT INTO events (name, total_seats, registered_count, event_date) VALUES
('Tech Conference', 200, 150, '2025-08-15'),
('Music Festival', 500, 400, '2025-09-10');

INSERT INTO attendees (name) VALUES
('Alice'), ('Bob'), ('Charlie');

INSERT INTO registrations (event_id, attendee_id, registration_date) VALUES
(1,1,'2025-07-01'), (1,2,'2025-07-05'), (2,3,'2025-07-20');

INSERT INTO feedback (event_id, attendee_id, rating, comments) VALUES
(1,1,5,'Great event!'), (1,2,4,'Good organization'), (2,3,3,'It was okay');

-- Queries

-- 1. Subquery in SELECT to calculate average feedback rating per event
SELECT
    e.name,
    (SELECT AVG(rating) FROM feedback f WHERE f.event_id = e.event_id) AS avg_rating
FROM events e;

-- 2. CASE to classify events based on turnout percentage
SELECT
    name,
    registered_count,
    total_seats,
    CASE
        WHEN registered_count / total_seats >= 0.8 THEN 'High Turnout'
        WHEN registered_count / total_seats BETWEEN 0.5 AND 0.79 THEN 'Medium Turnout'
        ELSE 'Low Turnout'
    END AS turnout_category
FROM events;

-- 3. UNION ALL to combine online and offline events
SELECT event_id, name, 'Online' AS event_type FROM events WHERE event_date >= CURDATE()
UNION ALL
SELECT event_id, name, 'Offline' AS event_type FROM events WHERE event_date < CURDATE();

-- 4. Correlated subquery to find top participant per event (most registrations)
SELECT
    event_id,
    (SELECT attendee_id FROM registrations r2 WHERE r2.event_id = r1.event_id GROUP BY attendee_id ORDER BY COUNT(*) DESC LIMIT 1) AS top_attendee
FROM registrations r1
GROUP BY event_id;

-- 5. JOIN + GROUP BY to show event-wise engagement (number of registrations)
SELECT
    e.name,
    COUNT(r.registration_id) AS registrations_count
FROM events e
LEFT JOIN registrations r ON e.event_id = r.event_id
GROUP BY e.event_id, e.name;

-- 6. Date filtering for upcoming events
SELECT * FROM events WHERE event_date >= CURDATE();
