CREATE DATABASE ecommerce; 
USE ecommerce; 
 
CREATE TABLE customers ( 
    customer_id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(100), 
    email VARCHAR(100) UNIQUE, 
    phone_number VARCHAR(15), 
    address TEXT, 
    registration_date DATE 
); 
 
CREATE TABLE products ( 
    product_id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(100), 
    category VARCHAR(50), 
    price DECIMAL(10,2), 
    stock_quantity INT 
); 
 
CREATE TABLE orders ( 
    order_id INT PRIMARY KEY AUTO_INCREMENT, 
    customer_id INT, 
    order_date DATE, 
    total_amount DECIMAL(10,2), 
    order_status VARCHAR(20), 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) 
);
CREATE TABLE order_details ( 
    order_detail_id INT PRIMARY KEY AUTO_INCREMENT, 
    order_id INT, 
    product_id INT, 
    quantity INT, 
    subtotal_price DECIMAL(10,2), 
    FOREIGN KEY (order_id) REFERENCES orders(order_id), 
    FOREIGN KEY (product_id) REFERENCES products(product_id) 
); 
 
CREATE TABLE payments ( 
    payment_id INT PRIMARY KEY AUTO_INCREMENT, 
    order_id INT, 
    payment_method VARCHAR(50), 
    payment_status VARCHAR(20), 
    payment_date DATE, 
    FOREIGN KEY (order_id) REFERENCES orders(order_id) 
); 
 
CREATE TABLE shipments ( 
    shipment_id INT PRIMARY KEY AUTO_INCREMENT, 
    order_id INT, 
    shipment_date DATE, 
    delivery_status VARCHAR(50), 
    FOREIGN KEY (order_id) REFERENCES orders(order_id) 
);

CREATE TABLE coupons (
    coupon_id INT PRIMARY KEY AUTO_INCREMENT,
    code VARCHAR(20) UNIQUE,
    discount_percent INT CHECK (discount_percent BETWEEN 1 AND 100),
    valid_from DATE,
    valid_to DATE,
    usage_limit INT
);

CREATE TABLE admin_users (
    admin_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),
    role VARCHAR(50),
    created_at DATE
);


INSERT INTO customers (name, email, phone_number, address, registration_date) VALUES
('Aarav Mehta', 'aarav.mehta@example.com', '9876543210', '12 MG Road, Mumbai', '2025-01-15'),
('Sneha Reddy', 'sneha.reddy@example.com', '9823456789', '45 Banjara Hills, Hyderabad', '2025-02-10'),
('Rohan Singh', 'rohan.singh@example.com', '9812345678', '78 Sector 22, Noida', '2025-03-05'),
('Priya Sharma', 'priya.sharma@example.com', '9801234567', '56 Park Street, Kolkata', '2025-01-28'),
('Kabir Nair', 'kabir.nair@example.com', '9988776655', '34 Brigade Road, Bangalore', '2025-03-18'),
('Ananya Jain', 'ananya.jain@example.com', '9877898765', '89 Gariahat, Kolkata', '2025-02-21'),
('Vikram Desai', 'vikram.desai@example.com', '9900112233', '12 Ashok Nagar, Chennai', '2025-04-02'),
('Diya Kapoor', 'diya.kapoor@example.com', '9765432109', '90 Worli Sea Face, Mumbai', '2025-04-10'),
('Aryan Khurana', 'aryan.khurana@example.com', '9123456780', '23 Rajaji Nagar, Bangalore', '2025-01-10'),
('Meera Iyer', 'meera.iyer@example.com', '9234567890', '88 T Nagar, Chennai', '2025-02-25'),
('Yash Patel', 'yash.patel@example.com', '9345678901', '77 C G Road, Ahmedabad', '2025-03-30'),
('Tanya Malhotra', 'tanya.malhotra@example.com', '9456789012', '102 Punjabi Bagh, Delhi', '2025-04-12'),
('Aditya Verma', 'aditya.verma@example.com', '9567890123', '61 Civil Lines, Kanpur', '2025-01-17'),
('Nikita Joshi', 'nikita.joshi@example.com', '9678901234', '18 Jayanagar, Bangalore', '2025-03-12'),
('Krishna Rao', 'krishna.rao@example.com', '9789012345', '27 Jubilee Hills, Hyderabad', '2025-02-08'),
('Sana Khan', 'sana.khan@example.com', '9890123456', '59 Gomti Nagar, Lucknow', '2025-04-04'),
('Devansh Sinha', 'devansh.sinha@example.com', '9901234567', '44 Paltan Bazar, Dehradun', '2025-01-25'),
('Ishita Bansal', 'ishita.bansal@example.com', '9012345678', '39 South Ex, Delhi', '2025-03-16'),
('Manav Ghosh', 'manav.ghosh@example.com', '9123456701', '68 Salt Lake, Kolkata', '2025-02-18'),
('Lavanya Krishnan', 'lavanya.krishnan@example.com', '9234567012', '72 Anna Nagar, Chennai', '2025-04-06');

