-- Project 4: Hospital Patient Records

CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- Tables
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    name VARCHAR(100),
    birth_date DATE
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY,
    name VARCHAR(100)
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
    appointment_id INT,
    treatment_name VARCHAR(100),
    cost DECIMAL(10,2),
    FOREIGN KEY (appointment_id) REFERENCES appointments(appointment_id)
);


INSERT INTO patients (patient_id, name, birth_date) VALUES
(1, 'John Doe', '1980-01-01'),
(2, 'Jane Smith', '1985-02-02'),
(3, 'Emily Davis', '1990-03-03'),
(4, 'Michael Brown', '1980-01-01');  -- same birthdate as John


INSERT INTO doctors (doctor_id, name) VALUES
(1, 'Dr. Adams'),
(2, 'Dr. Baker'),
(3, 'Dr. Clark');


INSERT INTO appointments (appointment_id, patient_id, doctor_id, appointment_date) VALUES
(1, 1, 1, '2025-07-01'),
(2, 2, 1, '2025-07-02'),
(3, 3, 2, '2025-07-03'),
(4, 4, 3, '2025-07-04'),
(5, 1, 2, '2025-07-05');


INSERT INTO treatments (treatment_id, appointment_id, treatment_name, cost) VALUES
(1, 1, 'X-ray', 1000),
(2, 2, 'MRI', 2500),
(3, 3, 'Physical Therapy', 1500),
(4, 4, 'Surgery', 5000),
(5, 5, 'Consultation', 500);


-- Total patients treated per doctor (COUNT)
SELECT d.name AS doctor_name, COUNT(DISTINCT a.patient_id) AS patient_count
FROM doctors d
LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id;

-- Average treatment cost per doctor (AVG)
SELECT d.name AS doctor_name, AVG(t.cost) AS avg_treatment_cost
FROM doctors d
LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
LEFT JOIN treatments t ON a.appointment_id = t.appointment_id
GROUP BY d.doctor_id;

-- Doctors who treated more than 10 patients (HAVING)
SELECT d.name AS doctor_name, COUNT(DISTINCT a.patient_id) AS patient_count
FROM doctors d
LEFT JOIN appointments a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id
HAVING patient_count > 10;

-- INNER JOIN: Appointments + Doctors
SELECT a.appointment_id, p.name AS patient_name, d.name AS doctor_name, a.appointment_date
FROM appointments a
INNER JOIN doctors d ON a.doctor_id = d.doctor_id
INNER JOIN patients p ON a.patient_id = p.patient_id;

-- RIGHT JOIN: All doctors, including those with no appointments
SELECT d.name AS doctor_name, a.appointment_id
FROM appointments a
RIGHT JOIN doctors d ON a.doctor_id = d.doctor_id
ORDER BY d.name;

-- SELF JOIN on patients to find those with same birth date
SELECT p1.name AS patient1, p2.name AS patient2, p1.birth_date
FROM patients p1
INNER JOIN patients p2 ON p1.birth_date = p2.birth_date AND p1.patient_id <> p2.patient_id
ORDER BY p1.birth_date;