# Write your MySQL query statement below

select sales.product_id, first_year, quantity, price
from sales
join (
    select product_id, min(year) as first_year
    from sales
    group by product_id
) earlist on sales.product_id=earlist.product_id and year=first_year
;