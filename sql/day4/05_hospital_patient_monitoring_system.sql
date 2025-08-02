-- Project 5: Hospital Patient Monitoring System

CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- Tables
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE,
    admission_date DATE,
    discharge_date DATE
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(100)
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE treatments (
    treatment_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    treatment_date DATE,
    cost DECIMAL(10,2),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- Insert data
INSERT INTO patients VALUES
(1, 'John Doe', '1980-01-10', '2025-06-01', '2025-06-10'),
(2, 'Jane Smith', '1990-05-12', '2025-07-01', NULL),
(3, 'Emily Davis', '1975-08-23', '2025-07-05', '2025-07-15'),
(4, 'Michael Brown', '1985-03-14', '2025-06-15', '2025-06-20'),
(5, 'Laura Wilson', '1992-11-30', '2025-07-10', NULL);

INSERT INTO doctors VALUES
(1, 'Dr. Adams', 'Cardiology'),
(2, 'Dr. Baker', 'Neurology'),
(3, 'Dr. Clark', 'Orthopedics');

INSERT INTO appointments VALUES
(1, 1, 1, '2025-06-02'),
(2, 2, 2, '2025-07-02'),
(3, 3, 1, '2025-07-06'),
(4, 4, 3, '2025-06-16'),
(5, 5, 2, '2025-07-11');

INSERT INTO treatments VALUES
(1, 1, 1, '2025-06-03', 1200.00),
(2, 1, 1, '2025-06-05', 800.00),
(3, 2, 2, '2025-07-03', 1500.00),
(4, 3, 1, '2025-07-07', 2000.00),
(5, 4, 3, '2025-06-17', 500.00),
(6, 5, 2, '2025-07-12', 700.00),
(7, 1, 1, '2025-06-07', 400.00);

-- Subquery in FROM to calculate total patients per doctor
SELECT d.name AS doctor_name, patient_count
FROM doctors d
JOIN (
    SELECT doctor_id, COUNT(DISTINCT patient_id) AS patient_count
    FROM treatments
    GROUP BY doctor_id
) AS t ON d.doctor_id = t.doctor_id;

-- Subquery in WHERE to get patients treated more than 3 times
SELECT name FROM patients
WHERE patient_id IN (
    SELECT patient_id FROM treatments
    GROUP BY patient_id
    HAVING COUNT(treatment_id) > 3
);

-- CASE to flag "Critical" patients based on treatment count or bill amount
SELECT p.name,
    CASE
        WHEN treatment_count > 3 OR total_cost > 3000 THEN 'Critical'
        ELSE 'Stable'
    END AS patient_status
FROM (
    SELECT patient_id, COUNT(*) AS treatment_count, SUM(cost) AS total_cost
    FROM treatments
    GROUP BY patient_id
) AS t
JOIN patients p ON t.patient_id = p.patient_id;

-- Correlated subquery to find patient with longest hospital stay per department
SELECT d.department, p.name, DATEDIFF(p.discharge_date, p.admission_date) AS stay_duration
FROM doctors d
JOIN treatments t ON d.doctor_id = t.doctor_id
JOIN patients p ON t.patient_id = p.patient_id
WHERE p.discharge_date IS NOT NULL
AND DATEDIFF(p.discharge_date, p.admission_date) = (
    SELECT MAX(DATEDIFF(p2.discharge_date, p2.admission_date))
    FROM treatments t2
    JOIN patients p2 ON t2.patient_id = p2.patient_id
    WHERE t2.doctor_id = d.doctor_id AND p2.discharge_date IS NOT NULL
)
GROUP BY d.department;

-- Date functions to find patients treated in last 30 days
SELECT DISTINCT p.name
FROM patients p
JOIN treatments t ON p.patient_id = t.patient_id
WHERE t.treatment_date >= CURDATE() - INTERVAL 30 DAY;

-- UNION to combine outpatient and inpatient records
-- Assuming outpatient and inpatient tables (simulate by filtering patients)
SELECT patient_id, name, 'Outpatient' AS patient_type FROM patients WHERE discharge_date IS NOT NULL
UNION
SELECT patient_id, name, 'Inpatient' AS patient_type FROM patients WHERE discharge_date IS NULL;
