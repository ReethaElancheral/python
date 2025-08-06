--  10. Banking System 
-- Requirements: 
--  View view_account_summary hides internal fraud flagging and full account 
-- details. 
--  Procedure transfer_funds(from_ac, to_ac, amount) with balance checks. 
--  Function get_transaction_count(account_id) for reports. 
--  Trigger before_transfer to prevent overdraft. 
--  Tellers access account info only via secure view.

-- Create Database
CREATE DATABASE IF NOT EXISTS BankingDB;
USE BankingDB;

-- Table: accounts
CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    account_holder VARCHAR(100),
    balance DECIMAL(10,2),
    fraud_flag BOOLEAN DEFAULT FALSE,
    account_type VARCHAR(50),
    opened_on DATE
);

-- Table: transactions
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    from_account INT,
    to_account INT,
    amount DECIMAL(10,2),
    trans_date DATE,
    FOREIGN KEY (from_account) REFERENCES accounts(account_id),
    FOREIGN KEY (to_account) REFERENCES accounts(account_id)
);

-- ✅ View: view_account_summary (hides fraud_flag & full details)
CREATE OR REPLACE VIEW view_account_summary AS
SELECT 
    account_id,
    account_holder,
    balance,
    account_type
FROM accounts;

-- ✅ Function: get_transaction_count(account_id)
DELIMITER //
CREATE FUNCTION get_transaction_count(ac_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total INT;
    SELECT COUNT(*) INTO total
    FROM transactions
    WHERE from_account = ac_id OR to_account = ac_id;
    RETURN total;
END;
//
DELIMITER ;

-- ✅ Procedure: transfer_funds(from_ac, to_ac, amount)
DELIMITER //
CREATE PROCEDURE transfer_funds(
    IN from_ac INT,
    IN to_ac INT,
    IN amt DECIMAL(10,2),
    IN trans_date DATE
)
BEGIN
    DECLARE from_balance DECIMAL(10,2);

    SELECT balance INTO from_balance
    FROM accounts
    WHERE account_id = from_ac;

    IF from_balance < amt THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient balance for transfer.';
    ELSE
        UPDATE accounts SET balance = balance - amt WHERE account_id = from_ac;
        UPDATE accounts SET balance = balance + amt WHERE account_id = to_ac;

        INSERT INTO transactions (from_account, to_account, amount, trans_date)
        VALUES (from_ac, to_ac, amt, trans_date);
    END IF;
END;
//
DELIMITER ;

-- ✅ Trigger: before_transfer to prevent overdraft
DELIMITER //
CREATE TRIGGER before_transfer
BEFORE INSERT ON transactions
FOR EACH ROW
BEGIN
    DECLARE available DECIMAL(10,2);
    SELECT balance INTO available FROM accounts WHERE account_id = NEW.from_account;

    IF available < NEW.amount THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Overdraft detected. Transfer blocked.';
    END IF;
END;
//
DELIMITER ;

-- ✅ Tellers: Restricted view for secure access
CREATE OR REPLACE VIEW view_teller_access AS
SELECT 
    account_id,
    account_holder,
    balance
FROM accounts
WHERE fraud_flag = FALSE;

-- ✅ Sample Data
INSERT INTO accounts (account_holder, balance, fraud_flag, account_type, opened_on)
VALUES 
('Nisha Reetha', 15000.00, FALSE, 'Savings', '2024-05-01'),
('Ravi Kumar', 8000.00, FALSE, 'Current', '2024-06-15'),
('Sneha Patel', 2000.00, TRUE, 'Savings', '2024-07-10');

-- ✅ Sample Usage
-- CALL transfer_funds(1, 2, 500.00, '2025-08-07');
-- SELECT get_transaction_count(1);
-- SELECT * FROM view_account_summary;
-- SELECT * FROM view_teller_access;
