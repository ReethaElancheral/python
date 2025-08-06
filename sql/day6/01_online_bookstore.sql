--  1. Online Bookstore Database 
-- Requirements: 
--  Tables: books, authors, genres, publishers, sales 
--  Normalize database to 3NF (separate genres, authors, etc.). 
--  Create a clustered index on book_id, non-clustered on title and author_id. 
--  Use EXPLAIN to optimize book search by title and author. 
--  Use JOIN to list books with publisher and genre. 
--  Create a denormalized summary table for monthly book sales. 
--  Add pagination to best-selling books using LIMIT. 


CREATE DATABASE IF NOT EXISTS bookstore_db;
USE bookstore_db;

-- 2. Normalized Tables
CREATE TABLE authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(50)
);

CREATE TABLE publishers (
    publisher_id INT PRIMARY KEY AUTO_INCREMENT,
    publisher_name VARCHAR(100)
);

CREATE TABLE books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    author_id INT,
    genre_id INT,
    publisher_id INT,
    price DECIMAL(10,2),
    published_date DATE,
    INDEX idx_title (title),                 -- Non-clustered index
    INDEX idx_author_id (author_id),         -- Non-clustered index
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- 3. Denormalized Summary Table
CREATE TABLE monthly_sales_summary (
    book_id INT,
    total_sales INT,
    sale_month VARCHAR(7), -- Format: YYYY-MM
    PRIMARY KEY (book_id, sale_month)
);

-- 4. Sample Data
INSERT INTO authors (name) VALUES ('J.K. Rowling'), ('George R.R. Martin');
INSERT INTO genres (genre_name) VALUES ('Fantasy'), ('Fiction');
INSERT INTO publishers (publisher_name) VALUES ('Bloomsbury'), ('Penguin');

INSERT INTO books (title, author_id, genre_id, publisher_id, price, published_date)
VALUES 
('Harry Potter', 1, 1, 1, 499.99, '2000-07-08'),
('Game of Thrones', 2, 1, 2, 699.99, '1996-08-01');

INSERT INTO sales (book_id, quantity, sale_date)
VALUES 
(1, 10, '2025-08-01'),
(2, 5, '2025-08-01'),
(1, 3, '2025-08-02');

-- 5. JOIN Query: Books with Publisher and Genre
SELECT 
    b.title, a.name AS author, g.genre_name, p.publisher_name, b.price
FROM books b
JOIN authors a ON b.author_id = a.author_id
JOIN genres g ON b.genre_id = g.genre_id
JOIN publishers p ON b.publisher_id = p.publisher_id;

-- 6. EXPLAIN Optimization
EXPLAIN SELECT * FROM books WHERE title = 'Harry Potter';
EXPLAIN SELECT * FROM books WHERE author_id = 1;

-- 7. Pagination
SELECT * FROM books ORDER BY price DESC LIMIT 0, 5;

-- 8. Summary Table Update Example
INSERT INTO monthly_sales_summary (book_id, total_sales, sale_month)
SELECT book_id, SUM(quantity), DATE_FORMAT(sale_date, '%Y-%m')
FROM sales
GROUP BY book_id, DATE_FORMAT(sale_date, '%Y-%m');
