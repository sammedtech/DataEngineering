
CREATE TABLE customers(id int PRIMARY KEY, 
					   name varchar(50), 
					   address varchar(100), 
					   city varchar(50));

INSERT INTO customers values(1, 'Prajakta', 'Sambhaji Nagar', 'Sambhaji Nagar'),
							(2, 'Vaibhav', 'Cidco', 'Pune'),
							(3, 'Vishwajeet', 'Shivaji Nagar', 'Pune'),
							(4, 'Akash', 'Kharadi', 'Mumbai');
							
CREATE TABLE orders(oid int PRIMARY KEY, 
					cust_id int, 
					product_name varchar(50), 
					ord_amount decimal(7,2),
					);

ALTER TABLE orders 
ADD CONSTRAINT fk_custId 
FOREIGN KEY (cust_id) 
REFERENCES customers (id); -- Query to add cust_id column as "foreign key" to "id" column of customers table

INSERT INTO orders values(1, 1, 'Refridgerator', 27000),
						(2, 4, 'Ceiling Fan', 4300),
						(3, 4, 'Mixer', 5200),
						(4, 2, 'TV', 63000);
						
INSERT INTO orders values(5, 1, 'Washing Machine', 21000),
						(6, 4, 'AC', 24000),
						(7, 4, 'Mixer', 3200);						


SELECT * FROM orders; -- This query wil show you all the columns (attributes/fields) and all the rows (data/records)
SELECT * FROM customers;

SELECT * FROM orders JOIN customers ON (orders.cust_id = customers.id); -- INNER JOIN

SELECT name, product_name, ord_amount, address, city 
FROM orders INNER JOIN customers ON (cust_id = id)
WHERE cust_id = 4; --> INNER JOIN : USED TO FETCH MATCHING RECORDS BETWEEN TABLES

-- LEFT JOIN
-- RIGHT JOIN
-- CROSS JOIN
-- SELF JOIN
-- FULL JOIN

SELECT * FROM customers LEFT JOIN orders ON (cust_id=id); 
--> LEFT JOIN : USED TO SHOW ALL THE DATA FROM LEFT TABLE 
-- AND NULL RECORDS FOR RIGHT TABLE WHERE JOIN CONDITION IS NOT MATCHING

SELECT * FROM customers RIGHT JOIN orders ON (cust_id=id);

SELECT * FROM customers FULL JOIN orders ON (cust_id=id);




CREATE TABLE A(aid int);

INSERT INTO A values(1),(2),(3),(1), (4);

CREATE TABLE B(bid int);

INSERT INTO B values(1),(4),(1),(5),(6),(1);

SELECT * FROM A INNER JOIN B ON (aid=bid); --> MATCHING RECORDS FROM BOTH THE TABLES
SELECT * FROM A LEFT OUTER JOIN B ON (aid=bid); --> ALL RECORDS FROM LEFT TABLE 
										  --> AND MATCHING RECORDS FROM RIGHT TABLE
SELECT * FROM A RIGHT OUTER JOIN B ON (aid=bid); --> ALL RECORDS FROM RIGHT TABLE 
										  --> AND MATCHING RECORDS FROM LEFT TABLE
SELECT * FROM A FULL JOIN B ON (aid=bid); --> FULL RECORDS FROM BOTH TABLES
SELECT * FROM A CROSS JOIN B;


SELECT * FROM orders ORDER BY cust_id;

-- 1 Roy 48000
-- 2 Joy 63000
-- 4 Poppeye 36700

SELECT cust_id, name, SUM(ord_amount) FROM orders
INNER JOIN customers ON (cust_id=id)
GROUP BY cust_id, name
HAVING SUM(ord_amount) > 50000;

select * from orders where oid IN (1,2,5,6);


-- AGGREGATE FUNCTIONS : 
-- MIN()
-- MAX()
-- SUM()
-- COUNT()



-- SUB-QUERY --> Query within Query
-- 		  --> SELECT Query in Where Condition


-- Query the two cities in STATION with the shortest and longest CITY names, 
-- as well as their respective lengths (i.e.: number of characters in the name). 
-- If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

SELECT city, length(city) as city_length from station
WHERE length(city) = (select max(length(city)) from station)
OR  length(city) IN (select min(length(city)) from station)
order by city_length DESC, city
LIMIT 2;
