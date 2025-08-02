-- 1. Online Bookstore Inventory & Sales Analysis
-- Requirements:
-- Create tables: books, authors, orders, customers.
-- Retrieve books with SELECT, filter by genre using WHERE.
-- Use JOINs to combine books with authors and sales.
-- Show total and average sales per author (GROUP BY, AVG()).
-- Filter duplicate books using DISTINCT.
-- Use BETWEEN to filter orders by date.
-- Use a subquery in WHERE to find books never sold.
-- Use CASE WHEN to classify sales performance (low/medium/high).
-- Sort books by revenue and author name.
-- Use UNION to merge physical and eBook sales.

CREATE DATABASE IF NOT EXISTS OnlineBookstoreDB;
USE OnlineBookstoreDB;


CREATE TABLE authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    country VARCHAR(50)
);

CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150),
    author_id INT,
    genre VARCHAR(50),
    price DECIMAL(10,2),
    format ENUM('physical', 'ebook'),
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    customer_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert Sample Data

INSERT INTO authors (name, country) VALUES
('George Orwell', 'UK'),
('Jane Austen', 'UK'),
('Mark Twain', 'USA'),
('J.K. Rowling', 'UK');

INSERT INTO books (title, author_id, genre, price, format) VALUES
('1984', 1, 'Dystopian', 350.00, 'physical'),
('Animal Farm', 1, 'Satire', 200.00, 'ebook'),
('Pride and Prejudice', 2, 'Romance', 300.00, 'physical'),
('Emma', 2, 'Romance', 280.00, 'ebook'),
('Adventures of Huckleberry Finn', 3, 'Adventure', 320.00, 'physical'),
('Harry Potter and the Sorcerer''s Stone', 4, 'Fantasy', 450.00, 'ebook');

INSERT INTO customers (name, email, city) VALUES
('Arjun Rao', 'arjun@example.com', 'Mumbai'),
('Meena Sharma', 'meena@example.com', 'Delhi'),
('John Smith', 'john@example.com', 'New York'),
('Aisha Khan', 'aisha@example.com', 'Bangalore');

INSERT INTO orders (book_id, customer_id, quantity, order_date) VALUES
(1, 1, 2, '2024-12-05'),
(2, 2, 1, '2025-01-15'),
(3, 3, 3, '2025-02-20'),
(5, 4, 1, '2025-03-25'),
(6, 1, 2, '2025-03-30'),
(1, 3, 1, '2025-04-01');


-- 1. Retrieve books with SELECT, filter by genre using WHERE

SELECT title from books where genre = 'Adventure';

-- 2. Use JOINs to combine books with authors and sales (orders)

SELECT b.title, a.name AS author_name, o.quantity, o.order_date
FROM books b
JOIN authors a ON b.author_id = a.author_id
JOIN orders o ON b.book_id = o.book_id;

-- 3. Show total and average sales per author (GROUP BY, AVG())
SELECT a.name AS author_name,
       SUM(o.quantity * b.price) AS total_sales,
       AVG(o.quantity * b.price) AS avg_sales
FROM authors a
JOIN books b ON a.author_id = b.author_id
JOIN orders o ON b.book_id = o.book_id
GROUP BY a.name;

-- 4. Filter duplicate books using DISTINCT
SELECT DISTINCT title FROM books;

-- 5. Use BETWEEN to filter orders by date
SELECT * FROM orders
WHERE order_date BETWEEN '2025-01-01' AND '2025-03-31';

-- 6. Use a subquery in WHERE to find books never sold
SELECT title FROM books
WHERE book_id NOT IN (
    SELECT DISTINCT book_id FROM orders
);

-- 7. Use CASE WHEN to classify sales performance (low/medium/high)
SELECT b.title,
       SUM(o.quantity * b.price) AS total_revenue,
       CASE
           WHEN SUM(o.quantity * b.price) < 500 THEN 'Low'
           WHEN SUM(o.quantity * b.price) BETWEEN 500 AND 1000 THEN 'Medium'
           ELSE 'High'
       END AS performance
FROM books b
JOIN orders o ON b.book_id = o.book_id
GROUP BY b.title;

-- 8. Sort books by revenue and author name
SELECT b.title, a.name AS author_name,
       SUM(o.quantity * b.price) AS revenue
FROM books b
JOIN authors a ON b.author_id = a.author_id
JOIN orders o ON b.book_id = o.book_id
GROUP BY b.book_id, a.name
ORDER BY revenue DESC, a.name;

-- 9. Use UNION to merge physical and eBook sales
SELECT b.title, 'Physical' AS format, SUM(o.quantity) AS total_sold
FROM books b
JOIN orders o ON b.book_id = o.book_id
WHERE b.format = 'physical'
GROUP BY b.book_id

UNION

SELECT b.title, 'eBook' AS format, SUM(o.quantity) AS total_sold
FROM books b
JOIN orders o ON b.book_id = o.book_id
WHERE b.format = 'ebook'
GROUP BY b.book_id;
