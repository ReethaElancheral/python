-- Project 8: Movie Rental System
CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50),
    price DECIMAL(10,2),
    rating DECIMAL(3,1),
    available BOOLEAN
);

INSERT INTO movies (movie_id, title, genre, price, rating, available) VALUES
(1, 'Star Wars: A New Hope', 'Action', 3.99, 4.8, TRUE),
(2, 'Star Trek', 'Sci-Fi', 2.99, 4.5, TRUE),
(3, 'The Silent Star', 'Thriller', 3.50, NULL, FALSE),
(4, 'Action Heroes', 'Action', 4.00, 4.2, TRUE),
(5, 'Thriller Night', 'Thriller', 3.75, 4.6, TRUE);

SELECT title, genre, rating FROM movies WHERE available = TRUE AND genre IN ('Action', 'Thriller');
SELECT * FROM movies WHERE title LIKE '%Star%';
SELECT * FROM movies WHERE rating IS NULL;
SELECT DISTINCT genre FROM movies;
SELECT * FROM movies ORDER BY rating DESC, price ASC;