INSERT INTO products (name, category, price, stock_quantity) VALUES
('Pampers Baby Dry Diapers - Medium', 'Baby Care', 699.00, 150),
('Johnson’s Baby Soap 75g', 'Baby Care', 55.00, 500),
('Chicco Baby Stroller - Red', 'Strollers', 5499.00, 30),
('Philips Avent Feeding Bottle 260ml', 'Feeding', 699.00, 200),
('Mee Mee Baby Shampoo 500ml', 'Baby Care', 299.00, 120),
('Boys Cotton T-Shirt - Blue (6-12 Months)', 'Boy\'s Fashion', 499.00, 75),
('Girls Frock - Floral Print (1-2 Years)', 'Girl\'s Fashion', 899.00, 60),
('Mothercare Baby Blanket', 'Baby Essentials', 1299.00, 45),
('Huggies Wonder Pants - Large', 'Baby Care', 799.00, 170),
('Dettol Antiseptic Liquid 250ml', 'Health & Hygiene', 95.00, 220),
('Babyhug Hooded Towel - Pink', 'Baby Essentials', 399.00, 100),
('R for Rabbit Convertible Car Seat', 'Strollers', 8999.00, 15),
('Little’s Soft Cleansing Baby Wipes - 80 pcs', 'Baby Care', 199.00, 300),
('Chicco Baby Lotion 200ml', 'Baby Care', 275.00, 140),
('Boys Jeans - Navy Blue (2-3 Years)', 'Boy\'s Fashion', 799.00, 50),
('Girls Leggings - Set of 3 (1-3 Years)', 'Girl\'s Fashion', 999.00, 40),
('Babyhug Rattle Toy Set - 5 Pieces', 'Toys', 349.00, 90),
('Mee Mee Milk Powder Dispenser', 'Feeding', 249.00, 80),
('LuvLap Sunshine Baby Carrier', 'Baby Essentials', 1699.00, 25),
('Himalaya Baby Cream 100ml', 'Baby Care', 160.00, 130);


INSERT INTO orders (customer_id, order_date, total_amount, order_status) VALUES
(1, '2025-07-01', 1454.00, 'Delivered'),
(2, '2025-07-02', 299.00, 'Shipped'),
(3, '2025-07-03', 899.00, 'Delivered'),
(4, '2025-07-04', 1600.00, 'Processing'),
(5, '2025-07-05', 275.00, 'Cancelled'),
(6, '2025-07-06', 1598.00, 'Delivered'),
(7, '2025-07-07', 199.00, 'Delivered'),
(8, '2025-07-08', 8999.00, 'Shipped'),
(9, '2025-07-09', 799.00, 'Delivered'),
(10, '2025-07-10', 1898.00, 'Returned'),
(2, '2025-07-11', 1100.00, 'Processing'),
(4, '2025-07-12', 345.00, 'Delivered'),
(6, '2025-07-13', 1498.00, 'Shipped'),
(1, '2025-07-14', 799.00, 'Delivered'),
(3, '2025-07-15', 1098.00, 'Delivered'),
(5, '2025-07-16', 245.00, 'Delivered'),
(8, '2025-07-17', 950.00, 'Processing'),
(9, '2025-07-18', 349.00, 'Shipped'),
(10, '2025-07-19', 1799.00, 'Delivered'),
(7, '2025-07-20', 160.00, 'Cancelled');

