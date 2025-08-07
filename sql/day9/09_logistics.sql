--  9. Logistics & Fleet Utilization Reporting 
-- Requirements: 
--  OLTP: deliveries, vehicles, drivers, routes. 
--  Warehouse: Star Schema with delivery fact and dimensions. 
--  ETL cleans GPS coordinates and timestamps.
--  Reports: fuel usage per trip, driver performance over time. 
--  OLAP used for route optimization analysis. 

-- Create Database
CREATE DATABASE IF NOT EXISTS LogisticsWarehouse;
USE LogisticsWarehouse;

-- Dimension Tables

-- Vehicle dimension
CREATE TABLE dim_vehicle (
    vehicle_id INT PRIMARY KEY,
    vehicle_number VARCHAR(20),
    vehicle_type VARCHAR(50)
);

-- Driver dimension
CREATE TABLE dim_driver (
    driver_id INT PRIMARY KEY,
    driver_name VARCHAR(100),
    license_no VARCHAR(50)
);

-- Route dimension
CREATE TABLE dim_route (
    route_id INT PRIMARY KEY,
    start_location VARCHAR(100),
    end_location VARCHAR(100),
    distance_km DECIMAL(6,2)
);

-- Time dimension
CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    delivery_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT
);

-- Fact Table
CREATE TABLE fact_delivery (
    delivery_id INT PRIMARY KEY AUTO_INCREMENT,
    vehicle_id INT,
    driver_id INT,
    route_id INT,
    time_id INT,
    fuel_used_liters DECIMAL(6,2),
    delivery_duration_minutes INT,
    delivery_status VARCHAR(20),
    FOREIGN KEY (vehicle_id) REFERENCES dim_vehicle(vehicle_id),
    FOREIGN KEY (driver_id) REFERENCES dim_driver(driver_id),
    FOREIGN KEY (route_id) REFERENCES dim_route(route_id),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id)
);

-- Sample Dimension Data
INSERT INTO dim_vehicle VALUES
(1,'QA-001','Truck'),
(2,'QA-002','Van');

INSERT INTO dim_driver VALUES
(1,'Ali','L12345'),
(2,'Sara','L67890');

INSERT INTO dim_route VALUES
(1,'Doha Warehouse','Al Wakrah Store',40.5),
(2,'Doha Warehouse','Al Khor Store',100.0);

INSERT INTO dim_time VALUES
(1,'2025-08-01',1,8,3,2025),
(2,'2025-08-02',2,8,3,2025);

-- Sample Fact Data (ETL applied: cleaned timestamps, calculated fuel)
INSERT INTO fact_delivery (vehicle_id, driver_id, route_id, time_id, fuel_used_liters, delivery_duration_minutes, delivery_status)
VALUES
(1,1,1,1,15.5,90,'Completed'),
(2,2,2,2,35.0,150,'Completed'),
(1,1,2,2,34.0,145,'Completed');

-- OLAP Queries

-- Total fuel usage per vehicle
SELECT v.vehicle_number, SUM(f.fuel_used_liters) AS total_fuel
FROM fact_delivery f
JOIN dim_vehicle v ON f.vehicle_id = v.vehicle_id
GROUP BY v.vehicle_number
ORDER BY total_fuel DESC;

-- Driver performance: total deliveries and avg duration
SELECT d.driver_name, COUNT(f.delivery_id) AS total_deliveries, AVG(f.delivery_duration_minutes) AS avg_duration
FROM fact_delivery f
JOIN dim_driver d ON f.driver_id = d.driver_id
GROUP BY d.driver_name
ORDER BY total_deliveries DESC;

-- Route-wise fuel efficiency
SELECT r.start_location, r.end_location, SUM(f.fuel_used_liters)/SUM(r.distance_km) AS fuel_per_km
FROM fact_delivery f
JOIN dim_route r ON f.route_id = r.route_id
GROUP BY r.start_location, r.end_location
ORDER BY fuel_per_km ASC;

-- Daily deliveries summary
SELECT t.delivery_date, COUNT(f.delivery_id) AS total_deliveries, SUM(f.fuel_used_liters) AS total_fuel
FROM fact_delivery f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.delivery_date
ORDER BY t.delivery_date;

-- OLAP analysis: identify routes with highest fuel consumption per distance
SELECT r.route_id, r.start_location, r.end_location, SUM(f.fuel_used_liters)/SUM(r.distance_km) AS fuel_per_km
FROM fact_delivery f
JOIN dim_route r ON f.route_id = r.route_id
GROUP BY r.route_id
ORDER BY fuel_per_km DESC;
