--  3. University Result Management 
-- Requirements: 
--  View view_student_grades to show subject-wise marks (hiding evaluator 
-- info). 
--  Procedure update_grade() to update a student’s marks with audit log. 
--  Function calculate_gpa(student_id) to return GPA. 
--  Trigger before_update_grades to prevent update if locked.
--  Use abstraction view view_final_results for students to view only final 
-- marks. 

-- Create Database
CREATE DATABASE IF NOT EXISTS UniversityResultDB;
USE UniversityResultDB;

-- Table: students
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    department VARCHAR(100)
);

-- Table: subjects
CREATE TABLE subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(100)
);

-- Table: grades
CREATE TABLE grades (
    grade_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject_id INT,
    marks INT,
    evaluator_name VARCHAR(100),
    is_locked BOOLEAN DEFAULT FALSE,
    updated_at DATETIME,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- Table: audit_log
CREATE TABLE audit_log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject_id INT,
    old_marks INT,
    new_marks INT,
    updated_at DATETIME
);

-- Sample Inserts
INSERT INTO students (name, department)
VALUES ('Aisha Kumar', 'Computer Science'),
       ('Rohan Mehta', 'Mechanical Engineering');

INSERT INTO subjects (subject_name)
VALUES ('Mathematics'), ('Physics'), ('Chemistry');

-- Sample grade entries
INSERT INTO grades (student_id, subject_id, marks, evaluator_name, updated_at)
VALUES 
(1, 1, 80, 'Prof. Sharma', NOW()),
(1, 2, 85, 'Prof. Sharma', NOW()),
(2, 1, 75, 'Prof. Iyer', NOW()),
(2, 3, 78, 'Prof. Iyer', NOW());

-- ✅ View: view_student_grades (hiding evaluator info)
CREATE OR REPLACE VIEW view_student_grades AS
SELECT 
    g.grade_id,
    s.name AS student_name,
    subj.subject_name,
    g.marks
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN subjects subj ON g.subject_id = subj.subject_id;

-- ✅ View: view_final_results (only final marks)
CREATE OR REPLACE VIEW view_final_results AS
SELECT 
    s.name AS student_name,
    subj.subject_name,
    g.marks
FROM grades g
JOIN students s ON g.student_id = s.student_id
JOIN subjects subj ON g.subject_id = subj.subject_id
WHERE g.is_locked = TRUE;

-- ✅ Function: calculate_gpa(student_id)
DELIMITER //
CREATE FUNCTION calculate_gpa(stud_id INT)
RETURNS DECIMAL(5,2)
DETERMINISTIC
BEGIN
    DECLARE avg_gpa DECIMAL(5,2);
    SELECT AVG(marks) INTO avg_gpa
    FROM grades
    WHERE student_id = stud_id;
    RETURN avg_gpa;
END;
//
DELIMITER ;

-- ✅ Procedure: update_grade(student_id, subject_id, new_marks)
DELIMITER //
CREATE PROCEDURE update_grade(
    IN stud_id INT,
    IN subj_id INT,
    IN new_marks INT
)
BEGIN
    DECLARE existing_marks INT;
    DECLARE locked BOOLEAN;

    SELECT marks, is_locked INTO existing_marks, locked
    FROM grades 
    WHERE student_id = stud_id AND subject_id = subj_id;

    IF locked THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Grades are locked and cannot be updated.';
    ELSE
        UPDATE grades
        SET marks = new_marks, updated_at = NOW()
        WHERE student_id = stud_id AND subject_id = subj_id;

        INSERT INTO audit_log(student_id, subject_id, old_marks, new_marks, updated_at)
        VALUES (stud_id, subj_id, existing_marks, new_marks, NOW());
    END IF;
END;
//
DELIMITER ;

-- ✅ Trigger: before updating grades — block if locked
DELIMITER //
CREATE TRIGGER before_update_grades
BEFORE UPDATE ON grades
FOR EACH ROW
BEGIN
    IF OLD.is_locked THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot update locked grades.';
    END IF;
END;
//
DELIMITER ;

-- ✅ Test the GPA function
-- SELECT calculate_gpa(1);

-- ✅ Test procedure to update marks (run only if not locked)
-- CALL update_grade(1, 1, 92);

-- ✅ Lock a grade and test trigger
-- UPDATE grades SET is_locked = TRUE WHERE student_id = 1 AND subject_id = 1;
-- Attempting an update will now be blocked by the trigger.

-- ✅ Use views
-- SELECT * FROM view_student_grades;
-- SELECT * FROM view_final_results;
