
-- 3. Hospital Patient Record System 
-- Requirements: 
--  Tables: patients, appointments, doctors, departments, medications 
--  Normalize data to 3NF; separate patient and visit details. 
--  Index appointment_date, patient_id, and doctor_id. 
--  Analyze execution plan for frequent appointment lookups. 
--  Use subqueries to find patients with the most visits. 
--  Create a denormalized view for dashboard analytics. 
--  Add LIMIT to retrieve last 5 appointments for a patient.


CREATE DATABASE IF NOT EXISTS HospitalDB;
USE HospitalDB;

-- Normalized Tables
CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    dob DATE,
    gender ENUM('M','F','Other')
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100)
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    reason VARCHAR(255),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE medications (
    medication_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    medication_name VARCHAR(100),
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- Indexing
CREATE INDEX idx_appt_date ON appointments(appointment_date);
CREATE INDEX idx_patient_id ON appointments(patient_id);
CREATE INDEX idx_doctor_id ON appointments(doctor_id);

-- Execution plan
EXPLAIN SELECT * FROM appointments WHERE appointment_date = CURDATE();

-- Subquery for most visited patients
SELECT patient_id, COUNT(*) AS total_visits
FROM appointments
GROUP BY patient_id
ORDER BY total_visits DESC
LIMIT 5;

-- Denormalized view for dashboard
CREATE VIEW patient_dashboard AS
SELECT p.patient_id, p.name, COUNT(a.appointment_id) AS total_appointments,
       GROUP_CONCAT(DISTINCT m.medication_name) AS meds
FROM patients p
LEFT JOIN appointments a ON p.patient_id = a.patient_id
LEFT JOIN medications m ON p.patient_id = m.patient_id
GROUP BY p.patient_id;

-- Retrieve last 5 appointments for a patient
SELECT * FROM appointments WHERE patient_id = 1 ORDER BY appointment_date DESC LIMIT 5;