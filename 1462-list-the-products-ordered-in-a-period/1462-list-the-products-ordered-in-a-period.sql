# Write your MySQL query statement below
SELECT 
    (SELECT product_name FROM Products WHERE Orders.product_id=Products.product_id) AS product_name,
    SUM(unit) as unit
FROM Orders
WHERE order_date >= '2020-02-01' AND order_date < '2020-03-01'
GROUP BY product_id
HAVING SUM(unit) >= 100