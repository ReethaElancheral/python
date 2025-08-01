-- Project 9: Hotel Guest Registry
CREATE TABLE guests (
    guest_id INT PRIMARY KEY,
    name VARCHAR(100),
    room_type VARCHAR(50),
    check_in DATE,
    check_out DATE,
    payment_status VARCHAR(20)
);

INSERT INTO guests (guest_id, name, room_type, check_in, check_out, payment_status) VALUES
(1, 'Karan Singh', 'Deluxe', '2025-07-10', '2025-07-15', 'Paid'),
(2, 'Kavya Patel', 'Suite', '2025-07-12', '2025-07-18', NULL),
(3, 'Rohan Mehta', 'Standard', '2025-07-15', '2025-07-17', 'Pending'),
(4, 'Kiran Kumar', 'Deluxe', '2025-07-14', '2025-07-20', 'Paid'),
(5, 'Priya Sharma', 'Standard', '2025-07-16', '2025-07-22', NULL);

SELECT name, room_type, check_in FROM guests WHERE check_in BETWEEN '2025-07-01' AND '2025-07-31';
SELECT * FROM guests WHERE payment_status IS NULL;
SELECT * FROM guests WHERE name LIKE 'K%';
SELECT DISTINCT room_type FROM guests;
SELECT * FROM guests ORDER BY check_out DESC, name ASC;