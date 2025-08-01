
CREATE DATABASE IF NOT EXISTS ITSupportDB;
USE ITSupportDB;

-- Technicians table
CREATE TABLE technicians (
    tech_id INT PRIMARY KEY,
    tech_name VARCHAR(100)
);

-- Clients table
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(100),
    company_name VARCHAR(100)
);

-- Tickets table
CREATE TABLE tickets (
    ticket_id INT PRIMARY KEY,
    client_id INT,
    tech_id INT,
    issue_type VARCHAR(100),
    opened_at DATETIME,
    resolved_at DATETIME,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (tech_id) REFERENCES technicians(tech_id)
);

-- Sample Data
INSERT INTO technicians VALUES 
(1, 'Ankit Singh'),
(2, 'Meera Joshi'),
(3, 'Ravi Iyer');

INSERT INTO clients VALUES 
(101, 'Deepak Rao', 'SoftCorp'),
(102, 'Alisha Mehta', 'InfoTech'),
(103, 'Manoj Kulkarni', 'NetVision');

INSERT INTO tickets VALUES 
(201, 101, 1, 'Login Issue', '2025-07-01 09:00:00', '2025-07-01 12:00:00'),
(202, 102, 2, 'Network Down', '2025-07-01 10:30:00', '2025-07-01 13:00:00'),
(203, 101, 1, 'Password Reset', '2025-07-02 11:00:00', '2025-07-02 11:15:00'),
(204, 103, 3, 'Software Bug', '2025-07-02 14:00:00', '2025-07-02 18:00:00'),
(205, 102, 1, 'Login Issue', '2025-07-03 08:00:00', '2025-07-03 10:00:00'),
(206, 103, 2, 'Password Reset', '2025-07-03 09:00:00', '2025-07-03 09:30:00'),
(207, 101, 1, 'Login Issue', '2025-07-04 07:45:00', '2025-07-04 08:15:00'),
(208, 101, 1, 'Software Bug', '2025-07-04 10:00:00', '2025-07-04 11:30:00'),
(209, 101, 1, 'Network Down', '2025-07-05 09:00:00', '2025-07-05 11:00:00'),
(210, 102, 1, 'Login Issue', '2025-07-05 12:00:00', '2025-07-05 14:00:00'),
(211, 103, 1, 'Software Bug', '2025-07-06 15:00:00', '2025-07-06 17:30:00');

-- 1. Count of tickets per technician
SELECT t.tech_name, COUNT(k.ticket_id) AS total_tickets
FROM tickets k
JOIN technicians t ON k.tech_id = t.tech_id
GROUP BY t.tech_id;

-- 2. Average resolution time per technician (in minutes)
SELECT t.tech_name, 
       ROUND(AVG(TIMESTAMPDIFF(MINUTE, k.opened_at, k.resolved_at)), 2) AS avg_resolution_mins
FROM tickets k
JOIN technicians t ON k.tech_id = t.tech_id
GROUP BY t.tech_id;

-- 3. Technicians handling more than 10 tickets
SELECT t.tech_name, COUNT(k.ticket_id) AS ticket_count
FROM tickets k
JOIN technicians t ON k.tech_id = t.tech_id
GROUP BY t.tech_id
HAVING ticket_count > 10;

-- 4. INNER JOIN: tickets ↔ technicians
SELECT k.ticket_id, t.tech_name, k.issue_type
FROM tickets k
INNER JOIN technicians t ON k.tech_id = t.tech_id;

-- 5. LEFT JOIN: clients ↔ tickets (all clients, even those without tickets)
SELECT c.client_name, c.company_name, k.ticket_id, k.issue_type
FROM clients c
LEFT JOIN tickets k ON c.client_id = k.client_id;

-- 6. SELF JOIN: tickets with same issue types (different ticket_ids)
SELECT t1.ticket_id AS Ticket1, t2.ticket_id AS Ticket2, t1.issue_type
FROM tickets t1
JOIN tickets t2 
  ON t1.issue_type = t2.issue_type AND t1.ticket_id < t2.ticket_id;
