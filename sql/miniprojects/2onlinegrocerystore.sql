CREATE DATABASE grocery_store;
USE grocery_store;

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE suppliers (
    supplier_id INT PRIMARY KEY AUTO_INCREMENT,
    supplier_name VARCHAR(100) NOT NULL,
    contact_email VARCHAR(100) UNIQUE
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL UNIQUE,
    category_id INT NOT NULL,
    supplier_id INT NOT NULL,
    price DECIMAL(8, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    discontinued BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

INSERT INTO categories (category_name) VALUES
('Fruits'),
('Vegetables'),
('Dairy'),
('Snacks'),
('Beverages');

INSERT INTO suppliers (supplier_name, contact_email) VALUES
('FreshFarm Ltd.', 'fresh@farm.com'),
('GreenGrow Co.', 'green@grow.com'),
('MilkyWay Dairies', 'milk@way.com'),
('SnackBox Pvt. Ltd.', 'snack@box.com'),
('CoolDrinks Inc.', 'cool@drinks.com');


INSERT INTO products (product_name, category_id, supplier_id, price, stock, discontinued) VALUES
('Apple', 1, 1, 50.00, 100, FALSE),
('Banana', 1, 1, 30.00, 80, FALSE),
('Orange', 1, 1, 60.00, 60, FALSE),
('Tomato', 2, 2, 25.00, 90, FALSE),
('Carrot', 2, 2, 20.00, 70, FALSE),
('Spinach', 2, 2, 15.00, 40, FALSE),
('Milk', 3, 3, 45.00, 120, FALSE),
('Cheese', 3, 3, 120.00, 50, FALSE),
('Butter', 3, 3, 80.00, 45, FALSE),
('Chips', 4, 4, 20.00, 200, FALSE),
('Cookies', 4, 4, 30.00, 150, FALSE),
('Chocolate Bar', 4, 4, 25.00, 180, FALSE),
('Cola', 5, 5, 40.00, 100, FALSE),
('Orange Juice', 5, 5, 50.00, 70, FALSE),
('Water Bottle', 5, 5, 15.00, 300, FALSE),
('Yogurt', 3, 3, 35.00, 60, FALSE),
('Cabbage', 2, 2, 18.00, 55, FALSE),
('Lemon', 1, 1, 10.00, 95, FALSE),
('Ice Tea', 5, 5, 45.00, 80, FALSE),
('Energy Drink', 5, 5, 70.00, 40, FALSE);


UPDATE products
SET stock = stock + 50
WHERE product_name = 'Apple';


UPDATE products SET discontinued = TRUE WHERE product_name = 'Energy Drink';

DELETE FROM products WHERE product_id = 19;


-- Group Products by Category and Count
SELECT c.category_name, COUNT(p.product_id) AS product_count
FROM products p
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name;




