-- 9. Music Streaming Service
-- Requirements:
-- Tables: songs, artists, users, play_history.
-- Use JOIN to show who listened to which song.
-- Use GROUP BY + COUNT() to get top songs.
-- Use ORDER BY for most played artists.
-- Use subquery to get users who listened to the same artist >10 times.
-- Use CASE to label users as “Light”, “Moderate”, “Heavy” listeners.
-- Filter by LIKE '%Love%' for romantic songs.


CREATE DATABASE IF NOT EXISTS MusicStreamingDB;
USE MusicStreamingDB;

CREATE TABLE artists (
    artist_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE songs (
    song_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    genre VARCHAR(50),
    artist_id INT,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE play_history (
    play_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    song_id INT,
    play_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (song_id) REFERENCES songs(song_id)
);

-- Insert Sample Data

INSERT INTO artists (name) VALUES 
('Arijit Singh'),
('Taylor Swift'),
('The Weeknd'),
('Shreya Ghoshal');

INSERT INTO songs (title, genre, artist_id) VALUES 
('Love Story', 'Pop', 2),
('Blinding Lights', 'R&B', 3),
('Tum Hi Ho', 'Romantic', 1),
('Channa Mereya', 'Romantic', 1),
('Blank Space', 'Pop', 2),
('Ghar More Pardesiya', 'Classical', 4);

INSERT INTO users (name, email) VALUES 
('Rahul Mehta', 'rahul@example.com'),
('Ananya Roy', 'ananya@example.com'),
('Karan Patel', 'karan@example.com'),
('Simran Kaur', 'simran@example.com');

INSERT INTO play_history (user_id, song_id, play_time) VALUES
(1, 1, '2025-07-01 10:00:00'),
(1, 3, '2025-07-01 10:05:00'),
(1, 2, '2025-07-01 10:10:00'),
(2, 3, '2025-07-01 11:00:00'),
(2, 4, '2025-07-01 11:05:00'),
(3, 1, '2025-07-01 12:00:00'),
(3, 5, '2025-07-01 12:05:00'),
(3, 1, '2025-07-01 13:00:00'),
(3, 1, '2025-07-02 14:00:00'),
(4, 6, '2025-07-01 14:00:00'),
(4, 3, '2025-07-01 14:30:00'),
(4, 3, '2025-07-01 15:00:00'),
(4, 3, '2025-07-01 15:30:00'),
(4, 3, '2025-07-01 16:00:00'),
(4, 3, '2025-07-01 16:30:00'),
(4, 3, '2025-07-01 17:00:00'),
(4, 3, '2025-07-01 17:30:00'),
(4, 3, '2025-07-01 18:00:00'),
(4, 3, '2025-07-01 18:30:00');

-- Queries

-- 1. JOIN to show who listened to which song
SELECT u.name AS user_name, s.title AS song_title, a.name AS artist_name, ph.play_time
FROM play_history ph
JOIN users u ON ph.user_id = u.user_id
JOIN songs s ON ph.song_id = s.song_id
JOIN artists a ON s.artist_id = a.artist_id;

-- 2. GROUP BY + COUNT() to get top songs
SELECT s.title, COUNT(*) AS play_count
FROM play_history ph
JOIN songs s ON ph.song_id = s.song_id
GROUP BY ph.song_id
ORDER BY play_count DESC;

-- 3. ORDER BY for most played artists
SELECT a.name AS artist_name, COUNT(*) AS total_plays
FROM play_history ph
JOIN songs s ON ph.song_id = s.song_id
JOIN artists a ON s.artist_id = a.artist_id
GROUP BY a.artist_id
ORDER BY total_plays DESC;

-- 4. Subquery to get users who listened to the same artist more than 10 times
SELECT DISTINCT u.name
FROM users u
JOIN play_history ph ON u.user_id = ph.user_id
JOIN songs s ON ph.song_id = s.song_id
WHERE s.artist_id IN (
    SELECT artist_id
    FROM play_history ph
    JOIN songs s ON ph.song_id = s.song_id
    GROUP BY s.artist_id, ph.user_id
    HAVING COUNT(*) > 10
);

-- 5. CASE to label users as “Light”, “Moderate”, “Heavy” listeners
SELECT u.name, COUNT(ph.play_id) AS total_plays,
       CASE 
           WHEN COUNT(ph.play_id) < 5 THEN 'Light'
           WHEN COUNT(ph.play_id) BETWEEN 5 AND 10 THEN 'Moderate'
           ELSE 'Heavy'
       END AS listener_type
FROM users u
LEFT JOIN play_history ph ON u.user_id = ph.user_id
GROUP BY u.user_id;

-- 6. Filter by LIKE '%Love%' for romantic songs
SELECT s.title, a.name AS artist_name
FROM songs s
JOIN artists a ON s.artist_id = a.artist_id
WHERE s.title LIKE '%Love%' OR s.genre LIKE '%Romantic%';
