-- Create database
CREATE DATABASE IF NOT EXISTS RealEstateDB;
USE RealEstateDB;

-- Agents table
CREATE TABLE agents (
    agent_id INT PRIMARY KEY,
    agent_name VARCHAR(100),
    area VARCHAR(100)
);

-- Clients table
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(100)
);

-- Properties table
CREATE TABLE properties (
    property_id INT PRIMARY KEY,
    agent_id INT,
    location VARCHAR(100),
    price DECIMAL(12,2),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

-- Inquiries table
CREATE TABLE inquiries (
    inquiry_id INT PRIMARY KEY,
    client_id INT,
    property_id INT,
    agent_id INT,
    inquiry_date DATE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

-- Sample Data
INSERT INTO agents VALUES 
(1, 'Rahul Kapoor', 'Mumbai'),
(2, 'Sneha Mehta', 'Delhi'),
(3, 'Arjun Verma', 'Mumbai');

INSERT INTO clients VALUES 
(101, 'Karan Sharma'),
(102, 'Priya Nair'),
(103, 'Amit Rao'),
(104, 'Neha Desai');

INSERT INTO properties VALUES 
(201, 1, 'Bandra', 9500000),
(202, 2, 'South Delhi', 12500000),
(203, 1, 'Andheri', 8700000),
(204, 3, 'Bandra', 7800000),
(205, 3, 'Worli', 10200000),
(206, 2, 'Noida', 6900000);

INSERT INTO inquiries VALUES 
(301, 101, 201, 1, '2025-07-01'),
(302, 102, 202, 2, '2025-07-02'),
(303, 103, 203, 1, '2025-07-03'),
(304, 104, 204, 3, '2025-07-04'),
(305, 101, 205, 3, '2025-07-05'),
(306, 102, 206, 2, '2025-07-06'),
(307, 103, 201, 1, '2025-07-07'),
(308, 101, 203, 1, '2025-07-08'),
(309, 104, 204, 3, '2025-07-08'),
(310, 103, 201, 1, '2025-07-09'),
(311, 102, 205, 3, '2025-07-10'),
(312, 104, 206, 2, '2025-07-11');

--  Total loans issued per officer 
--  Clients with repayment > ₹1,00,000 
--  Officers approving more than 10 loans 
--  INNER JOIN: clients ↔ loans ↔ officers 
--  FULL OUTER JOIN: loans ↔ repayments 
--  SELF JOIN: clients from same city 

SELECT a.agent_name, COUNT(p.property_id) AS property_count
FROM agents a
JOIN properties p ON a.agent_id = p.agent_id
GROUP BY a.agent_id;

SELECT location, ROUND(AVG(price), 2) AS avg_price
FROM properties
GROUP BY location;

SELECT a.agent_name, COUNT(i.inquiry_id) AS inquiry_count
FROM agents a
JOIN inquiries i ON a.agent_id = i.agent_id
GROUP BY a.agent_id
HAVING inquiry_count > 20;

SELECT i.inquiry_id, a.agent_name, p.location, c.client_name
FROM inquiries i
JOIN agents a ON i.agent_id = a.agent_id
JOIN properties p ON i.property_id = p.property_id
JOIN clients c ON i.client_id = c.client_id;

SELECT p.property_id, p.location, i.inquiry_id
FROM properties p
LEFT JOIN inquiries i ON p.property_id = i.property_id;

SELECT a1.agent_name AS Agent1, a2.agent_name AS Agent2, a1.area
FROM agents a1
JOIN agents a2 
  ON a1.area = a2.area AND a1.agent_id < a2.agent_id;
