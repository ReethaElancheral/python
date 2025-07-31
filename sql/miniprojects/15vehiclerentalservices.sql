-- -----------------------------------------------
-- Project 15: Vehicle Rental Service
-- Requirements:
-- • Create rental_db
-- • Tables: vehicles, customers, rentals, vehicle_types
-- • Store rental duration, cost, customer info
-- • Queries:
--    - Vehicles rented in a date range
--    - Total income per vehicle type
-- -----------------------------------------------

CREATE DATABASE IF NOT EXISTS rental_db;
USE rental_db;

-- Vehicle types table
CREATE TABLE vehicle_types (
    type_id INT PRIMARY KEY AUTO_INCREMENT,
    type_name VARCHAR(50) NOT NULL
);

-- Vehicles table
CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY AUTO_INCREMENT,
    type_id INT,
    make VARCHAR(50),
    model VARCHAR(50),
    registration_number VARCHAR(50) UNIQUE NOT NULL,
    FOREIGN KEY (type_id) REFERENCES vehicle_types(type_id)
);

-- Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Rentals table
CREATE TABLE rentals (
    rental_id INT PRIMARY KEY AUTO_INCREMENT,
    vehicle_id INT,
    customer_id INT,
    rent_start DATE,
    rent_end DATE,
    cost DECIMAL(10,2),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert vehicle types
INSERT INTO vehicle_types (type_name) VALUES
('Sedan'),
('SUV'),
('Truck'),
('Motorbike');

-- Insert vehicles
INSERT INTO vehicles (type_id, make, model, registration_number) VALUES
(1, 'Toyota', 'Camry', 'ABC123'),
(2, 'Honda', 'CR-V', 'XYZ789'),
(3, 'Ford', 'F-150', 'TRK456'),
(4, 'Yamaha', 'YZF-R3', 'MOTO111');

-- Insert customers
INSERT INTO customers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com');

-- Insert rentals
INSERT INTO rentals (vehicle_id, customer_id, rent_start, rent_end, cost) VALUES
(1, 1, '2025-07-01', '2025-07-05', 5000.00),
(2, 2, '2025-07-03', '2025-07-06', 7500.00),
(3, 3, '2025-07-05', '2025-07-10', 12000.00),
(4, 4, '2025-07-07', '2025-07-08', 1500.00),
(1, 2, '2025-07-10', '2025-07-12', 3000.00);

-- -----------------------------------------------
-- Queries
-- -----------------------------------------------

-- 1. Vehicles rented in a date range (example: between '2025-07-02' and '2025-07-08')
SELECT
    v.registration_number,
    v.make,
    v.model,
    vt.type_name,
    r.rent_start,
    r.rent_end,
    c.name AS customer_name
FROM rentals r
JOIN vehicles v ON r.vehicle_id = v.vehicle_id
JOIN vehicle_types vt ON v.type_id = vt.type_id
JOIN customers c ON r.customer_id = c.customer_id
WHERE r.rent_start <= '2025-07-08' AND r.rent_end >= '2025-07-02'
ORDER BY r.rent_start;

-- 2. Total income per vehicle type
SELECT
    vt.type_name,
    SUM(r.cost) AS total_income
FROM rentals r
JOIN vehicles v ON r.vehicle_id = v.vehicle_id
JOIN vehicle_types vt ON v.type_id = vt.type_id
GROUP BY vt.type_name
ORDER BY total_income DESC;
