-- Project 15: Pet Adoption Registry
CREATE TABLE pets (
    pet_id INT PRIMARY KEY,
    name VARCHAR(100),
    species VARCHAR(50),
    breed VARCHAR(100),
    age INT,
    adopted BOOLEAN,
    owner_name VARCHAR(100)
);

INSERT INTO pets (pet_id, name, species, breed, age, adopted, owner_name) VALUES
(1, 'Buddy', 'Dog', 'German Shepherd', 3, FALSE, NULL),
(2, 'Mittens', 'Cat', 'Siamese', 2, TRUE, 'Anita'),
(3, 'Charlie', 'Dog', 'Beagle', 5, FALSE, NULL),
(4, 'Bella', 'Dog', 'Labrador', 4, TRUE, 'Rajesh'),
(5, 'Luna', 'Cat', 'Persian', 1, FALSE, NULL);

SELECT name, breed, species FROM pets WHERE adopted = FALSE AND age BETWEEN 1 AND 5;
SELECT * FROM pets WHERE breed LIKE '%shepherd%';
SELECT * FROM pets WHERE owner_name IS NULL;
SELECT DISTINCT species FROM pets;
SELECT * FROM pets ORDER BY age ASC, name ASC;