-- 20. Public Library System 
-- Requirements: 
--  Tables: members, books, checkouts, fines 
--  Count books issued per member 
--  Members with fines over ₹500 
--  Books with > 5 checkouts 
--  INNER JOIN: checkouts ↔ members ↔ books 
--  LEFT JOIN: books ↔ checkouts 
--  SELF JOIN: members who borrowed the same books

-- Create database
CREATE DATABASE IF NOT EXISTS LibraryDB;
USE LibraryDB;

-- Create tables

CREATE TABLE members (
    member_id INT PRIMARY KEY,
    member_name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(150),
    author VARCHAR(100),
    genre VARCHAR(50)
);

CREATE TABLE checkouts (
    checkout_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    checkout_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

CREATE TABLE fines (
    fine_id INT PRIMARY KEY,
    member_id INT,
    amount DECIMAL(10,2),
    fine_date DATE,
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

-- Insert sample data into members
INSERT INTO members VALUES
(1, 'Anita Sharma', 'anita.sharma@example.com'),
(2, 'Rohit Singh', 'rohit.singh@example.com'),
(3, 'Priya Nair', 'priya.nair@example.com'),
(4, 'Vikram Patel', 'vikram.patel@example.com'),
(5, 'Sunita Desai', 'sunita.desai@example.com');

-- Insert sample data into books
INSERT INTO books VALUES
(101, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction'),
(102, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction'),
(103, '1984', 'George Orwell', 'Dystopian'),
(104, 'Pride and Prejudice', 'Jane Austen', 'Romance'),
(105, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy');

-- Insert sample data into checkouts
INSERT INTO checkouts VALUES
(201, 1, 101, '2025-07-01', '2025-07-10'),
(202, 1, 102, '2025-07-11', '2025-07-20'),
(203, 2, 103, '2025-07-05', NULL),
(204, 3, 101, '2025-07-07', '2025-07-15'),
(205, 4, 104, '2025-07-08', '2025-07-18'),
(206, 5, 105, '2025-07-10', '2025-07-25'),
(207, 2, 101, '2025-07-15', NULL),
(208, 3, 102, '2025-07-18', NULL),
(209, 4, 103, '2025-07-20', NULL),
(210, 1, 103, '2025-07-22', NULL),
(211, 5, 101, '2025-07-25', NULL),
(212, 3, 105, '2025-07-27', NULL),
(213, 4, 105, '2025-07-28', NULL),
(214, 2, 104, '2025-07-29', NULL),
(215, 1, 105, '2025-07-30', NULL);

-- Insert sample data into fines
INSERT INTO fines VALUES
(301, 1, 600.00, '2025-07-15'),
(302, 2, 450.00, '2025-07-18'),
(303, 3, 700.00, '2025-07-20'),
(304, 4, 300.00, '2025-07-22'),
(305, 5, 1000.00, '2025-07-25');

SELECT m.member_name, COUNT(c.checkout_id) AS books_issued
FROM members m
JOIN checkouts c ON m.member_id = c.member_id
GROUP BY m.member_id;

SELECT m.member_name, SUM(f.amount) AS total_fines
FROM members m
JOIN fines f ON m.member_id = f.member_id
GROUP BY m.member_id
HAVING total_fines > 500;

SELECT b.title, COUNT(c.checkout_id) AS checkout_count
FROM books b
JOIN checkouts c ON b.book_id = c.book_id
GROUP BY b.book_id
HAVING checkout_count > 5;

SELECT c.checkout_id, m.member_name, b.title, c.checkout_date, c.return_date
FROM checkouts c
JOIN members m ON c.member_id = m.member_id
JOIN books b ON c.book_id = b.book_id;

SELECT b.book_id, b.title, c.checkout_id
FROM books b
LEFT JOIN checkouts c ON b.book_id = c.book_id;

SELECT DISTINCT m1.member_name AS Member1, m2.member_name AS Member2, b.title
FROM checkouts c1
JOIN checkouts c2 ON c1.book_id = c2.book_id AND c1.member_id <> c2.member_id
JOIN members m1 ON c1.member_id = m1.member_id
JOIN members m2 ON c2.member_id = m2.member_id
JOIN books b ON c1.book_id = b.book_id
ORDER BY b.title, Member1, Member2;
