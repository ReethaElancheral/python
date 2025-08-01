-- Project 10: Vehicle Service Records
CREATE TABLE services (
    service_id INT PRIMARY KEY,
    vehicle_no VARCHAR(20),
    service_type VARCHAR(50),
    cost DECIMAL(10,2),
    service_date DATE,
    technician VARCHAR(100)
);

INSERT INTO services (service_id, vehicle_no, service_type, cost, service_date, technician) VALUES
(1, 'MH12AB1234', 'Oil Change', 1200, '2025-07-01', 'Ramesh'),
(2, 'DL09CD5678', 'Brake Repair', 1500, '2025-07-05', NULL),
(3, 'KA03EF9876', 'Tire Replacement', 1800, '2025-07-10', 'Suresh'),
(4, 'TN22GH4321', 'Battery Replacement', 2000, '2025-07-15', 'Manish'),
(5, 'MH12AB1234', 'Engine Tune-Up', 2500, '2025-07-20', NULL);

SELECT vehicle_no, service_type, cost FROM services WHERE service_date BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();
SELECT * FROM services WHERE vehicle_no LIKE '%9';
SELECT * FROM services WHERE cost BETWEEN 500 AND 2000;
SELECT * FROM services WHERE technician IS NULL;
SELECT DISTINCT service_type FROM services;
SELECT * FROM services ORDER BY service_date DESC, cost ASC;