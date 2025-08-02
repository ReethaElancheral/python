CREATE DATABASE IF NOT EXISTS jobportal_db;
USE jobportal_db;

CREATE TABLE jobs (
    job_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    job_type ENUM('Full-Time', 'Internship'),
    company_id INT
);

CREATE TABLE applicants (
    applicant_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE applications (
    application_id INT AUTO_INCREMENT PRIMARY KEY,
    job_id INT,
    applicant_id INT,
    application_status ENUM('Shortlisted', 'Rejected', 'In Review'),
    application_date DATE,
    FOREIGN KEY (job_id) REFERENCES jobs(job_id),
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id)
);

CREATE TABLE companies (
    company_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

-- Sample data

INSERT INTO companies (name) VALUES ('Company A'), ('Company B');

INSERT INTO jobs (title, job_type, company_id) VALUES
('Software Engineer', 'Full-Time', 1),
('Marketing Intern', 'Internship', 2),
('Data Analyst', 'Full-Time', 1);

INSERT INTO applicants (name) VALUES ('Alice'), ('Bob'), ('Charlie');

INSERT INTO applications (job_id, applicant_id, application_status, application_date) VALUES
(1,1,'Shortlisted','2025-07-01'),
(2,1,'In Review','2025-07-05'),
(3,1,'Rejected','2025-07-10'),
(1,2,'In Review','2025-07-11'),
(2,2,'Rejected','2025-07-15'),
(3,3,'Shortlisted','2025-07-20');

-- Queries

-- 1. Subquery to show jobs applied by applicants with > 3 applications
SELECT * FROM applications WHERE applicant_id IN (
    SELECT applicant_id FROM applications GROUP BY applicant_id HAVING COUNT(*) > 3
);

-- 2. CASE to mark application status
SELECT
    application_id,
    application_status,
    CASE application_status
        WHEN 'Shortlisted' THEN 'Shortlisted'
        WHEN 'Rejected' THEN 'Rejected'
        WHEN 'In Review' THEN 'In Review'
        ELSE 'Unknown'
    END AS status_label
FROM applications;

-- 3. JOIN + GROUP BY to calculate applications per job
SELECT
    j.job_id,
    j.title,
    COUNT(a.application_id) AS application_count
FROM jobs j
LEFT JOIN applications a ON j.job_id = a.job_id
GROUP BY j.job_id, j.title;

-- 4. UNION to combine full-time and internship roles
SELECT job_id, title, 'Full-Time' AS job_type FROM jobs WHERE job_type = 'Full-Time'
UNION
SELECT job_id, title, 'Internship' AS job_type FROM jobs WHERE job_type = 'Internship';

-- 5. Correlated subquery to find most applied job per applicant
SELECT
    applicant_id,
    (SELECT job_id
     FROM applications a2
     WHERE a2.applicant_id = a.applicant_id
     GROUP BY job_id
     ORDER BY COUNT(*) DESC
     LIMIT 1) AS most_applied_job
FROM applications a
GROUP BY applicant_id;

-- 6. Date filter for recent applications (last 30 days)
SELECT * FROM applications WHERE application_date >= CURDATE() - INTERVAL 30 DAY;
