
-- 4. Bookstore Catalog

-- Create table
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    author VARCHAR(100),
    genre VARCHAR(50),
    price DECIMAL(10,2),
    published_year INT,
    stock INT
);

INSERT INTO books (book_id, title, author, genre, price, published_year, stock) VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 450.00, 2012, 30),
(2, 'To Kill a Mockingbird', 'Harper Lee', 'Fiction', 400.00, 2015, 25),
(3, 'The Silent Patient', 'Alex Michaelides', 'Thriller', 480.00, 2020, 15),
(4, 'Educated', 'Tara Westover', 'Memoir', 550.00, 2018, NULL),
(5, 'Becoming', 'Michelle Obama', 'Biography', 500.00, 2016, 20),
(6, 'The Subtle Art of Not Giving a F*ck', 'Mark Manson', 'Self-help', 350.00, 2019, 40),
(7, 'Sapiens', 'Yuval Noah Harari', 'History', 600.00, 2017, 10),
(8, 'The Alchemist', 'Paulo Coelho', 'Fiction', 300.00, 2010, 50),
(9, 'The Power of Habit', 'Charles Duhigg', 'Self-help', 420.00, 2012, 35),
(10, 'The Martian', 'Andy Weir', 'Science Fiction', 480.00, 2014, 28);

-- Get all fiction books priced under 500
SELECT title, author, price FROM books
WHERE genre = 'Fiction' AND price < 500;

-- List all distinct genres
SELECT DISTINCT genre FROM books;

-- Find titles that start with "The"
SELECT * FROM books
WHERE title LIKE 'The%';

-- Filter books published between 2010 and 2023
SELECT * FROM books
WHERE published_year BETWEEN 2010 AND 2023;

-- Identify books with NULL stock values
SELECT * FROM books
WHERE stock IS NULL;

-- Sort by published_year DESC, then title ASC
SELECT * FROM books
ORDER BY published_year DESC, title ASC;
