CREATE DATABASE library_db;
USE library_db;


CREATE TABLE books (
  book_id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  total_copies INT DEFAULT 1,
  available_copies INT DEFAULT 1
);

CREATE TABLE members (
  member_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE borrowings (
  borrowing_id INT AUTO_INCREMENT PRIMARY KEY,
  member_id INT,
  book_id INT,
  borrow_date DATE,
  due_date DATE,
  return_date DATE DEFAULT NULL,
  FOREIGN KEY (member_id) REFERENCES members(member_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id)
);

INSERT INTO members (name, email) VALUES
('Alice Sharma', 'alice@example.com'),
('Bob Mehta', 'bob@example.com'),
('Carol Rao', 'carol@example.com'),
('Dev Sen', 'dev@example.com'),
('Eva Das', 'eva@example.com'),
('Farhan Khan', 'farhan@example.com'),
('Gita Iyer', 'gita@example.com'),
('Hari Patel', 'hari@example.com'),
('Indira Singh', 'indira@example.com'),
('Jay Malhotra', 'jay@example.com');

INSERT INTO books (title, author, total_copies, available_copies) VALUES
('The Alchemist', 'Paulo Coelho', 5, 3),
('1984', 'George Orwell', 4, 2),
('To Kill a Mockingbird', 'Harper Lee', 6, 4),
('The Book Thief', 'Markus Zusak', 3, 1),
('Atomic Habits', 'James Clear', 7, 6),
('The Great Gatsby', 'F. Scott Fitzgerald', 5, 4),
('Sapiens', 'Yuval Noah Harari', 4, 3),
('Educated', 'Tara Westover', 2, 1),
('Ikigai', 'Héctor García', 3, 2),
('Wings of Fire', 'A.P.J. Abdul Kalam', 6, 5);

INSERT INTO borrowings (member_id, book_id, borrow_date, due_date, return_date) VALUES
(1, 1, '2025-07-10', '2025-07-20', NULL),
(2, 3, '2025-07-05', '2025-07-15', '2025-07-14'),
(3, 2, '2025-07-12', '2025-07-22', NULL),
(4, 4, '2025-07-01', '2025-07-10', NULL),
(1, 5, '2025-07-15', '2025-07-25', NULL);

-- Books Borrowed by a Member
SELECT b.title, br.borrow_date, br.due_date
FROM borrowings br
JOIN books b ON br.book_id = b.book_id
WHERE br.member_id = 1;

-- Select * from borrowings;

-- Overdue Books
SELECT m.name AS member_name, b.title, br.due_date
FROM borrowings br
JOIN members m ON br.member_id = m.member_id
JOIN books b ON br.book_id = b.book_id
WHERE br.return_date IS NULL AND br.due_date < CURDATE();

-- Most Borrowed Books
SELECT b.title, COUNT(*) AS times_borrowed
FROM borrowings br
JOIN books b ON br.book_id = b.book_id
GROUP BY br.book_id
ORDER BY times_borrowed DESC
LIMIT 5;



