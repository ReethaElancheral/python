--  5. Library Management System 
-- Requirements: 
--  View view_book_availability for members (no supplier or purchase price). 
--  Procedure issue_book(member_id, book_id) to handle book issuing. 
--  Function get_due_date(issue_date) returns return date. 
--  Trigger after_issue updates availability. 
--  Use views to protect cost and supplier details from members.

-- Create Database
CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

-- Table: books
CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150),
    author VARCHAR(100),
    genre VARCHAR(50),
    stock INT
);

-- Table: members
CREATE TABLE members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    membership_date DATE
);

-- Table: borrow_records
CREATE TABLE borrow_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    member_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- Sample Data
INSERT INTO books (title, author, genre, stock) VALUES
('The Alchemist', 'Paulo Coelho', 'Fiction', 4),
('Clean Code', 'Robert C. Martin', 'Programming', 2),
('Atomic Habits', 'James Clear', 'Self-help', 5),
('1984', 'George Orwell', 'Dystopian', 3);

INSERT INTO members (name, membership_date) VALUES
('Ravi Deshmukh', '2024-01-15'),
('Nisha Sharma', '2024-03-02'),
('Kiran Rao', '2024-06-10');

-- ✅ View: borrowed_books_summary
CREATE OR REPLACE VIEW borrowed_books_summary AS
SELECT
    m.name AS member_name,
    b.title AS book_title,
    br.borrow_date,
    br.return_date
FROM borrow_records br
JOIN books b ON br.book_id = b.book_id
JOIN members m ON br.member_id = m.member_id;

-- ✅ Function: overdue_fee(borrow_date, return_date)
DELIMITER //
CREATE FUNCTION overdue_fee(borrow DATE, return_d DATE)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE fee DECIMAL(10,2);
    DECLARE overdue_days INT;

    SET overdue_days = DATEDIFF(return_d, borrow) - 14;

    IF overdue_days > 0 THEN
        SET fee = overdue_days * 5.00;
    ELSE
        SET fee = 0.00;
    END IF;

    RETURN fee;
END;
//
DELIMITER ;

-- ✅ Procedure: borrow_book(member_id, book_id, borrow_date)
DELIMITER //
CREATE PROCEDURE borrow_book(
    IN mem_id INT,
    IN bk_id INT,
    IN b_date DATE
)
BEGIN
    DECLARE available_stock INT;

    SELECT stock INTO available_stock FROM books WHERE book_id = bk_id;

    IF available_stock <= 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Book not available';
    END IF;

    INSERT INTO borrow_records (book_id, member_id, borrow_date)
    VALUES (bk_id, mem_id, b_date);

    UPDATE books SET stock = stock - 1 WHERE book_id = bk_id;
END;
//
DELIMITER ;

-- ✅ Trigger: before_return_date_insert (ensure return_date >= borrow_date)
DELIMITER //
CREATE TRIGGER check_return_date
BEFORE INSERT ON borrow_records
FOR EACH ROW
BEGIN
    IF NEW.return_date IS NOT NULL AND NEW.return_date < NEW.borrow_date THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Return date cannot be earlier than borrow date';
    END IF;
END;
//
DELIMITER ;

-- ✅ Test Examples
-- CALL borrow_book(1, 2, '2025-08-01');
-- SELECT * FROM borrowed_books_summary;
-- SELECT overdue_fee('2025-07-01', '2025-08-01');  -- Should return late fee
