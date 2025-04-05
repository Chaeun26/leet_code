# Write your MySQL query statement below

SELECT reports_to AS employee_id, 
    (
        SELECT name FROM Employees e2 WHERE e1.reports_to=e2.employee_id
    ) AS name,
    COUNT(reports_to) AS reports_count,
    ROUND(AVG(age)) AS average_age
FROM Employees e1
GROUP BY reports_to
HAVING reports_count > 0
ORDER BY employee_id
