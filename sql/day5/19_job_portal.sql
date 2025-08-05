
-- Project 19: Job Portal and Applications

CREATE DATABASE IF NOT EXISTS JobPortalDB;
USE JobPortalDB;

CREATE TABLE recruiters (
    recruiter_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE jobs (
    job_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    recruiter_id INT,
    deadline DATE,
    FOREIGN KEY (recruiter_id) REFERENCES recruiters(recruiter_id)
);

CREATE TABLE applicants (
    applicant_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    experience INT CHECK (experience >= 0)
);

CREATE TABLE applications (
    app_id INT PRIMARY KEY AUTO_INCREMENT,
    job_id INT,
    applicant_id INT,
    status VARCHAR(50),
    UNIQUE (job_id, applicant_id),
    FOREIGN KEY (job_id) REFERENCES jobs(job_id),
    FOREIGN KEY (applicant_id) REFERENCES applicants(applicant_id)
);

-- Insert job application
INSERT INTO recruiters (name) VALUES ('TCS');
INSERT INTO jobs (title, recruiter_id, deadline) VALUES ('Python Developer', 1, '2025-12-31');
INSERT INTO applicants (name, experience) VALUES ('Sneha Rao', 2);

-- Transaction: post job + notify applicants
START TRANSACTION;
INSERT INTO applications (job_id, applicant_id, status) VALUES (1, 1, 'Applied');
UPDATE applications SET status = 'Interview' WHERE job_id = 1 AND applicant_id = 1;
COMMIT;

-- Delete past-deadline applications
DELETE FROM applications 
WHERE job_id IN (SELECT job_id FROM jobs WHERE deadline < CURDATE());
