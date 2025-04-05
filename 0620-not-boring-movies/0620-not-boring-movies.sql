# Write your MySQL query statement below
SELECT *
From Cinema
WHERE NOT description='boring' AND id%2=1
ORDER BY rating DESC;