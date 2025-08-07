-- 6. Call Center Escalation Reporting 
-- Requirements: 
--  Escalation levels: Agent → Supervisor → Manager. 
--  Use recursive CTE to show escalation flow.
--  Use ROW_NUMBER() to order support interactions. 
--  Use RANK() to find most escalated agents. 
--  Compare issue resolution time with LAG(). 

-- Create Database
CREATE DATABASE IF NOT EXISTS CallCenterDB;
USE CallCenterDB;

-- Tables
CREATE TABLE agents (
    agent_id INT PRIMARY KEY,
    name VARCHAR(100),
    supervisor_id INT NULL
);

CREATE TABLE issues (
    issue_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    issue_date DATE
);

CREATE TABLE escalations (
    escalation_id INT PRIMARY KEY AUTO_INCREMENT,
    issue_id INT,
    agent_id INT,
    escalation_date DATE,
    resolved_date DATE,
    FOREIGN KEY (issue_id) REFERENCES issues(issue_id),
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
);

-- Sample Data
INSERT INTO agents VALUES
(1,'Alice',2),
(2,'Bob',3),
(3,'Charlie',NULL),
(4,'Diana',2);

INSERT INTO issues VALUES
(101,'John','2025-01-01'),
(102,'Mary','2025-01-02'),
(103,'Peter','2025-01-03');

INSERT INTO escalations (issue_id, agent_id, escalation_date, resolved_date) VALUES
(101,1,'2025-01-01','2025-01-02'),
(101,2,'2025-01-02','2025-01-03'),
(102,4,'2025-01-02','2025-01-04'),
(103,1,'2025-01-03','2025-01-05');

-- Recursive CTE: Escalation flow Agent -> Supervisor -> Manager
WITH RECURSIVE escalation_flow AS (
    SELECT agent_id, name, supervisor_id, 1 AS level
    FROM agents
    WHERE supervisor_id IS NOT NULL
    UNION ALL
    SELECT a.agent_id, a.name, a.supervisor_id, ef.level + 1
    FROM agents a
    INNER JOIN escalation_flow ef ON a.agent_id = ef.supervisor_id
)
SELECT * FROM escalation_flow
ORDER BY level, agent_id;

-- ROW_NUMBER() to order support interactions per agent
WITH interactions_ordered AS (
    SELECT e.escalation_id, e.agent_id, a.name AS agent_name, e.issue_id, e.escalation_date, e.resolved_date,
           ROW_NUMBER() OVER (PARTITION BY e.agent_id ORDER BY e.escalation_date) AS interaction_no
    FROM escalations e
    JOIN agents a ON e.agent_id = a.agent_id
)
SELECT * FROM interactions_ordered
ORDER BY agent_id, interaction_no;

-- RANK() to find most escalated agents
WITH agent_escalations AS (
    SELECT agent_id, COUNT(*) AS total_escalations
    FROM escalations
    GROUP BY agent_id
)
SELECT a.agent_id, ag.name AS agent_name, ae.total_escalations,
       RANK() OVER (ORDER BY ae.total_escalations DESC) AS rank_by_escalation
FROM agent_escalations ae
JOIN agents ag ON ae.agent_id = ag.agent_id;

-- Compare issue resolution time using LAG()
WITH resolution_time AS (
    SELECT e.agent_id, a.name AS agent_name, e.issue_id, e.escalation_date, e.resolved_date,
           DATEDIFF(e.resolved_date, e.escalation_date) AS days_to_resolve,
           LAG(DATEDIFF(e.resolved_date, e.escalation_date)) OVER (PARTITION BY e.agent_id ORDER BY e.escalation_date) AS prev_days_to_resolve
    FROM escalations e
    JOIN agents a ON e.agent_id = a.agent_id
)
SELECT agent_name, issue_id, days_to_resolve, prev_days_to_resolve
FROM resolution_time
ORDER BY agent_id, issue_id;
