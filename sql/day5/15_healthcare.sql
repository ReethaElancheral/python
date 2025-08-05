--  15. Healthcare Prescription System 
-- Requirements: 
--  Tables: doctors, patients, prescriptions, medications 
--  Insert prescription with constraints on dosage range. 
--  Update medication stock. 
--  Delete prescriptions after 6 months. 
--  Add CHECK (dosage >= 1 AND dosage <= 5). 
--  Modify and drop NOT NULL on optional medication. 
--  Wrap full prescription process in a transaction.

-- Create Database
CREATE DATABASE IF NOT EXISTS HealthcareDB;
USE HealthcareDB;

-- Doctors Table
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100)
);

-- Patients Table
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    date_of_birth DATE
);

-- Medications Table
CREATE TABLE medications (
    medication_id INT AUTO_INCREMENT PRIMARY KEY,
    medication_name VARCHAR(100) NOT NULL,
    stock INT NOT NULL CHECK (stock >= 0),
    dosage_optional VARCHAR(100) NULL
);

-- Prescriptions Table
CREATE TABLE prescriptions (
    prescription_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_id INT,
    patient_id INT,
    medication_id INT,
    dosage INT CHECK (dosage >= 1 AND dosage <= 5),
    prescribed_date DATE DEFAULT (CURDATE()),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (medication_id) REFERENCES medications(medication_id)
);

-- Sample Inserts
INSERT INTO doctors (name, specialization) VALUES
('Dr. Asha Kumar', 'Cardiology'),
('Dr. Rajesh Singh', 'General Medicine');

INSERT INTO patients (name, date_of_birth) VALUES
('Neha Sharma', '1990-05-15'),
('Karan Verma', '1985-12-20');

INSERT INTO medications (medication_name, stock, dosage_optional) VALUES
('Paracetamol', 100, '500mg'),
('Amoxicillin', 50, NULL);

-- Insert prescription within valid dosage range
INSERT INTO prescriptions (doctor_id, patient_id, medication_id, dosage) VALUES
(1, 1, 1, 3),
(2, 2, 2, 2);

-- Update medication stock after prescription
UPDATE medications SET stock = stock - 1 WHERE medication_id = 1;

-- Delete prescriptions older than 6 months
DELETE FROM prescriptions WHERE prescribed_date < (CURDATE() - INTERVAL 6 MONTH);

-- Modify and drop NOT NULL on optional medication dosage_optional
ALTER TABLE medications MODIFY dosage_optional VARCHAR(100) NULL;

-- Transaction wrapping full prescription process
START TRANSACTION;

-- Insert new prescription
INSERT INTO prescriptions (doctor_id, patient_id, medication_id, dosage)
VALUES (1, 2, 1, 4);

-- Update stock
UPDATE medications SET stock = stock - 1 WHERE medication_id = 1;

-- Commit or rollback if stock < 0 (handle externally)
COMMIT;
