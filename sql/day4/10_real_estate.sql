-- Project 10: Real Estate Property Listings Analyzer

CREATE DATABASE IF NOT EXISTS real_estate_db;
USE real_estate_db;

CREATE TABLE agents (
    agent_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

CREATE TABLE properties (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    agent_id INT,
    type ENUM('Residential', 'Commercial'),
    listing_date DATE,
    sale_date DATE,
    price DECIMAL(15,2),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    client_id INT,
    sale_price DECIMAL(15,2),
    sale_date DATE,
    FOREIGN KEY (property_id) REFERENCES properties(property_id)
);

CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

-- Insert sample data

INSERT INTO agents (name, city) VALUES
('Alice Johnson', 'New York'),
('Bob Smith', 'Los Angeles'),
('Clara Lee', 'Chicago');

INSERT INTO clients (name, city) VALUES
('David Green', 'New York'),
('Eva Brown', 'Los Angeles'),
('Frank White', 'Chicago');

INSERT INTO properties (agent_id, type, listing_date, sale_date, price) VALUES
(1, 'Residential', '2025-01-10', '2025-03-15', 500000),
(1, 'Commercial', '2025-02-01', NULL, 1200000),
(2, 'Residential', '2025-01-20', '2025-04-10', 450000),
(3, 'Commercial', '2025-02-15', '2025-05-05', 800000);

INSERT INTO sales (property_id, client_id, sale_price, sale_date) VALUES
(1, 1, 520000, '2025-03-15'),
(3, 2, 460000, '2025-04-10'),
(4, 3, 820000, '2025-05-05');

-- Queries

-- 1. Subquery to find agents whose total sales are above company average
SELECT
    a.name AS agent_name,
    SUM(s.sale_price) AS total_sales
FROM agents a
JOIN properties p ON a.agent_id = p.agent_id
JOIN sales s ON p.property_id = s.property_id
GROUP BY a.agent_id, a.name
HAVING total_sales > (
    SELECT AVG(agent_sales) FROM (
        SELECT SUM(sale_price) AS agent_sales
        FROM agents
        JOIN properties ON agents.agent_id = properties.agent_id
        JOIN sales ON properties.property_id = sales.property_id
        GROUP BY agents.agent_id
    ) AS sub
);

-- 2. CASE to categorize property types
SELECT
    property_id,
    type,
    CASE
        WHEN type = 'Residential' THEN 'Residential Property'
        WHEN type = 'Commercial' THEN 'Commercial Property'
        ELSE 'Other'
    END AS category
FROM properties;

-- 3. UNION ALL for properties sold vs still listed
SELECT
    property_id,
    'Sold' AS status
FROM sales
UNION ALL
SELECT
    property_id,
    'Listed' AS status
FROM properties
WHERE sale_date IS NULL;

-- 4. Correlated subquery to find highest sale per agent
SELECT
    a.name AS agent_name,
    (SELECT MAX(s.sale_price)
     FROM properties p
     JOIN sales s ON p.property_id = s.property_id
     WHERE p.agent_id = a.agent_id) AS highest_sale
FROM agents a;

-- 5. JOIN + GROUP BY to show agent sales by city
SELECT
    a.city,
    a.name AS agent_name,
    COUNT(s.sale_id) AS total_sales,
    SUM(s.sale_price) AS total_revenue
FROM agents a
LEFT JOIN properties p ON a.agent_id = p.agent_id
LEFT JOIN sales s ON p.property_id = s.property_id
GROUP BY a.city, a.agent_id, a.name;

-- 6. Use DATEDIFF to calculate time between listing and sale
SELECT
    property_id,
    listing_date,
    sale_date,
    DATEDIFF(sale_date, listing_date) AS days_to_sell
FROM properties
WHERE sale_date IS NOT NULL;
