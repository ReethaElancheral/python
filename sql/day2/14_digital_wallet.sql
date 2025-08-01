-- Project 14: Digital Wallet Transactions
CREATE TABLE transactions (
    txn_id INT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10,2),
    txn_type VARCHAR(50),
    txn_date DATE,
    status VARCHAR(20)
);

INSERT INTO transactions (txn_id, user_id, amount, txn_type, txn_date, status) VALUES
(1, 101, 500, 'Recharge', '2025-07-01', 'Completed'),
(2, 102, 1500, 'Withdrawal', '2025-07-03', NULL),
(3, 103, 250, 'Recharge', '2025-07-05', 'Completed'),
(4, 104, 1000, 'Payment', '2025-07-10', 'Pending'),
(5, 105, 750, 'Recharge', '2025-07-15', 'Completed');

SELECT user_id, amount, txn_type FROM transactions WHERE amount BETWEEN 100 AND 1000;
SELECT * FROM transactions WHERE txn_type LIKE '%recharge%';
SELECT * FROM transactions WHERE status IS NULL;
SELECT * FROM transactions ORDER BY txn_date DESC;