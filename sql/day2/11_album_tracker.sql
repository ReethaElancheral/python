-- Project 11: Music Album Tracker
CREATE TABLE albums (
    album_id INT PRIMARY KEY,
    artist VARCHAR(100),
    genre VARCHAR(50),
    title VARCHAR(100),
    release_year INT,
    price DECIMAL(10,2)
);

INSERT INTO albums (album_id, artist, genre, title, release_year, price) VALUES
(1, 'Miles Davis', 'Jazz', 'Kind of Blue', 2019, 15.99),
(2, 'Ludovico Einaudi', 'Classical', 'Elements', 2017, 12.99),
(3, 'John Coltrane', 'Jazz', 'A Love Supreme', 2016, 14.99),
(4, 'Beethoven', 'Classical', 'Symphony No. 9', 2015, NULL),
(5, 'Adele', 'Pop', '25', 2018, 9.99),
(6, 'Ella Fitzgerald', 'Jazz', 'Ella and Louis', 2020, 13.99),
(7, 'Mozart', 'Classical', 'Requiem', 2014, 11.99),
(8, 'Coldplay', 'Rock', 'A Head Full of Dreams', 2017, 10.99),
(9, 'Norah Jones', 'Jazz', 'Come Away with Me', 2019, NULL),
(10, 'Vivaldi', 'Classical', 'The Four Seasons', 2021, 14.50);

SELECT title, artist, price FROM albums WHERE genre IN ('Jazz', 'Classical') AND release_year > 2015;
SELECT DISTINCT artist FROM albums;
SELECT * FROM albums WHERE title LIKE '%Love%';
SELECT * FROM albums WHERE price IS NULL;
SELECT * FROM albums ORDER BY release_year DESC, title ASC;