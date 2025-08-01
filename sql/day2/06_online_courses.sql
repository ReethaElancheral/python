-- Project 6: Online Course Catalog
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    title VARCHAR(100),
    category VARCHAR(50),
    duration INT,
    price DECIMAL(10,2),
    instructor VARCHAR(100),
    status VARCHAR(20)
);

INSERT INTO courses (course_id, title, category, duration, price, instructor, status) VALUES
(1, 'Data Science Basics', 'Tech', 30, 900, 'John Doe', 'Active'),
(2, 'Business Management 101', 'Business', 45, 1200, 'Jane Smith', 'Inactive'),
(3, 'Advanced Python', 'Tech', 40, 1500, NULL, 'Active'),
(4, 'Digital Marketing', 'Business', 25, 800, 'Mike Johnson', 'Active'),
(5, 'Data Analytics', 'Tech', 35, 950, 'John Doe', 'Active');


SELECT title, category, price FROM courses WHERE status = 'active' AND price < 1000;
SELECT DISTINCT instructor FROM courses;
SELECT * FROM courses WHERE title LIKE 'Data%';
SELECT * FROM courses WHERE category IN ('Tech', 'Business');
SELECT * FROM courses WHERE instructor IS NULL;
SELECT * FROM courses ORDER BY price DESC, duration ASC;