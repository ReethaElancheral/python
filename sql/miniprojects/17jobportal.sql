-- -----------------------------------------------
-- Project 17: Job Portal
-- Requirements:
-- • Create job_portal_db
-- • Tables: jobs, applicants, applications, companies
-- • Many-to-many between jobs and applicants
-- • Insert 10 job listings, 5 companies, 15 applications
-- • SQL:
--    - Find all jobs a user has applied for
--    - Count applications per company
-- -----------------------------------------------

CREATE DATABASE IF NOT EXISTS job_portal_db;
USE job_portal_db;

-- Companies table
CREATE TABLE companies (
    company_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    location VARCHAR(150)
);

-- Jobs table
CREATE TABLE jobs (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    company_id INT,
    title VARCHAR(150) NOT NULL,
    description TEXT,
    posted_date DATE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

-- Applicants table
CREATE TABLE applicants (
    applicant_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Applications table (many-to-many between jobs and applicants)
CREATE TABLE applications (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    job_id INT,
    applicant_id INT,
    application_date DATE,
    status ENUM('Pending', 'Accepted', 'Rejected') DEFAULT 'Pending',
    FOREIGN KEY (job_id) REFERENCES jobs(job_id),
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id)
);

-- Insert companies (5)
INSERT INTO companies (name, location) VALUES
('Tech Innovators', 'New York'),
('Health Solutions', 'San Francisco'),
('EduTech', 'Boston'),
('Finance Corp', 'Chicago'),
('Retail Experts', 'Seattle');

-- Insert jobs (10)
INSERT INTO jobs (company_id, title, description, posted_date) VALUES
(1, 'Software Engineer', 'Develop and maintain software.', '2025-06-01'),
(1, 'Data Scientist', 'Analyze data and build models.', '2025-06-05'),
(2, 'Nurse', 'Provide patient care.', '2025-06-10'),
(2, 'Medical Assistant', 'Support medical staff.', '2025-06-15'),
(3, 'Teacher', 'Teach math and science.', '2025-06-20'),
(3, 'Curriculum Developer', 'Develop educational content.', '2025-06-25'),
(4, 'Financial Analyst', 'Analyze financial data.', '2025-07-01'),
(4, 'Accountant', 'Manage accounts.', '2025-07-05'),
(5, 'Store Manager', 'Manage retail operations.', '2025-07-10'),
(5, 'Sales Associate', 'Sell products to customers.', '2025-07-15');

-- Insert applicants (5)
INSERT INTO applicants (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com'),
('Eva', 'eva@example.com');

-- Insert applications (15)
INSERT INTO applications (job_id, applicant_id, application_date, status) VALUES
(1, 1, '2025-06-10', 'Pending'),
(2, 1, '2025-06-12', 'Accepted'),
(3, 2, '2025-06-15', 'Pending'),
(4, 2, '2025-06-18', 'Rejected'),
(5, 3, '2025-06-20', 'Pending'),
(6, 3, '2025-06-22', 'Pending'),
(7, 4, '2025-07-01', 'Accepted'),
(8, 4, '2025-07-02', 'Pending'),
(9, 5, '2025-07-10', 'Pending'),
(10, 5, '2025-07-12', 'Pending'),
(1, 3, '2025-06-15', 'Pending'),
(2, 4, '2025-06-20', 'Rejected'),
(3, 5, '2025-06-25', 'Pending'),
(4, 1, '2025-06-28', 'Pending'),
(5, 2, '2025-07-01', 'Pending');

-- -----------------------------------------------
-- Queries
-- -----------------------------------------------

-- 1. Find all jobs a user (applicant) has applied for
-- Example: for applicant with id = 1 (Alice)
SELECT 
    a.name AS applicant_name,
    j.title AS job_title,
    c.name AS company_name,
    app.application_date,
    app.status
FROM applications app
JOIN applicants a ON app.applicant_id = a.applicant_id
JOIN jobs j ON app.job_id = j.job_id
JOIN companies c ON j.company_id = c.company_id
WHERE a.applicant_id = 1
ORDER BY app.application_date DESC;

-- 2. Count applications per company
SELECT 
    c.name AS company_name,
    COUNT(app.application_id) AS total_applications
FROM companies c
JOIN jobs j ON c.company_id = j.company_id
LEFT JOIN applications app ON j.job_id = app.job_id
GROUP BY c.company_id
ORDER BY total_applications DESC;
