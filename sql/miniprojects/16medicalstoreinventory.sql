-- -----------------------------------------------
-- Project 16: Medical Store Inventory
-- Requirements:
-- • Create medical_store_db
-- • Tables: medicines, suppliers, stock, sales
-- • Track batch numbers, expiry, and stock levels
-- • SQL to:
--    - Find low stock items
--    - Sales by medicine and supplier
-- -----------------------------------------------

CREATE DATABASE IF NOT EXISTS medical_store_db;
USE medical_store_db;

-- Suppliers table
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    contact_info VARCHAR(255)
);

-- Medicines table
CREATE TABLE medicines (
    medicine_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    description TEXT
);

-- Stock table
CREATE TABLE stock (
    stock_id INT PRIMARY KEY AUTO_INCREMENT,
    medicine_id INT,
    supplier_id INT,
    batch_number VARCHAR(50) NOT NULL,
    expiry_date DATE NOT NULL,
    quantity INT NOT NULL,
    FOREIGN KEY (medicine_id) REFERENCES medicines(medicine_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Sales table
CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    medicine_id INT,
    sale_date DATE,
    quantity_sold INT,
    supplier_id INT,
    FOREIGN KEY (medicine_id) REFERENCES medicines(medicine_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

-- Insert suppliers
INSERT INTO suppliers (name, contact_info) VALUES
('HealthSupplies Ltd.', 'contact@healthsupplies.com'),
('MediCare Inc.', 'info@medicare.com'),
('PharmaPlus', 'support@pharmaplus.com');

-- Insert medicines
INSERT INTO medicines (name, description) VALUES
('Paracetamol', 'Pain reliever and fever reducer'),
('Ibuprofen', 'Nonsteroidal anti-inflammatory drug'),
('Amoxicillin', 'Antibiotic for bacterial infections'),
('Cetirizine', 'Antihistamine for allergies'),
('Omeprazole', 'Reduces stomach acid');

-- Insert stock
INSERT INTO stock (medicine_id, supplier_id, batch_number, expiry_date, quantity) VALUES
(1, 1, 'B001', '2026-01-31', 150),
(2, 2, 'B002', '2025-09-30', 80),
(3, 3, 'B003', '2025-12-31', 50),
(4, 1, 'B004', '2025-08-15', 20),
(5, 2, 'B005', '2026-03-01', 100);

-- Insert sales
INSERT INTO sales (medicine_id, sale_date, quantity_sold, supplier_id) VALUES
(1, '2025-07-01', 20, 1),
(2, '2025-07-02', 15, 2),
(3, '2025-07-03', 10, 3),
(1, '2025-07-04', 30, 1),
(5, '2025-07-05', 25, 2),
(4, '2025-07-06', 5, 1);

-- -----------------------------------------------
-- Queries
-- -----------------------------------------------

-- 1. Find low stock items (e.g., quantity < 50)
SELECT 
    m.name AS medicine_name,
    s.batch_number,
    s.expiry_date,
    s.quantity,
    sup.name AS supplier_name
FROM stock s
JOIN medicines m ON s.medicine_id = m.medicine_id
JOIN suppliers sup ON s.supplier_id = sup.supplier_id
WHERE s.quantity < 50
ORDER BY s.quantity ASC;

-- 2. Sales by medicine and supplier
SELECT 
    m.name AS medicine_name,
    sup.name AS supplier_name,
    SUM(s.quantity_sold) AS total_sold
FROM sales s
JOIN medicines m ON s.medicine_id = m.medicine_id
JOIN suppliers sup ON s.supplier_id = sup.supplier_id
GROUP BY s.medicine_id, s.supplier_id
ORDER BY total_sold DESC;
