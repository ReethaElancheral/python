--  3. Healthcare Patient Visit Analytics 
-- Requirements: 
--  OLTP: appointments, doctors, patients, departments. 
--  Create a Star Schema with fact_visits, dim_time, dim_doctor, dim_patient. 
--  ETL process to clean records and compute wait times. 
--  OLAP reports: average wait time per doctor, department traffic. 
--  Compare OLAP summaries to granular OLTP logs.

-- Create Database
CREATE DATABASE IF NOT EXISTS HealthcareWarehouse;
USE HealthcareWarehouse;

-- Dimension Tables
CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    appointment_date DATE,
    day INT,
    month INT,
    quarter INT,
    year INT
);

CREATE TABLE dim_doctor (
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(100),
    specialization VARCHAR(50),
    department_id INT
);

CREATE TABLE dim_patient (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE dim_department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Fact Table
CREATE TABLE fact_visits (
    visit_id INT PRIMARY KEY AUTO_INCREMENT,
    time_id INT,
    doctor_id INT,
    patient_id INT,
    department_id INT,
    appointment_time TIME,
    arrival_time TIME,
    wait_minutes INT,
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (doctor_id) REFERENCES dim_doctor(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES dim_patient(patient_id),
    FOREIGN KEY (department_id) REFERENCES dim_department(department_id)
);

-- Sample Dimension Data
INSERT INTO dim_department VALUES
(1,'Cardiology'),
(2,'Neurology');

INSERT INTO dim_doctor VALUES
(1,'Dr. Alice','Cardiologist',1),
(2,'Dr. Bob','Neurologist',2);

INSERT INTO dim_patient VALUES
(1,'John Doe',45,'M'),
(2,'Jane Smith',30,'F');

INSERT INTO dim_time VALUES
(1,'2025-08-01',1,8,3,2025),
(2,'2025-08-02',2,8,3,2025);

-- Sample Fact Data (ETL processed)
INSERT INTO fact_visits (time_id, doctor_id, patient_id, department_id, appointment_time, arrival_time, wait_minutes)
VALUES
(1,1,1,1,'09:00:00','09:10:00',10),
(1,2,2,2,'10:00:00','10:05:00',5),
(2,1,2,1,'11:00:00','11:15:00',15);

-- OLAP Queries

-- Average Wait Time per Doctor
SELECT d.doctor_name, AVG(f.wait_minutes) AS avg_wait_time
FROM fact_visits f
JOIN dim_doctor d ON f.doctor_id = d.doctor_id
GROUP BY d.doctor_name;

-- Department Traffic (number of visits per department)
SELECT dep.department_name, COUNT(f.visit_id) AS total_visits
FROM fact_visits f
JOIN dim_department dep ON f.department_id = dep.department_id
GROUP BY dep.department_name;

-- Monthly Visits per Department
SELECT t.year, t.month, dep.department_name, COUNT(f.visit_id) AS visits
FROM fact_visits f
JOIN dim_time t ON f.time_id = t.time_id
JOIN dim_department dep ON f.department_id = dep.department_id
GROUP BY t.year, t.month, dep.department_name
ORDER BY t.year, t.month, dep.department_name;

-- Compare OLAP summaries vs raw OLTP (example: average wait per doctor)
-- Assuming OLTP table: appointments
-- CREATE TABLE appointments (appointment_id, doctor_id, patient_id, scheduled_time, arrival_time);
-- SELECT doctor_id, AVG(TIMESTAMPDIFF(MINUTE, scheduled_time, arrival_time)) AS avg_wait
-- FROM appointments GROUP BY doctor_id;
