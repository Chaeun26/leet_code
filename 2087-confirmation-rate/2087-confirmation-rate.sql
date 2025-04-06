SELECT
    s.user_id,
    ROUND(AVG(CASE WHEN action='confirmed' THEN 1 ELSE 0 END),2) AS confirmation_rate
FROM
    Confirmations c
    RIGHT JOIN
        Signups s ON c.user_id=s.user_id
GROUP BY s.user_id
;