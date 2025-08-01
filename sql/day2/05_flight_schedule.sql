-- Project 5: Flight Schedule System
CREATE TABLE flights (
    flight_id INT PRIMARY KEY,
    flight_number VARCHAR(10),
    origin VARCHAR(50),
    destination VARCHAR(50),
    status VARCHAR(20),
    departure_time DATETIME
);

INSERT INTO flights (flight_id, flight_number, origin, destination, status, departure_time) VALUES
(1, 'AI101', 'Delhi', 'Chennai', 'On Time', '2025-08-01 09:00:00'),
(2, 'AI102', 'Mumbai', 'Chennai', 'Delayed', '2025-08-01 11:30:00'),
(3, 'AI201', 'Chennai', 'Mumbai', NULL, '2025-08-02 14:00:00'),
(4, 'BA303', 'London', 'Delhi', 'On Time', '2025-08-03 20:00:00'),
(5, 'AI303', 'Chennai', 'Kolkata', 'Cancelled', '2025-08-04 17:00:00');


SELECT flight_number, origin, destination FROM flights WHERE destination IN ('Chennai', 'Mumbai');
SELECT * FROM flights WHERE flight_number LIKE '%AI';
SELECT * FROM flights WHERE departure_time BETWEEN '2025-07-31 00:00:00' AND '2025-07-31 23:59:59';
SELECT * FROM flights WHERE status IS NULL;
SELECT DISTINCT destination FROM flights;
SELECT * FROM flights ORDER BY departure_time ASC;