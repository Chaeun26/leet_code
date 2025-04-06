WITH boarded AS(
    SELECT
        person_name,
        turn,
        SUM(weight) OVER (ORDER BY turn) AS cum_weight
    FROM Queue
)

SELECT person_name
FROM boarded
WHERE cum_weight<=1000
ORDER BY turn DESC
LIMIT 1;