INSERT INTO order_details (order_id, product_id, quantity, subtotal_price) VALUES
(1, 3, 2, 998.00),
(1, 5, 1, 456.00),
(2, 2, 1, 299.00),
(3, 7, 1, 899.00),
(4, 1, 4, 1600.00),
(5, 6, 1, 275.00),
(6, 4, 2, 1598.00),
(7, 9, 1, 199.00),
(8, 10, 1, 8999.00),
(9, 8, 2, 799.00),
(10, 11, 2, 1898.00),
(11, 12, 1, 1100.00),
(12, 5, 1, 345.00),
(13, 3, 2, 1498.00),
(14, 7, 1, 799.00),
(15, 6, 2, 1098.00),
(16, 2, 1, 245.00),
(17, 8, 1, 950.00),
(18, 4, 1, 349.00),
(19, 13, 1, 1799.00),
(20, 9, 1, 160.00);

INSERT INTO payments (order_id, payment_method, payment_status, payment_date) VALUES
(1, 'Credit Card', 'Paid', '2025-08-01'),
(2, 'UPI', 'Paid', '2025-08-01'),
(3, 'Net Banking', 'Pending', '2025-08-02'),
(4, 'Cash on Delivery', 'Unpaid', '2025-08-02'),
(5, 'Credit Card', 'Paid', '2025-08-03'),
(6, 'UPI', 'Paid', '2025-08-03'),
(7, 'Wallet', 'Paid', '2025-08-04'),
(8, 'Net Banking', 'Paid', '2025-08-04'),
(9, 'Credit Card', 'Pending', '2025-08-05'),
(10, 'Cash on Delivery', 'Unpaid', '2025-08-05'),
(11, 'UPI', 'Paid', '2025-08-06'),
(12, 'Credit Card', 'Paid', '2025-08-06'),
(13, 'Wallet', 'Paid', '2025-08-07'),
(14, 'Net Banking', 'Pending', '2025-08-07'),
(15, 'Credit Card', 'Paid', '2025-08-08'),
(16, 'UPI', 'Paid', '2025-08-08'),
(17, 'Wallet', 'Paid', '2025-08-09'),
(18, 'Cash on Delivery', 'Unpaid', '2025-08-09'),
(19, 'Net Banking', 'Paid', '2025-08-10'),
(20, 'UPI', 'Paid', '2025-08-10');

INSERT INTO shipments (order_id, shipment_date, delivery_status) VALUES
(1, '2025-08-02', 'Delivered'),
(2, '2025-08-03', 'Delivered'),
(3, '2025-08-04', 'Shipped'),
(4, '2025-08-04', 'Processing'),
(5, '2025-08-05', 'Delivered'),
(6, '2025-08-06', 'Delivered'),
(7, '2025-08-06', 'Shipped'),
(8, '2025-08-07', 'Delivered'),
(9, '2025-08-08', 'Shipped'),
(10, '2025-08-08', 'Processing'),
(11, '2025-08-09', 'Delivered'),
(12, '2025-08-09', 'Delivered'),
(13, '2025-08-10', 'Shipped'),
(14, '2025-08-10', 'Processing'),
(15, '2025-08-11', 'Delivered'),
(16, '2025-08-11', 'Delivered'),
(17, '2025-08-12', 'Shipped'),
(18, '2025-08-12', 'Processing'),
(19, '2025-08-13', 'Delivered'),
(20, '2025-08-13', 'Delivered');


