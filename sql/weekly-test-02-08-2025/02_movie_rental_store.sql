-- 2. Movie Rental Store Management
-- Requirements:
-- Tables: movies, customers, rentals, genres.
-- Use subqueries to find top 3 rented movies per genre.
-- Use LIKE to search movies by partial title.
-- Aggregate revenue per genre using GROUP BY, SUM().
-- Filter null return dates (IS NULL) to find unreturned movies.
-- Use CASE to label late returns.
-- Combine rental and purchase data using UNION ALL.
-- Use JOIN to fetch full customer and rental info.


CREATE DATABASE IF NOT EXISTS MovieRentalDB;
USE MovieRentalDB;

CREATE TABLE genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE movies (
    movie_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    genre_id INT,
    price DECIMAL(6,2),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE rentals (
    rental_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    customer_id INT,
    rental_date DATE,
    return_date DATE,
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Optional: Purchases Table (for UNION ALL)
CREATE TABLE purchases (
    purchase_id INT PRIMARY KEY AUTO_INCREMENT,
    movie_id INT,
    customer_id INT,
    purchase_date DATE,
    price DECIMAL(6,2),
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert Sample Data

INSERT INTO genres (name) VALUES
('Action'), ('Comedy'), ('Drama'), ('Horror');

INSERT INTO movies (title, genre_id, price) VALUES
('Avengers: Endgame', 1, 150.00),
('John Wick', 1, 120.00),
('The Mask', 2, 100.00),
('Jumanji', 2, 110.00),
('The Godfather', 3, 160.00),
('The Conjuring', 4, 130.00),
('Insidious', 4, 140.00);

INSERT INTO customers (name, email, city) VALUES
('Ravi Verma', 'ravi@example.com', 'Mumbai'),
('Sara Khan', 'sara@example.com', 'Delhi'),
('David Miller', 'david@example.com', 'London'),
('Anita Joshi', 'anita@example.com', 'Bangalore');

INSERT INTO rentals (movie_id, customer_id, rental_date, return_date) VALUES
(1, 1, '2025-07-01', '2025-07-05'),
(2, 2, '2025-07-02', '2025-07-03'),
(3, 3, '2025-07-03', NULL),
(4, 1, '2025-07-04', '2025-07-10'),
(5, 2, '2025-07-05', '2025-07-12'),
(6, 3, '2025-07-06', NULL),
(7, 4, '2025-07-07', '2025-07-08'),
(1, 4, '2025-07-08', '2025-07-11'),
(3, 2, '2025-07-09', '2025-07-13');

INSERT INTO purchases (movie_id, customer_id, purchase_date, price) VALUES
(1, 1, '2025-07-10', 150.00),
(5, 3, '2025-07-12', 160.00),
(2, 4, '2025-07-15', 120.00);

-- Queries

-- 1. Subqueries: Top 3 rented movies per genre
SELECT m.title, g.name AS genre_name, COUNT(*) AS total_rentals
FROM movies m
JOIN genres g ON m.genre_id = g.genre_id
JOIN rentals r ON m.movie_id = r.movie_id
GROUP BY m.movie_id, g.name
HAVING (SELECT COUNT(*) FROM rentals r2
        JOIN movies m2 ON r2.movie_id = m2.movie_id
        WHERE m2.genre_id = m.genre_id
        AND r2.movie_id = m.movie_id) >= 1
ORDER BY g.name, total_rentals DESC
LIMIT 3;

-- 2. Search movies by partial title using LIKE
SELECT * FROM movies
WHERE title LIKE '%man%';

-- 3. Aggregate revenue per genre
SELECT g.name AS genre_name,
       SUM(m.price) AS total_revenue
FROM genres g
JOIN movies m ON g.genre_id = m.genre_id
JOIN rentals r ON m.movie_id = r.movie_id
GROUP BY g.genre_id;

-- 4. Find unreturned movies (return_date IS NULL)
SELECT r.rental_id, c.name AS customer_name, m.title, r.rental_date
FROM rentals r
JOIN customers c ON r.customer_id = c.customer_id
JOIN movies m ON r.movie_id = m.movie_id
WHERE r.return_date IS NULL;

-- 5. CASE WHEN to label late returns
-- Assume rentals should be returned in 3 days
SELECT r.rental_id, m.title, r.rental_date, r.return_date,
       CASE
           WHEN DATEDIFF(r.return_date, r.rental_date) <= 3 THEN 'On Time'
           WHEN r.return_date IS NULL THEN 'Not Returned'
           ELSE 'Late'
       END AS return_status
FROM rentals r
JOIN movies m ON r.movie_id = m.movie_id;

-- 6. UNION ALL: Combine rental and purchase data
SELECT c.name AS customer_name, m.title, 'Rental' AS type, r.rental_date AS date, m.price
FROM rentals r
JOIN movies m ON r.movie_id = m.movie_id
JOIN customers c ON r.customer_id = c.customer_id

UNION ALL

SELECT c.name, m.title, 'Purchase', p.purchase_date, p.price
FROM purchases p
JOIN movies m ON p.movie_id = m.movie_id
JOIN customers c ON p.customer_id = c.customer_id;

-- 7. JOIN to fetch full customer and rental info
SELECT c.customer_id, c.name AS customer_name, c.email, c.city,
       m.title AS movie_title, r.rental_date, r.return_date
FROM customers c
JOIN rentals r ON c.customer_id = r.customer_id
JOIN movies m ON r.movie_id = m.movie_id;
