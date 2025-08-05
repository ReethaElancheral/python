
-- Project 18: Voting Registration & Results System

CREATE DATABASE IF NOT EXISTS VotingDB;
USE VotingDB;

CREATE TABLE voters (
    voter_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    CHECK (age >= 18)
);

CREATE TABLE elections (
    election_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100),
    election_date DATE
);

CREATE TABLE candidates (
    candidate_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    election_id INT,
    FOREIGN KEY (election_id) REFERENCES elections(election_id)
);

CREATE TABLE votes (
    vote_id INT PRIMARY KEY AUTO_INCREMENT,
    voter_id INT,
    candidate_id INT,
    status VARCHAR(20) DEFAULT 'pending',
    FOREIGN KEY (voter_id) REFERENCES voters(voter_id) ON DELETE CASCADE,
    FOREIGN KEY (candidate_id) REFERENCES candidates(candidate_id)
);

-- Insert voter
INSERT INTO voters (voter_id, name, age) VALUES (1001, 'Rehan Malik', 25);

-- Transaction: cast vote + log + confirm
START TRANSACTION;
INSERT INTO votes (voter_id, candidate_id, status) VALUES (1001, 1, 'submitted');
UPDATE votes SET status = 'confirmed' WHERE voter_id = 1001 AND candidate_id = 1;
COMMIT;
