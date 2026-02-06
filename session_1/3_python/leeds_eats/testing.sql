-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 food_delivery.db
-- 2. Load this script: .read testing.sql
-- 3. Exit SQLite: .exit


-- You can use this to test your sql before you write it into your program.

-- ## Section 1 - Summaries

-- 1. Display the total number of customers.
SELECT COUNT(customer_id) FROM customers;

-- 2. Show the earliest and latest customer signup dates.
SELECT signup_date FROM customers ORDER BY signup_date ASC LIMIT 1;
SELECT signup_date FROM customers ORDER BY signup_date DESC LIMIT 1;

-- 3. Display:
-- - total number of orders
-- - average order value
-- - highest and lowest order totals
SELECT COUNT(order_id), AVG(order_total), MAX(order_total), MIN(order_total) FROM orders;

-- 4. Display the total number of drivers and their hire dates.
SELECT COUNT(*) FROM drivers;
SELECT DISTINCT(hire_date) FROM drivers;

-- ## Section 2 - Key Statistics

-- 5. Orders per customer
-- - Customer name
-- - Number of orders
-- - Total amount spent
SELECT C.customer_name, COUNT(O.order_Id), SUM(O.order_total)
FROM customers C LEFT JOIN orders O
ON C.customer_id = O.customer_id
GROUP BY C.customer_id;

-- 6. Driver workload
-- - Driver name
-- - Number of deliveries completed
SELECT DR.driver_name, COUNT(DL.delivery_id)
FROM drivers DR LEFT JOIN deliveries DL
ON DR.driver_id = DL.driver_id
GROUP BY DR.driver_id;

-- 7. Order delivery Lookup - search for a individual order
-- - search for an order by ID
-- - customer name
-- - order total
-- - delivery date
-- - driver
SELECT C.customer_name, O.order_total, DL.delivery_date, DR.driver_name
FROM orders O
JOIN customers C ON O.customer_id = C.customer_id
JOIN deliveries DL ON O.order_id = DL.order_id
JOIN drivers DR ON DL.driver_id = DR.driver_id
WHERE O.order_id = ?;


-- ## Section 3 - Time-based Summaries

-- 8. Count the number of orders per order date.
SELECT O.order_date, COUNT(O.order_id) FROM orders O
GROUP BY O.order_date;

-- 9. Count the number of deliveries per delivery date.
SELECT DL.delivery_date, COUNT(DL.delivery_id)
FROM deliveries DL GROUP BY DL.delivery_date;

-- 10. Count customer signups per month - you may need to do some python processing on this one!

-- ## Section 4 - Performance and Rankings

-- 11. List the top 5 customers by total spend.
SELECT C.customer_name, SUM(O.order_total)
FROM customers C
LEFT JOIN orders O ON C.customer_id = O.customer_id
GROUP BY C.customer_id
ORDER BY SUM(O.order_total) DESC LIMIT 5;

-- 12. Rank drivers by number of deliveries completed.
SELECT DR.driver_name, COUNT(DL.delivery_id)
FROM drivers DR
LEFT JOIN deliveries DL ON DR.driver_id = DL.driver_id
GROUP BY DR.driver_id
ORDER BY COUNT(DL.delivery_id) DESC;

-- 13. Display all orders above a value which should be inputted by the user (e.g. £100)
SELECT * FROM orders WHERE order_total > ?;