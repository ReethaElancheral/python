-- Project 11: Online Bookstore Analytics

CREATE DATABASE IF NOT EXISTS bookstore_db;
USE bookstore_db;


CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(150),
    author_id INT,
    genre VARCHAR(50),
    rating FLOAT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY,
    book_id INT,
    customer_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);



INSERT INTO authors (author_id, name) VALUES
(1, 'Chetan Bhagat'),
(2, 'Arundhati Roy'),
(3, 'Amish Tripathi'),
(4, 'Rujuta Diwekar');

INSERT INTO books (book_id, title, author_id, genre, rating) VALUES
(1, 'Half Girlfriend', 1, 'Romance', 4.2),
(2, 'The God of Small Things', 2, 'Fiction', 4.6),
(3, 'Shiva Trilogy', 3, 'Mythology', 4.8),
(4, 'Indian Superfoods', 4, 'Health', 4.7),
(5, '2 States', 1, 'Romance', 4.0);

INSERT INTO customers (customer_id, name, email) VALUES
(1, 'Rahul Kumar', 'rahul@example.com'),
(2, 'Sneha Patel', 'sneha@example.com'),
(3, 'Ajay Singh', 'ajay@example.com'),
(4, 'Neha Reddy', 'neha@example.com');

INSERT INTO sales (sale_id, book_id, customer_id, quantity, sale_date) VALUES
(1, 1, 1, 1, '2024-01-10'),
(2, 2, 1, 2, '2024-01-12'),
(3, 3, 2, 3, '2024-01-15'),
(4, 4, 2, 1, '2024-01-16'),
(5, 2, 3, 2, '2024-01-20'),
(6, 3, 3, 5, '2024-01-21'),
(7, 4, 4, 1, '2024-01-22'),
(8, 3, 4, 4, '2024-01-23'),
(9, 2, 4, 2, '2024-01-24'),
(10, 3, 1, 2, '2024-01-25');



-- 1. Top-selling authors (GROUP BY, SUM)
SELECT 
    a.name AS author_name,
    SUM(s.quantity) AS total_books_sold
FROM authors a
JOIN books b ON a.author_id = b.author_id
JOIN sales s ON b.book_id = s.book_id
GROUP BY a.author_id, a.name
ORDER BY total_books_sold DESC;

-- 2. Books with rating over 4.5 and sold more than 100 times
SELECT 
    b.title,
    SUM(s.quantity) AS total_sold,
    b.rating
FROM books b
JOIN sales s ON b.book_id = s.book_id
WHERE b.rating > 4.5
GROUP BY b.book_id, b.title, b.rating
HAVING total_sold > 100;

-- 3. Customers with > 5 purchases (HAVING)
SELECT 
    c.name,
    COUNT(s.sale_id) AS purchases
FROM customers c
JOIN sales s ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.name
HAVING purchases > 5;

-- 4. INNER JOIN books ↔ sales ↔ customers
SELECT 
    b.title,
    c.name AS customer_name,
    s.quantity,
    s.sale_date
FROM sales s
INNER JOIN books b ON s.book_id = b.book_id
INNER JOIN customers c ON s.customer_id = c.customer_id;

-- 5. FULL OUTER JOIN authors ↔ books (Simulated using UNION)
SELECT 
    a.name AS author_name,
    b.title AS book_title
FROM authors a
LEFT JOIN books b ON a.author_id = b.author_id
UNION
SELECT 
    a.name,
    b.title
FROM books b
RIGHT JOIN authors a ON a.author_id = b.author_id;

-- 6. SELF JOIN on books with same genre
SELECT 
    b1.title AS book1,
    b2.title AS book2,
    b1.genre
FROM books b1
JOIN books b2 ON b1.genre = b2.genre AND b1.book_id < b2.book_id;
