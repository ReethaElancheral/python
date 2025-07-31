-- -----------------------------------------------
-- Project 12: Online Voting Platform
-- Requirements:
-- • Create voting_db
-- • Tables: voters, candidates, votes, elections
-- • A voter can vote once per election
-- • Insert at least 3 elections
-- • SQL tasks:
--    - Count votes per candidate
--    - Find election winners
--    - Update vote records
-- -----------------------------------------------

CREATE DATABASE IF NOT EXISTS voting_db;
USE voting_db;

-- Create elections table
CREATE TABLE elections (
    election_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    election_date DATE NOT NULL
);

-- Create voters table
CREATE TABLE voters (
    voter_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create candidates table
CREATE TABLE candidates (
    candidate_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    election_id INT,
    FOREIGN KEY (election_id) REFERENCES elections(election_id)
);

-- Create votes table
CREATE TABLE votes (
    vote_id INT PRIMARY KEY AUTO_INCREMENT,
    voter_id INT,
    candidate_id INT,
    election_id INT,
    vote_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (voter_id) REFERENCES voters(voter_id),
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id),
    FOREIGN KEY (election_id) REFERENCES elections(election_id),
    UNIQUE (voter_id, election_id) -- ensures one vote per voter per election
);

-- Insert elections
INSERT INTO elections (name, election_date) VALUES
('Presidential Election 2025', '2025-11-05'),
('City Council Election 2025', '2025-12-01'),
('School Board Election 2025', '2025-10-15');

-- Insert voters
INSERT INTO voters (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Carol', 'carol@example.com'),
('David', 'david@example.com'),
('Eva', 'eva@example.com');

-- Insert candidates
INSERT INTO candidates (name, election_id) VALUES
('John Doe', 1),
('Jane Smith', 1),
('Mike Johnson', 2),
('Sara Williams', 2),
('Tom Brown', 3);

-- Insert votes
INSERT INTO votes (voter_id, candidate_id, election_id) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 1, 1),
(4, 2, 1),
(5, 1, 1),
(1, 3, 2),
(2, 3, 2),
(3, 4, 2),
(4, 3, 2),
(5, 4, 2),
(1, 5, 3),
(2, 5, 3),
(3, 5, 3);



-- 1. Count votes per candidate per election
SELECT 
    e.name AS election_name,
    c.name AS candidate_name,
    COUNT(v.vote_id) AS vote_count
FROM votes v
JOIN candidates c ON v.candidate_id = c.candidate_id
JOIN elections e ON v.election_id = e.election_id
GROUP BY v.election_id, v.candidate_id
ORDER BY e.election_id, vote_count DESC;

-- 2. Find election winners (candidate with highest votes per election)
SELECT 
    election_name,
    candidate_name,
    vote_count
FROM (
    SELECT 
        e.name AS election_name,
        c.name AS candidate_name,
        COUNT(v.vote_id) AS vote_count,
        ROW_NUMBER() OVER (PARTITION BY e.election_id ORDER BY COUNT(v.vote_id) DESC) AS rank
    FROM votes v
    JOIN candidates c ON v.candidate_id = c.candidate_id
    JOIN elections e ON v.election_id = e.election_id
    GROUP BY e.election_id, c.candidate_id
) AS ranked
WHERE rank = 1;


-- 3. Update a vote record (change voter's vote in an election)
-- Example: Voter with voter_id=1 changes vote in election_id=1 to candidate_id=2
UPDATE votes
SET candidate_id = 2
WHERE voter_id = 1 AND election_id = 1;
