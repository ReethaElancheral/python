-- -----------------------------------------------
-- Project 8: Hospital Appointment Booking
-- Requirements:
-- • Create hospital_db
-- • Tables: patients, doctors, appointments, departments
-- • Each appointment links a patient and a doctor
-- • Insert 10 doctors, 15 patients, 20 appointments
-- • SELECT queries:
--     - Find appointments by date
--     - Find doctors by department
--     - Count patients per doctor
-- -----------------------------------------------

-- Create database
CREATE DATABASE IF NOT EXISTS hospital_db;
USE hospital_db;

-- Create departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

-- Create doctors table
CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

-- Create patients table
CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    dob DATE
);

-- Create appointments table
CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

-- Insert departments
INSERT INTO departments (name) VALUES
('Cardiology'), ('Neurology'), ('Orthopedics'), ('Pediatrics'), ('General Medicine');

-- Insert doctors
INSERT INTO doctors (name, department_id) VALUES
('Dr. Smith', 1),
('Dr. Brown', 2),
('Dr. Johnson', 3),
('Dr. Patel', 4),
('Dr. Kumar', 5),
('Dr. Lee', 1),
('Dr. Gupta', 2),
('Dr. Adams', 3),
('Dr. Shah', 4),
('Dr. Wilson', 5);

-- Insert patients
INSERT INTO patients (name, dob) VALUES
('Alice', '1990-01-15'),
('Bob', '1985-03-20'),
('Carol', '1992-07-25'),
('David', '2000-11-30'),
('Eva', '1995-06-18'),
('Frank', '1988-04-10'),
('Grace', '1993-12-22'),
('Hannah', '1999-09-09'),
('Ian', '2001-02-17'),
('Jane', '1996-10-05'),
('Karan', '1983-08-12'),
('Lina', '1997-03-28'),
('Mira', '1994-12-01'),
('Nathan', '1989-07-07'),
('Olivia', '2002-05-14');

-- Insert appointments
INSERT INTO appointments (patient_id, doctor_id, appointment_date, notes) VALUES
(1, 1, '2025-07-30', 'Follow-up for chest pain'),
(2, 2, '2025-07-30', 'Headache evaluation'),
(3, 3, '2025-07-31', 'Knee injury'),
(4, 4, '2025-08-01', 'Routine child check-up'),
(5, 5, '2025-08-01', 'Fever'),
(6, 6, '2025-08-02', 'Blood pressure check'),
(7, 7, '2025-08-02', 'Seizure follow-up'),
(8, 8, '2025-08-03', 'Fracture follow-up'),
(9, 9, '2025-08-03', 'Vaccination'),
(10, 10, '2025-08-04', 'General consultation'),
(11, 1, '2025-08-04', 'Cardiac check-up'),
(12, 2, '2025-08-05', 'Migraine'),
(13, 3, '2025-08-06', 'Joint pain'),
(14, 4, '2025-08-06', 'Child cough'),
(15, 5, '2025-08-07', 'General fever'),
(1, 6, '2025-08-07', 'ECG review'),
(2, 7, '2025-08-08', 'Neurological test'),
(3, 8, '2025-08-08', 'Leg sprain'),
(4, 9, '2025-08-09', 'Child growth consult'),
(5, 10, '2025-08-09', 'Cold and cough');

-- -----------------------------------------------
-- 📊 Required SELECT Queries
-- -----------------------------------------------

-- 1. Find appointments by date (e.g., for 2025-08-01)
SELECT 
    a.appointment_id,
    a.appointment_date,
    p.name AS patient_name,
    d.name AS doctor_name
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN doctors d ON a.doctor_id = d.doctor_id
WHERE a.appointment_date = '2025-08-01';

-- 2. Find doctors by department (e.g., 'Cardiology')
SELECT 
    d.name AS doctor_name,
    dept.name AS department_name
FROM doctors d
JOIN departments dept ON d.department_id = dept.department_id
WHERE dept.name = 'Cardiology';

-- 3. Count patients per doctor
SELECT 
    doc.name AS doctor_name,
    COUNT(app.patient_id) AS patient_count
FROM doctors doc
LEFT JOIN appointments app ON doc.doctor_id = app.doctor_id
GROUP BY doc.doctor_id;
