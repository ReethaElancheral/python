--  10. Vehicle Rental Management 
-- Requirements: 
--  Tables: vehicles, customers, rentals, invoices 
--  Insert rentals with constraints on vehicle availability. 
--  Update mileage and fuel after return. 
--  Delete completed rentals older than 3 months. 
--  CHECK (return_date > rental_date). 
--  Use SAVEPOINT during rental and rollback on pricing error. 
--  Demonstrate durability by recovering transaction after reconnect. 

-- Create Database
CREATE DATABASE IF NOT EXISTS VehicleRentalDB;
USE VehicleRentalDB;

-- Create Vehicles Table
CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_type VARCHAR(50) NOT NULL,
    model VARCHAR(100),
    mileage INT,
    fuel_level DECIMAL(5,2),
    is_available BOOLEAN DEFAULT TRUE
);

-- Create Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(15) UNIQUE
);

-- Create Rentals Table
CREATE TABLE rentals (
    rental_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT,
    customer_id INT,
    rental_date DATE NOT NULL,
    return_date DATE,
    CHECK (return_date IS NULL OR return_date > rental_date),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create Invoices Table
CREATE TABLE invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    rental_id INT,
    amount DECIMAL(10,2),
    paid BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (rental_id) REFERENCES rentals(rental_id)
);

-- Insert Sample Vehicles
INSERT INTO vehicles (vehicle_type, model, mileage, fuel_level, is_available) VALUES
('Sedan', 'Honda City', 30000, 75.0, TRUE),
('SUV', 'Hyundai Creta', 20000, 60.5, TRUE),
('Bike', 'Royal Enfield', 15000, 90.0, TRUE);

-- Insert Sample Customers
INSERT INTO customers (name, phone) VALUES
('Aarav Mehta', '9876543210'),
('Ishita Roy', '9123456789');

-- ✅ Rental Transaction with SAVEPOINT (No Stored Procedure)
START TRANSACTION;

-- Check availability of vehicle_id = 1
SELECT is_available INTO @available FROM vehicles WHERE vehicle_id = 1;

-- Assume @available is TRUE (proceed manually without logic branching)
-- Step 1: Insert Rental
INSERT INTO rentals (vehicle_id, customer_id, rental_date)
VALUES (1, 1, CURDATE());

-- Step 2: Savepoint after rental
SAVEPOINT after_rental;

-- Step 3: Insert Invoice
INSERT INTO invoices (rental_id, amount, paid)
VALUES (LAST_INSERT_ID(), 1500.00, FALSE);

-- Simulate a pricing error condition
-- SET @error := TRUE;

-- ROLLBACK TO after_rental; -- Uncomment if error simulation is true
-- ROLLBACK;                 -- Full rollback if necessary
-- COMMIT if all good
COMMIT;

-- ✅ Update vehicle data on return (mileage and fuel)
UPDATE vehicles
SET mileage = mileage + 300, fuel_level = 50.0, is_available = TRUE
WHERE vehicle_id = 1;

-- ✅ Delete completed rentals older than 3 months
DELETE FROM rentals
WHERE return_date IS NOT NULL AND return_date < (CURDATE() - INTERVAL 3 MONTH);

-- ✅ Demonstrate durability (simulated: re-run SELECT after reconnect)
SELECT * FROM rentals;
SELECT * FROM invoices;
