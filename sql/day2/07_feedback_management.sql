-- Project 7: Customer Feedback Management
CREATE TABLE feedback (
    feedback_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    rating INT,
    comment TEXT,
    product VARCHAR(100),
    submitted_date DATE
);

INSERT INTO feedback (feedback_id, customer_name, rating, comment, product, submitted_date) VALUES
(1, 'Alice', 5, 'Excellent smartphone!', 'Smartphone', '2025-07-01'),
(2, 'Bob', 3, 'Phone is slow sometimes', 'Smartphone', '2025-07-10'),
(3, 'Charlie', 4, NULL, 'Laptop', '2025-07-15'),
(4, 'Diana', 2, 'Battery drains fast', 'Smartphone', '2025-07-20'),
(5, 'Eva', 5, 'Great value', 'Smartphone', '2025-07-22');

SELECT customer_name, rating, comment FROM feedback WHERE rating >= 4 AND product = 'Smartphone';
SELECT * FROM feedback WHERE comment LIKE '%slow%';
SELECT * FROM feedback WHERE submitted_date BETWEEN CURDATE() - INTERVAL 30 DAY AND CURDATE();
SELECT * FROM feedback WHERE comment IS NULL;
SELECT DISTINCT product FROM feedback;
SELECT * FROM feedback ORDER BY rating DESC, submitted_date DESC;