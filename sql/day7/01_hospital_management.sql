--  1. Hospital Management System 
-- Requirements: 
--  Use a view view_patient_summary to show name, age, and latest 
-- appointment (hide billing). 
--  Create a stored procedure add_patient_visit() to add a visit and auto-log it. 
--  Use a function get_doctor_schedule() to retrieve appointments for a 
-- doctor. 
--  Trigger after_insert_appointment to update availability in the doctors 
-- table. 
--  Use abstraction: restrict non-admin users to views (not raw tables). 

CREATE DATABASE IF NOT EXISTS HospitalDB;
USE HospitalDB;

-- Table Definitions
CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE doctors (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    specialization VARCHAR(50),
    availability_status VARCHAR(20) DEFAULT 'Available'
);

CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    doctor_id INT,
    appointment_date DATETIME,
    notes TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

CREATE TABLE visits (
    visit_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    visit_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    reason TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

-- View: view_patient_summary
CREATE OR REPLACE VIEW view_patient_summary AS
SELECT 
    p.patient_id,
    p.name,
    p.age,
    (SELECT a.appointment_date 
     FROM appointments a 
     WHERE a.patient_id = p.patient_id 
     ORDER BY a.appointment_date DESC 
     LIMIT 1) AS latest_appointment
FROM patients p;

-- Stored Procedure: add_patient_visit
DELIMITER $$
CREATE PROCEDURE add_patient_visit(
    IN p_patient_id INT,
    IN p_reason TEXT
)
BEGIN
    INSERT INTO visits(patient_id, reason)
    VALUES (p_patient_id, p_reason);
END $$
DELIMITER ;

-- Function: get_doctor_schedule
DELIMITER $$
CREATE FUNCTION get_doctor_schedule(p_doctor_id INT)
RETURNS TEXT
DETERMINISTIC
BEGIN
    DECLARE schedule TEXT;
    SELECT GROUP_CONCAT(DATE_FORMAT(appointment_date, '%Y-%m-%d %H:%i'))
    INTO schedule
    FROM appointments
    WHERE doctor_id = p_doctor_id
    ORDER BY appointment_date;
    RETURN schedule;
END $$
DELIMITER ;

-- Trigger: after_insert_appointment
DELIMITER $$
CREATE TRIGGER after_insert_appointment
AFTER INSERT ON appointments
FOR EACH ROW
BEGIN
    UPDATE doctors 
    SET availability_status = 'Busy'
    WHERE doctor_id = NEW.doctor_id;
END $$
DELIMITER ;

-- Optional: Abstraction (restricting access)
-- Create a limited access view for non-admins
CREATE OR REPLACE VIEW view_limited_patient_summary AS
SELECT patient_id, name, age FROM patients;


