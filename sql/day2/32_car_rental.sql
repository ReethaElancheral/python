-- Project 12: Car Rental Service

CREATE DATABASE IF NOT EXISTS car_rental_db;
USE car_rental_db;


CREATE TABLE vehicles (
    vehicle_id INT PRIMARY KEY,
    model VARCHAR(100),
    car_type VARCHAR(50)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE rentals (
    rental_id INT PRIMARY KEY,
    vehicle_id INT,
    customer_id INT,
    rental_date DATE,
    return_date DATE,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    rental_id INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (rental_id) REFERENCES rentals(rental_id)
);



INSERT INTO vehicles (vehicle_id, model, car_type) VALUES
(1, 'Toyota Innova', 'SUV'),
(2, 'Hyundai i20', 'Hatchback'),
(3, 'Maruti Swift', 'Hatchback'),
(4, 'Mahindra Thar', 'SUV'),
(5, 'Honda Amaze', 'Sedan');

INSERT INTO customers (customer_id, name, city) VALUES
(1, 'Amit Sharma', 'Delhi'),
(2, 'Priya Verma', 'Mumbai'),
(3, 'Ravi Kumar', 'Chennai'),
(4, 'Neha Singh', 'Delhi');

INSERT INTO rentals (rental_id, vehicle_id, customer_id, rental_date, return_date) VALUES
(1, 1, 1, '2024-01-05', '2024-01-10'),
(2, 2, 2, '2024-01-06', '2024-01-08'),
(3, 3, 3, '2024-01-07', '2024-01-09'),
(4, 1, 2, '2024-01-12', '2024-01-14'),
(5, 1, 3, '2024-01-15', '2024-01-18'),
(6, 1, 4, '2024-01-19', '2024-01-22'),
(7, 4, 1, '2024-01-23', '2024-01-25'),
(8, 4, 2, '2024-01-26', '2024-01-27'),
(9, 5, 2, '2024-01-28', '2024-01-29'),
(10, 1, 1, '2024-01-30', '2024-02-02');

INSERT INTO payments (payment_id, rental_id, amount) VALUES
(1, 1, 5000),
(2, 2, 2000),
(3, 3, 2500),
(4, 4, 4800),
(5, 5, 4900),
(6, 6, 4700),
(7, 7, 6000),
(8, 8, 6200),
(9, 9, 4300),
(10, 10, 5100);



-- 1. Total rentals per vehicle
SELECT 
    v.model,
    COUNT(r.rental_id) AS total_rentals
FROM vehicles v
LEFT JOIN rentals r ON v.vehicle_id = r.vehicle_id
GROUP BY v.vehicle_id, v.model;

-- 2. Vehicles rented more than 10 times (HAVING)
SELECT 
    v.model,
    COUNT(r.rental_id) AS rental_count
FROM vehicles v
JOIN rentals r ON v.vehicle_id = r.vehicle_id
GROUP BY v.vehicle_id, v.model
HAVING rental_count > 10;

-- 3. Average rental cost per car type
SELECT 
    v.car_type,
    AVG(p.amount) AS avg_rental_cost
FROM vehicles v
JOIN rentals r ON v.vehicle_id = r.vehicle_id
JOIN payments p ON r.rental_id = p.rental_id
GROUP BY v.car_type;

-- 4. INNER JOIN rentals ↔ vehicles
SELECT 
    r.rental_id,
    c.name AS customer,
    v.model AS vehicle,
    r.rental_date,
    r.return_date
FROM rentals r
JOIN customers c ON r.customer_id = c.customer_id
JOIN vehicles v ON r.vehicle_id = v.vehicle_id;

-- 5. LEFT JOIN: vehicles ↔ payments (vehicles without payments)
SELECT 
    v.model,
    p.amount
FROM vehicles v
LEFT JOIN rentals r ON v.vehicle_id = r.vehicle_id
LEFT JOIN payments p ON r.rental_id = p.rental_id;

-- 6. SELF JOIN: cars of the same model and type
SELECT 
    v1.model AS vehicle1,
    v2.model AS vehicle2,
    v1.car_type
FROM vehicles v1
JOIN vehicles v2 ON v1.car_type = v2.car_type 
WHERE v1.vehicle_id < v2.vehicle_id;
