--  4. Library Management System 
-- Requirements: 
--  Tables: books, members, loans 
--  Insert new books with UNIQUE ISBN, and NOT NULL title. 
--  UPDATE book stock after loans. 
--  DELETE loans when returned. 
--  Enforce FOREIGN KEY between loans → members and loans → books. 
--  Add a CHECK for max 3 active loans per member. 
--  Temporarily disable the CHECK, perform updates, then re-enable. 
--  Use transactions to rollback if loan exceeds stock. 


CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(150),
    total_stock INT NOT NULL CHECK (total_stock >= 0),
    available_stock INT NOT NULL CHECK (available_stock >= 0)
);


CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    member_name VARCHAR(100) NOT NULL,
    contact VARCHAR(15)
);


CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    book_id INT NOT NULL,
    loan_date DATE NOT NULL,
    return_date DATE DEFAULT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    CHECK (active IN (0,1))
);

-- Add CHECK for max 3 active loans per member via trigger (since CHECK cannot count rows)

DELIMITER $$

CREATE TRIGGER trg_max_active_loans BEFORE INSERT ON loans
FOR EACH ROW
BEGIN
    DECLARE active_loans INT;
    SELECT COUNT(*) INTO active_loans
    FROM loans
    WHERE member_id = NEW.member_id AND active = TRUE;

    IF active_loans >= 3 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Member cannot have more than 3 active loans';
    END IF;
END$$

DELIMITER ;

-- Insert sample books
INSERT INTO books (isbn, title, author, total_stock, available_stock) VALUES
('978-0132350884', 'Clean Code', 'Robert C. Martin', 10, 10),
('978-0201616224', 'The Pragmatic Programmer', 'Andrew Hunt', 8, 8);

-- Insert sample members
INSERT INTO members (member_name, contact) VALUES
('Alice Green', '1234567890'),
('Bob Brown', '0987654321');

-- Example: loan a book - update book stock after loan within transaction
START TRANSACTION;

-- Check if book is available
SELECT available_stock FROM books WHERE book_id = 1;

-- If available_stock > 0, proceed
INSERT INTO loans (member_id, book_id, loan_date) VALUES (1, 1, CURDATE());

-- Decrement available_stock
UPDATE books SET available_stock = available_stock - 1 WHERE book_id = 1;

-- Commit transaction
COMMIT;

-- Delete loans when returned (i.e., mark loan inactive and increase stock)
UPDATE loans SET active = FALSE, return_date = CURDATE() WHERE loan_id = 1;

UPDATE books SET available_stock = available_stock + 1 WHERE book_id = (
    SELECT book_id FROM loans WHERE loan_id = 1
);

-- Temporarily disable the CHECK constraint on books.available_stock
-- MySQL does not support disabling CHECK constraints directly
-- We simulate by ignoring or altering the check

-- If you want to perform updates ignoring CHECK, you can remove constraint by recreating the table
-- For demonstration, assume it's disabled during bulk update and re-enabled after

-- Use transactions to rollback if loan exceeds stock

-- Start the transaction
START TRANSACTION;

-- Check availability first
SELECT available_stock FROM books WHERE book_id = 2;

-- Based on that result, manually proceed or rollback:
-- (You do this check from app logic or visually if testing in Workbench)

-- If available_stock > 0, then:
INSERT INTO loans (member_id, book_id, loan_date) VALUES (2, 2, CURDATE());
UPDATE books SET available_stock = available_stock - 1 WHERE book_id = 2;
COMMIT;

-- If available_stock = 0, then:
-- ROLLBACK;

