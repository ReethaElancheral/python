-- 1. Hospital Management System 
-- Requirements: 
--  Tables: patients, doctors, appointments, departments 
--  INSERT new patient details with NOT NULL constraints. 
--  Use FOREIGN KEY from appointments → doctors. 
--  Update doctor specialization and department ID. 
--  Delete a patient record and all associated appointments. 
--  Add a CHECK constraint for patient age between 0 and 120. 
--  Use a SAVEPOINT before deleting a patient, and ROLLBACK if needed. 
--  Demonstrate atomicity when updating both doctor and appointment info in 
-- a transaction.

-- Create Database
CREATE DATABASE IF NOT EXISTS HospitalDB;
USE HospitalDB;

-- Create Departments Table
CREATE TABLE departments (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

-- Create Doctors Table
CREATE TABLE doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    doctor_name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create Patients Table with CHECK constraint for age (0-120)
CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    age INT NOT NULL CHECK (age BETWEEN 0 AND 120),
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact VARCHAR(15) NOT NULL
);

-- Create Appointments Table
CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- Insert sample data into departments
INSERT INTO departments (department_name) VALUES
('Cardiology'), ('Neurology'), ('Orthopedics'), ('Pediatrics');

-- Insert sample data into doctors
INSERT INTO doctors (doctor_name, specialization, department_id) VALUES
('Dr. Alice Smith', 'Cardiologist', 1),
('Dr. Bob Jones', 'Neurologist', 2),
('Dr. Carol White', 'Orthopedic Surgeon', 3),
('Dr. David Black', 'Pediatrician', 4);

-- Insert sample patients (with NOT NULL constraints enforced)
INSERT INTO patients (patient_name, age, gender, contact) VALUES
('John Doe', 35, 'Male', '1234567890'),
('Jane Roe', 28, 'Female', '0987654321');

-- Insert sample appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time) VALUES
(1, 1, '2025-08-10', '10:30:00'),
(2, 4, '2025-08-11', '14:00:00');

-- Update doctor specialization and department ID example
UPDATE doctors
SET specialization = 'Interventional Cardiologist', department_id = 1
WHERE doctor_id = 1;

-- Demonstrate SAVEPOINT and ROLLBACK when deleting a patient and associated appointments

START TRANSACTION;

SAVEPOINT before_delete_patient;

DELETE FROM patients WHERE patient_id = 2;

-- ROLLBACK TO SAVEPOINT before_delete_patient;

-- Commit if everything is fine
COMMIT;

-- Demonstrate atomicity in updating doctor and appointment info in a transaction
START TRANSACTION;

UPDATE doctors
SET specialization = 'Senior Cardiologist'
WHERE doctor_id = 1;

UPDATE appointments
SET appointment_date = '2025-08-15', appointment_time = '11:00:00'
WHERE doctor_id = 1 AND patient_id = 1;


COMMIT;


