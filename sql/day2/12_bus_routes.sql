-- Project 12: Bus Route Information
CREATE TABLE routes (
    route_id INT PRIMARY KEY,
    bus_no VARCHAR(20),
    origin VARCHAR(50),
    destination VARCHAR(50),
    departure DATETIME,
    arrival DATETIME,
    status VARCHAR(20)
);

INSERT INTO routes (route_id, bus_no, origin, destination, departure, arrival, status) VALUES
(1, 'TN22X1234', 'Coimbatore', 'Madurai', '07:00:00', '11:00:00', 'On Time'),
(2, 'TN22X5678', 'Coimbatore', 'Salem', '09:00:00', '12:00:00', NULL),
(3, 'TN22X9012', 'Madurai', 'Coimbatore', '14:00:00', '18:00:00', 'Delayed'),
(4, 'TN22X3456', 'Salem', 'Madurai', '06:00:00', '10:00:00', 'On Time'),
(5, 'TN22X7890', 'Coimbatore', 'Tirupur', '13:00:00', '15:00:00', 'Cancelled');

SELECT bus_no, departure, arrival FROM routes WHERE origin = 'Coimbatore' AND destination = 'Madurai';
SELECT * FROM routes WHERE destination LIKE '%pur';
SELECT * FROM routes WHERE destination IN ('Madurai', 'Salem', 'Tirupur');
SELECT * FROM routes WHERE status IS NULL;
SELECT * FROM routes ORDER BY departure ASC;