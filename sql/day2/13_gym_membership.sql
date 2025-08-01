-- Project 13: Gym Membership Database
CREATE TABLE members (
    member_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    plan_type VARCHAR(50),
    start_date DATE,
    status VARCHAR(20)
);

INSERT INTO members (member_id, name, age, plan_type, start_date, status) VALUES
(1, 'Suresh Kumar', 25, 'Premium', '2024-01-15', 'Active'),
(2, 'Sunita Sharma', 32, 'Basic', '2023-07-20', 'Inactive'),
(3, 'Rohit Singh', 29, 'Standard', '2024-03-05', NULL),
(4, 'Sneha Patel', 22, 'Premium', '2024-02-10', 'Active'),
(5, 'Sanjay Joshi', 40, 'Basic', '2023-12-01', 'Active');

SELECT name, age, plan_type FROM members WHERE status = 'active' AND age BETWEEN 20 AND 40;
SELECT DISTINCT plan_type FROM members;
SELECT * FROM members WHERE name LIKE 'S%';
SELECT * FROM members WHERE status IS NULL;
SELECT * FROM members ORDER BY age ASC, name ASC;