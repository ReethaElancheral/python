
-- Project 20: Subscription Billing and Plan Management

CREATE DATABASE IF NOT EXISTS SubscriptionDB;
USE SubscriptionDB;

CREATE TABLE plans (
    plan_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    price DECIMAL(10,2),
    duration_months INT
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE subscriptions (
    sub_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    plan_id INT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id),
    CHECK (start_date < end_date)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY AUTO_INCREMENT,
    sub_id INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (sub_id) REFERENCES subscriptions(sub_id)
);

-- Insert & transaction
INSERT INTO users (name) VALUES ('Fatima Qureshi');
INSERT INTO plans (name, price, duration_months) VALUES ('Premium', 999.99, 12);

-- SAVEPOINT example
START TRANSACTION;
SAVEPOINT before_renewal;
INSERT INTO subscriptions (user_id, plan_id, start_date, end_date) VALUES (1, 1, '2025-08-01', '2026-08-01');
INSERT INTO payments (sub_id, amount) VALUES (1, 999.99,CURRENT_DATE);
COMMIT;