INSERT INTO coupons (code, discount_percent, valid_from, valid_to, usage_limit) VALUES
('WELCOME10', 10, '2025-01-01', '2025-12-31', 100),
('SUMMER15', 15, '2025-06-01', '2025-08-31', 50),
('FESTIVE20', 20, '2025-11-01', '2025-12-31', 200),
('VIP25', 25, '2025-01-01', '2025-12-31', 20),
('NEWYEAR30', 30, '2025-12-25', '2026-01-10', 150),
('FLASH5', 5, '2025-08-01', '2025-08-05', 500),
('BLACKFRIDAY50', 50, '2025-11-27', '2025-11-30', 1000),
('SPRING10', 10, '2025-03-01', '2025-05-31', 300),
('SAVE15', 15, '2025-01-15', '2025-12-31', 250),
('LOYAL20', 20, '2025-01-01', '2026-01-01', 100),
('FREESHIP', 0, '2025-01-01', '2025-12-31', 1000),
('WELCOME5', 5, '2025-01-01', '2025-12-31', 150),
('SUMMER30', 30, '2025-06-01', '2025-06-30', 75),
('BIGSALE40', 40, '2025-09-01', '2025-09-10', 80),
('WINTER15', 15, '2025-12-01', '2026-02-28', 90),
('FLASHSALE20', 20, '2025-07-15', '2025-07-20', 60),
('HALFOFF50', 50, '2025-10-01', '2025-10-05', 100),
('EXTRA10', 10, '2025-05-01', '2025-05-31', 120),
('SUMMERFUN25', 25, '2025-06-15', '2025-07-15', 75),
('ENDYEAR30', 30, '2025-12-15', '2025-12-31', 100);

INSERT INTO admin_users (username, password_hash, role, created_at) VALUES
('admin1', SHA2('Password123!', 256), 'superadmin', '2025-01-01'),
('admin2', SHA2('SecurePass456$', 256), 'manager', '2025-01-15'),
('admin3', SHA2('MySecret789#', 256), 'support', '2025-02-01'),
('admin4', SHA2('AdminPass321$', 256), 'editor', '2025-02-10'),
('admin5', SHA2('Password987!', 256), 'manager', '2025-03-05'),
('admin6', SHA2('Secure789$', 256), 'support', '2025-03-20'),
('admin7', SHA2('StrongPass123#', 256), 'superadmin', '2025-04-01'),
('admin8', SHA2('AdminKey456$', 256), 'editor', '2025-04-15'),
('admin9', SHA2('MyPass987!', 256), 'manager', '2025-05-01'),
('admin10', SHA2('Secret321#', 256), 'support', '2025-05-10'),
('admin11', SHA2('UserPass654$', 256), 'editor', '2025-06-01'),
('admin12', SHA2('Pass789!', 256), 'superadmin', '2025-06-15'),
('admin13', SHA2('SafePass123$', 256), 'manager', '2025-07-01'),
('admin14', SHA2('SecureKey456#', 256), 'support', '2025-07-15'),
('admin15', SHA2('AdminPass789!', 256), 'editor', '2025-08-01'),
('admin16', SHA2('StrongKey321$', 256), 'manager', '2025-08-10'),
('admin17', SHA2('UserSecret654#', 256), 'support', '2025-09-01'),
('admin18', SHA2('PassKey987!', 256), 'superadmin', '2025-09-15'),
('admin19', SHA2('SafeKey123$', 256), 'manager', '2025-10-01'),
('admin20', SHA2('SecurePass456#', 256), 'editor', '2025-10-10');

-- 1. Retrieve Customer Purchase History 

SELECT 
    c.customer_id,
    c.name AS customer_name,
    o.order_id,
    o.order_date,
    p.product_id,
    p.name AS product_name,
    od.quantity,
    od.subtotal_price,
    o.total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
ORDER BY c.customer_id, o.order_date DESC;

--  2. Identify Best-Selling Products
SELECT 
    p.product_id,
    p.name AS product_name,
    SUM(od.quantity) AS total_quantity_sold,
    SUM(od.subtotal_price) AS total_revenue
FROM products p
JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.product_id, p.name
ORDER BY total_quantity_sold DESC
LIMIT 20;

--  3. Generate Monthly Sales Report Using Window Functions 

SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m') AS sales_month,
    SUM(o.total_amount) AS total_sales,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROW_NUMBER() OVER (ORDER BY DATE_FORMAT(o.order_date, '%Y-%m')) AS month_rank,
    LAG(SUM(o.total_amount)) OVER (ORDER BY DATE_FORMAT(o.order_date, '%Y-%m')) AS previous_month_sales,
    SUM(o.total_amount) OVER (ORDER BY DATE_FORMAT(o.order_date, '%Y-%m')) AS running_total_sales
FROM orders o
GROUP BY sales_month
ORDER BY sales_month;

--  4. Customers with the Most Orders 

SELECT 
    c.customer_id,
    c.name AS customer_name,
    c.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_sp


