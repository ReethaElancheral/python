-- 10. Versioned Document Tracker 
-- Requirements: 
--  Documents are versioned (v1, v2, ...). 
--  Use ROW_NUMBER() to list versions per document. 
--  Use LAG() to compare changes between versions. 
--  Use WITH RECURSIVE to trace dependencies between documents. 
--  CTEs for filtering current, outdated, or broken versions.

-- Create Database
CREATE DATABASE IF NOT EXISTS DocumentTrackerDB;
USE DocumentTrackerDB;

-- Tables
CREATE TABLE documents (
    document_id INT PRIMARY KEY,
    title VARCHAR(100)
);

CREATE TABLE document_versions (
    version_id INT PRIMARY KEY AUTO_INCREMENT,
    document_id INT,
    version_number INT,
    content TEXT,
    created_date DATE,
    previous_version_id INT NULL,
    FOREIGN KEY (document_id) REFERENCES documents(document_id),
    FOREIGN KEY (previous_version_id) REFERENCES document_versions(version_id)
);

-- Sample Data
INSERT INTO documents VALUES
(1,'Employee Handbook'),
(2,'Project Guidelines');

INSERT INTO document_versions (document_id, version_number, content, created_date, previous_version_id) VALUES
(1,1,'Initial Handbook','2025-01-01',NULL),
(1,2,'Updated Policies','2025-02-01',1),
(1,3,'Final Policies','2025-03-01',2),
(2,1,'Guidelines v1','2025-01-10',NULL),
(2,2,'Guidelines v2','2025-02-10',4);

-- ROW_NUMBER() to list versions per document
WITH version_list AS (
    SELECT document_id, version_id, version_number, content, created_date,
           ROW_NUMBER() OVER (PARTITION BY document_id ORDER BY version_number) AS version_order
    FROM document_versions
)
SELECT * FROM version_list
ORDER BY document_id, version_order;

-- LAG() to compare content with previous version
WITH version_diff AS (
    SELECT document_id, version_id, version_number, content, created_date,
           LAG(content) OVER (PARTITION BY document_id ORDER BY version_number) AS prev_content
    FROM document_versions
)
SELECT * FROM version_diff
ORDER BY document_id, version_number;

-- Recursive CTE to trace dependencies (previous versions)
WITH RECURSIVE version_chain AS (
    SELECT version_id, document_id, version_number, content, previous_version_id
    FROM document_versions
    WHERE previous_version_id IS NULL
    UNION ALL
    SELECT dv.version_id, dv.document_id, dv.version_number, dv.content, dv.previous_version_id
    FROM document_versions dv
    INNER JOIN version_chain vc ON dv.previous_version_id = vc.version_id
)
SELECT * FROM version_chain
ORDER BY document_id, version_number;

-- CTE to filter current, outdated, or broken versions
WITH version_status AS (
    SELECT dv.document_id, dv.version_id, dv.version_number,
           CASE
               WHEN dv.version_id = (SELECT MAX(version_id) FROM document_versions WHERE document_id = dv.document_id)
               THEN 'Current'
               WHEN dv.previous_version_id IS NOT NULL AND dv.version_id < (SELECT MAX(version_id) FROM document_versions WHERE document_id = dv.document_id)
               THEN 'Outdated'
               ELSE 'Broken'
           END AS status
    FROM document_versions dv
)
SELECT * FROM version_status
ORDER BY document_id, version_number;
