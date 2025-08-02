-- 3. Hospital Patient Visit Tracker
-- Requirements:
-- Tables: patients, doctors, appointments, departments.
-- Use LEFT JOIN to show all patients, even those with no appointments.
-- Filter data using BETWEEN for date range of visits.
-- Aggregate visit counts per department.
-- Use FULL OUTER JOIN to get all appointments and doctors, even if missing.
-- Use subquery in FROM to summarize daily appointments.
-- Use CASE to flag emergency vs. routine.
-- Combine regular and emergency visits using UNION.


CREATE DATABASE IF NOT EXISTS HospitalDB;
USE HospitalDB;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    specialization VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    gender ENUM('Male', 'Female'),
    age INT
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    type ENUM('regular', 'emergency'),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- Insert Sample Data

INSERT INTO departments (name) VALUES
('Cardiology'),
('Neurology'),
('Orthopedics'),
('Pediatrics');

INSERT INTO doctors (name, specialization, dept_id) VALUES
('Dr. Mehta', 'Cardiologist', 1),
('Dr. Verma', 'Neurologist', 2),
('Dr. Iyer', 'Orthopedic Surgeon', 3),
('Dr. Shah', 'Pediatrician', 4);

INSERT INTO patients (name, gender, age) VALUES
('Aarav Singh', 'Male', 30),
('Neha Reddy', 'Female', 25),
('John Abraham', 'Male', 45),
('Kavya Das', 'Female', 10),
('Mohan Kumar', 'Male', 55);

INSERT INTO appointments (patient_id, doctor_id, appointment_date, type) VALUES
(1, 1, '2025-07-10', 'regular'),
(2, 2, '2025-07-11', 'emergency'),
(3, 1, '2025-07-12', 'regular'),
(4, 4, '2025-07-13', 'regular'),
(5, 3, '2025-07-14', 'emergency');

-- 1. LEFT JOIN to show all patients, even those with no appointments
SELECT p.patient_id, p.name AS patient_name, a.appointment_date, a.type
FROM patients p
LEFT JOIN appointments a ON p.patient_id = a.patient_id;

-- 2. Filter data using BETWEEN for date range of visits
SELECT a.appointment_id, p.name AS patient_name, a.appointment_date
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
WHERE a.appointment_date BETWEEN '2025-07-11' AND '2025-07-13';

-- 3. Aggregate visit counts per department
SELECT d.name AS department_name, COUNT(a.appointment_id) AS total_visits
FROM appointments a
JOIN doctors doc ON a.doctor_id = doc.doctor_id
JOIN departments d ON doc.dept_id = d.dept_id
GROUP BY d.name;

-- 4. FULL OUTER JOIN (simulated using UNION of LEFT and RIGHT JOINs)
SELECT a.appointment_id, a.appointment_date, d.doctor_id, d.name AS doctor_name
FROM appointments a
LEFT JOIN doctors d ON a.doctor_id = d.doctor_id

UNION

SELECT a.appointment_id, a.appointment_date, d.doctor_id, d.name AS doctor_name
FROM appointments a
RIGHT JOIN doctors d ON a.doctor_id = d.doctor_id;

-- 5. Subquery in FROM to summarize daily appointments
SELECT daily.appointment_date, COUNT(daily.appointment_id) AS total_appointments
FROM (
    SELECT appointment_id, appointment_date
    FROM appointments
) AS daily
GROUP BY daily.appointment_date;

-- 6. CASE to flag emergency vs. routine
SELECT a.appointment_id, p.name AS patient_name, a.appointment_date,
       CASE
           WHEN a.type = 'emergency' THEN 'Emergency Visit'
           ELSE 'Routine Visit'
       END AS visit_type
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id;

-- 7. Combine regular and emergency visits using UNION
SELECT a.appointment_id, p.name AS patient_name, a.appointment_date, 'Regular' AS visit_type
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
WHERE a.type = 'regular'

UNION

SELECT a.appointment_id, p.name, a.appointment_date, 'Emergency'
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
WHERE a.type = 'emergency';
