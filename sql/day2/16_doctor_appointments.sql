-- Project 16: Doctor Appointment Records
CREATE TABLE appointments (
    appointment_id INT PRIMARY KEY,
    patient_name VARCHAR(100),
    doctor_name VARCHAR(100),
    date DATE,
    status VARCHAR(20),
    notes TEXT
);

INSERT INTO appointments (appointment_id, patient_name, doctor_name, date, status, notes) VALUES
(1, 'Amit Shah', 'Dr. Kumar', '2025-07-20', 'Confirmed', 'First-time visit'),
(2, 'Neha Gupta', 'Dr. Singh', '2025-07-22', 'Cancelled', NULL),
(3, 'Raj Patel', 'Dr. Kumar', '2025-07-25', 'Confirmed', 'Follow-up'),
(4, 'Sonal Mehta', 'Dr. Iyer', '2025-07-23', 'Pending', 'Requires tests'),
(5, 'Vikram Rao', 'Dr. Singh', '2025-07-24', 'Confirmed', NULL);

SELECT doctor_name, date, status FROM appointments WHERE date BETWEEN CURDATE() - INTERVAL 7 DAY AND CURDATE();
SELECT * FROM appointments WHERE patient_name LIKE '%th%';
SELECT * FROM appointments WHERE notes IS NULL;
SELECT DISTINCT doctor_name FROM appointments;
SELECT * FROM appointments ORDER BY date DESC;