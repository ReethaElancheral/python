CREATE DATABASE IF NOT EXISTS saas_db;
USE saas_db;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    plan_id INT,
    last_active DATE
);

CREATE TABLE plans (
    plan_id INT AUTO_INCREMENT PRIMARY KEY,
    plan_name VARCHAR(50),
    monthly_fee DECIMAL(10,2)
);

CREATE TABLE subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    plan_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id)
);

CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    subscription_id INT,
    payment_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(subscription_id)
);

-- Insert sample data

INSERT INTO plans (plan_name, monthly_fee) VALUES
('Free', 0), ('Basic', 50), ('Premium', 100);

INSERT INTO users (name, plan_id, last_active) VALUES
('Alice', 2, '2025-07-25'), ('Bob', 3, '2025-07-28'), ('Charlie', 1, '2025-06-15');

INSERT INTO subscriptions (user_id, plan_id, start_date, end_date) VALUES
(1, 2, '2025-01-01', '2025-12-31'),
(2, 3, '2025-03-01', '2025-08-31'),
(3, 1, '2025-01-01', '2025-12-31');

INSERT INTO payments (subscription_id, payment_date, amount) VALUES
(1, '2025-07-01', 50),
(2, '2025-07-01', 100),
(3, '2025-07-01', 0);

-- Queries

-- 1. Subquery in FROM to calculate plan-wise average revenue
SELECT
    plan_id,
    AVG(plan_revenue) AS avg_revenue
FROM (
    SELECT
        p.plan_id,
        SUM(payments.amount) AS plan_revenue
    FROM payments
    JOIN subscriptions s ON payments.subscription_id = s.subscription_id
    JOIN plans p ON s.plan_id = p.plan_id
    GROUP BY p.plan_id
) AS sub
GROUP BY plan_id;

-- 2. CASE to show user activity
SELECT
    name,
    CASE
        WHEN last_active >= CURDATE() - INTERVAL 30 DAY THEN 'Active'
        WHEN last_active BETWEEN CURDATE() - INTERVAL 90 DAY AND CURDATE() - INTERVAL 31 DAY THEN 'Inactive'
        ELSE 'Trial'
    END AS activity_status
FROM users;

-- 3. UNION to merge paid and free-tier users
SELECT user_id, name, 'Paid' AS user_type FROM users WHERE plan_id != 1
UNION
SELECT user_id, name, 'Free' AS user_type FROM users WHERE plan_id = 1;

-- 4. JOIN + GROUP BY for monthly revenue trends
SELECT
    YEAR(payment_date) AS year,
    MONTH(payment_date) AS month,
    SUM(amount) AS total_revenue
FROM payments
GROUP BY year, month
ORDER BY year, month;

-- 5. Correlated subquery to find longest-subscribed users
SELECT
    u.user_id,
    u.name,
    (SELECT MAX(DATEDIFF(end_date, start_date)) FROM subscriptions s WHERE s.user_id = u.user_id) AS longest_subscription_days
FROM users u;

-- 6. Date filtering for renewal reminders (subscriptions ending within next 7 days)
SELECT * FROM subscriptions WHERE end_date BETWEEN CURDATE() AND CURDATE() + INTERVAL 7 DAY;
