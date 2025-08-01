-- Project 10: Sales Team CRM Dashboard

CREATE DATABASE IF NOT EXISTS sales_crm_db;
USE sales_crm_db;

-- Tables

CREATE TABLE sales_reps (
    rep_id INT PRIMARY KEY,
    name VARCHAR(100),
    region VARCHAR(100)
);

CREATE TABLE leads (
    lead_id INT PRIMARY KEY,
    rep_id INT,
    client_name VARCHAR(100),
    status VARCHAR(50),
    conversion_days INT,
    FOREIGN KEY (rep_id) REFERENCES sales_reps(rep_id)
);

CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    name VARCHAR(100),
    region VARCHAR(100),
    rep_id INT,
    FOREIGN KEY (rep_id) REFERENCES sales_reps(rep_id)
);

CREATE TABLE meetings (
    meeting_id INT PRIMARY KEY,
    client_id INT,
    rep_id INT,
    meeting_date DATE,
    notes TEXT,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (rep_id) REFERENCES sales_reps(rep_id)
);

-- Sample Data

INSERT INTO sales_reps (rep_id, name, region) VALUES
(1, 'Amit Sharma', 'North'),
(2, 'Riya Mehra', 'South'),
(3, 'Karan Sethi', 'East'),
(4, 'Neha Verma', 'West');

INSERT INTO leads (lead_id, rep_id, client_name, status, conversion_days) VALUES
(1, 1, 'Alpha Corp', 'Closed', 12),
(2, 1, 'Beta Ltd', 'Closed', 18),
(3, 2, 'Gamma Pvt Ltd', 'Open', NULL),
(4, 2, 'Delta Inc', 'Closed', 9),
(5, 3, 'Epsilon Co', 'Closed', 15),
(6, 3, 'Zeta Works', 'Closed', 8),
(7, 3, 'Eta Systems', 'Closed', 10),
(8, 3, 'Theta Networks', 'Closed', 7),
(9, 3, 'Iota Group', 'Closed', 14),
(10, 3, 'Kappa Tech', 'Closed', 11);

INSERT INTO clients (client_id, name, region, rep_id) VALUES
(1, 'Alpha Corp', 'North', 1),
(2, 'Beta Ltd', 'North', 1),
(3, 'Delta Inc', 'South', 2),
(4, 'Epsilon Co', 'East', 3),
(5, 'Zeta Works', 'East', 3),
(6, 'Mu Holdings', 'South', NULL);  -- Client with no rep

INSERT INTO meetings (meeting_id, client_id, rep_id, meeting_date, notes) VALUES
(1, 1, 1, '2024-01-12', 'Initial discussion'),
(2, 2, 1, '2024-01-20', 'Follow-up call'),
(3, 3, 2, '2024-02-01', 'Contract negotiation'),
(4, 4, 3, '2024-02-10', 'Demo session'),
(5, 5, 3, '2024-02-15', 'Feedback meeting');

-- Queries

-- 1. Count leads per sales rep
SELECT 
    sr.name AS rep_name,
    COUNT(l.lead_id) AS total_leads
FROM sales_reps sr
LEFT JOIN leads l ON sr.rep_id = l.rep_id
GROUP BY sr.rep_id, sr.name;

-- 2. Average conversion time
SELECT 
    sr.name AS rep_name,
    AVG(l.conversion_days) AS avg_conversion_days
FROM sales_reps sr
JOIN leads l ON sr.rep_id = l.rep_id
WHERE l.conversion_days IS NOT NULL
GROUP BY sr.rep_id, sr.name;

-- 3. Reps who closed more than 5 deals
SELECT 
    sr.name,
    COUNT(l.lead_id) AS deals_closed
FROM sales_reps sr
JOIN leads l ON sr.rep_id = l.rep_id
WHERE l.status = 'Closed'
GROUP BY sr.rep_id, sr.name
HAVING deals_closed > 5;

-- 4. INNER JOIN reps and leads
SELECT 
    sr.name AS rep_name,
    l.client_name,
    l.status
FROM sales_reps sr
INNER JOIN leads l ON sr.rep_id = l.rep_id;

-- 5. RIGHT JOIN: reps and clients
SELECT 
    c.name AS client_name,
    sr.name AS rep_name
FROM clients c
RIGHT JOIN sales_reps sr ON c.rep_id = sr.rep_id;

-- 6. SELF JOIN to compare reps from the same region
SELECT 
    r1.name AS rep1,
    r2.name AS rep2,
    r1.region
FROM sales_reps r1
JOIN sales_reps r2 ON r1.region = r2.region AND r1.rep_id < r2.rep_id;
