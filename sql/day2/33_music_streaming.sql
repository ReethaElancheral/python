-- Project 13: Music Streaming Insights

CREATE DATABASE IF NOT EXISTS music_streaming_db;
USE music_streaming_db;



CREATE TABLE artists (
    artist_id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE songs (
    song_id INT PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(50),
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE listeners (
    listener_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE plays (
    play_id INT PRIMARY KEY,
    song_id INT,
    listener_id INT,
    play_duration INT,
    play_date DATE,
    FOREIGN KEY (song_id) REFERENCES songs(song_id),
    FOREIGN KEY (listener_id) REFERENCES listeners(listener_id)
);



INSERT INTO artists (artist_id, name) VALUES
(1, 'A. R. Rahman'),
(2, 'Shreya Ghoshal'),
(3, 'Arijit Singh'),
(4, 'Neha Kakkar');

INSERT INTO songs (song_id, title, genre, artist_id) VALUES
(1, 'Tum Hi Ho', 'Romantic', 3),
(2, 'Jai Ho', 'World', 1),
(3, 'Sun Raha Hai', 'Sad', 2),
(4, 'Kar Gayi Chull', 'Pop', 4),
(5, 'Kun Faya Kun', 'Spiritual', 1);

INSERT INTO listeners (listener_id, name, city) VALUES
(1, 'Rajeev Reddy', 'Hyderabad'),
(2, 'Anjali Menon', 'Bangalore'),
(3, 'Devansh Patel', 'Ahmedabad'),
(4, 'Kriti Rao', 'Mumbai');

INSERT INTO plays (play_id, song_id, listener_id, play_duration, play_date) VALUES
(1, 1, 1, 210, '2024-06-01'),
(2, 2, 2, 250, '2024-06-01'),
(3, 3, 3, 230, '2024-06-02'),
(4, 1, 1, 210, '2024-06-03'),
(5, 1, 2, 215, '2024-06-04'),
(6, 1, 3, 220, '2024-06-04'),
(7, 2, 4, 245, '2024-06-05'),
(8, 5, 1, 300, '2024-06-06'),
(9, 5, 3, 310, '2024-06-07'),
(10, 4, 2, 200, '2024-06-08'),
(11, 3, 4, 235, '2024-06-09'),
(12, 3, 1, 240, '2024-06-10'),
(13, 3, 2, 220, '2024-06-11'),
(14, 3, 3, 225, '2024-06-12'),
(15, 3, 4, 230, '2024-06-13');

-- Queries

-- 1. Total plays per song
SELECT 
    s.title,
    COUNT(p.play_id) AS total_plays
FROM songs s
LEFT JOIN plays p ON s.song_id = p.song_id
GROUP BY s.song_id, s.title;

-- 2. Average play duration per genre
SELECT 
    s.genre,
    AVG(p.play_duration) AS avg_duration
FROM songs s
JOIN plays p ON s.song_id = p.song_id
GROUP BY s.genre;

-- 3. Artists with songs played > 1,000 times
SELECT 
    a.name AS artist_name,
    COUNT(p.play_id) AS total_plays
FROM artists a
JOIN songs s ON a.artist_id = s.artist_id
JOIN plays p ON s.song_id = p.song_id
GROUP BY a.artist_id, a.name
HAVING total_plays > 1000;

-- 4. INNER JOIN: songs ↔ plays
SELECT 
    s.title,
    l.name AS listener,
    p.play_duration,
    p.play_date
FROM plays p
JOIN songs s ON p.song_id = s.song_id
JOIN listeners l ON p.listener_id = l.listener_id;

-- 5. RIGHT JOIN: listeners ↔ plays (listeners who may not have played)
SELECT 
    l.name,
    p.play_duration
FROM listeners l
RIGHT JOIN plays p ON l.listener_id = p.listener_id;

-- 6. SELF JOIN to list listeners who play similar genres
SELECT 
    l1.name AS listener1,
    l2.name AS listener2,
    s1.genre
FROM plays p1
JOIN songs s1 ON p1.song_id = s1.song_id
JOIN listeners l1 ON p1.listener_id = l1.listener_id
JOIN plays p2 ON s1.genre = (SELECT genre FROM songs WHERE song_id = p2.song_id)
JOIN listeners l2 ON p2.listener_id = l2.listener_id
WHERE l1.listener_id < l2.listener_id;
