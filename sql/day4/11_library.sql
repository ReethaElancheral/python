CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(100)
);

CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    loan_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id)
);

CREATE TABLE returns (
    return_id INT AUTO_INCREMENT PRIMARY KEY,
    loan_id INT,
    return_date DATE,
    FOREIGN KEY (loan_id) REFERENCES loans(loan_id)
);

-- Insert sample data
INSERT INTO books (title, genre) VALUES
('The Great Gatsby', 'Fiction'),
('A Brief History of Time', 'Non-Fiction'),
('1984', 'Fiction'),
('Sapiens', 'Non-Fiction'),
('To Kill a Mockingbird', 'Fiction');

INSERT INTO members (name) VALUES
('John Doe'), ('Jane Smith'), ('Alice Brown'), ('Bob White');

INSERT INTO loans (book_id, member_id, loan_date) VALUES
(1,1,'2025-04-01'), (2,1,'2025-04-10'), (3,2,'2025-04-15'),
(4,3,'2025-04-20'), (5,4,'2025-03-20'), (1,4,'2025-05-01'),
(2,3,'2025-04-28'), (3,1,'2025-05-05');

INSERT INTO returns (loan_id, return_date) VALUES
(1,'2025-04-15'), (2,'2025-04-20'), (3,'2025-04-25');

-- Queries

-- 1. Books borrowed more than average
SELECT
    b.title,
    COUNT(l.loan_id) AS borrow_count
FROM books b
JOIN loans l ON b.book_id = l.book_id
GROUP BY b.book_id, b.title
HAVING borrow_count > (
    SELECT AVG(borrow_count) FROM (
        SELECT COUNT(loan_id) AS borrow_count FROM loans GROUP BY book_id
    ) AS sub
);

-- 2. CASE to classify members based on total borrowings
SELECT
    m.name,
    COUNT(l.loan_id) AS total_borrowings,
    CASE
        WHEN COUNT(l.loan_id) > 5 THEN 'Frequent Borrower'
        WHEN COUNT(l.loan_id) BETWEEN 2 AND 5 THEN 'Regular Borrower'
        ELSE 'Infrequent Borrower'
    END AS borrower_type
FROM members m
LEFT JOIN loans l ON m.member_id = l.member_id
GROUP BY m.member_id, m.name;

-- 3. JOIN + GROUP BY for most borrowed genres
SELECT
    b.genre,
    COUNT(l.loan_id) AS total_borrowings
FROM books b
JOIN loans l ON b.book_id = l.book_id
GROUP BY b.genre
ORDER BY total_borrowings DESC;

-- 4. UNION to show active and inactive borrowers
SELECT member_id, 'Active' AS status FROM loans GROUP BY member_id
UNION
SELECT member_id, 'Inactive' AS status FROM members WHERE member_id NOT IN (SELECT DISTINCT member_id FROM loans);

-- 5. INTERSECT for members who borrowed both Fiction and Non-Fiction
SELECT member_id FROM loans l JOIN books b ON l.book_id = b.book_id WHERE b.genre = 'Fiction'
INTERSECT
SELECT member_id FROM loans l JOIN books b ON l.book_id = b.book_id WHERE b.genre = 'Non-Fiction';

-- 6. Date-based filtering for loans in the past 90 days
SELECT * FROM loans WHERE loan_date >= CURDATE() - INTERVAL 90 DAY;
