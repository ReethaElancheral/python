CREATE DATABASE IF NOT EXISTS insurance_db;
USE insurance_db;

CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    insurance_type VARCHAR(100)
);

CREATE TABLE agents (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE claims (
    claim_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT,
    agent_id INT,
    claim_amount DECIMAL(10,2),
    claim_status ENUM('Approved', 'Pending', 'Rejected'),
    claim_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    claim_id INT,
    payment_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (claim_id) REFERENCES claims(claim_id)
);

-- Sample data

INSERT INTO clients (name, insurance_type) VALUES
('John Doe', 'Health'),
('Jane Smith', 'Auto'),
('Bob Brown', 'Life');

INSERT INTO agents (name) VALUES ('Agent A'), ('Agent B');

INSERT INTO claims (client_id, agent_id, claim_amount, claim_status, claim_date) VALUES
(1, 1, 5000, 'Approved', '2025-07-01'),
(2, 2, 15000, 'Pending', '2025-06-15'),
(3, 1, 7000, 'Rejected', '2025-05-20');

INSERT INTO payments (claim_id, payment_date, amount) VALUES
(1, '2025-07-05', 5000),
(2, '2025-06-20', 0);

-- Queries

-- 1. Subquery to calculate average claim per insurance type
SELECT
    insurance_type,
    AVG(claim_amount) AS avg_claim_amount
FROM clients c
JOIN claims cl ON c.client_id = cl.client_id
GROUP BY insurance_type;

-- 2. CASE to show claim status
SELECT
    claim_id,
    claim_status,
    CASE
        WHEN claim_status = 'Approved' THEN 'Approved'
        WHEN claim_status = 'Pending' THEN 'Pending'
        WHEN claim_status = 'Rejected' THEN 'Rejected'
        ELSE 'Unknown'
    END AS claim_status_desc
FROM claims;

-- 3. UNION ALL for old and new policy claims (Assuming new policies from 2024 onwards)
SELECT * FROM claims WHERE claim_date < '2024-01-01'
UNION ALL
SELECT * FROM claims WHERE claim_date >= '2024-01-01';

-- 4. Correlated subquery to get highest claim per client
SELECT
    client_id,
    (SELECT MAX(claim_amount) FROM claims WHERE client_id = c.client_id) AS highest_claim
FROM clients c;

-- 5. JOIN + GROUP BY to find average claims per agent
SELECT
    a.name AS agent_name,
    AVG(cl.claim_amount) AS avg_claim_amount,
    COUNT(cl.claim_id) AS total_claims
FROM agents a
LEFT JOIN claims cl ON a.agent_id = cl.agent_id
GROUP BY a.agent_id, a.name;

-- 6. Date filtering for claims filed this quarter
SELECT * FROM claims
WHERE QUARTER(claim_date) = QUARTER(CURDATE()) AND YEAR(claim_date) = YEAR(CURDATE());
