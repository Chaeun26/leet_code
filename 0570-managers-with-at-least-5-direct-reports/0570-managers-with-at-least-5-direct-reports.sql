
SELECT name
FROM Employee
WHERE 
    id IN(
        SELECT DISTINCT managerId
        FROM Employee
        GROUP BY managerId
        HAVING COUNT(*) >= 5
    )
