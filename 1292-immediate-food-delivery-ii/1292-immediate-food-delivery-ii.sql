-- see first order of each customer
-- order_date=customer_pref_delivery_date ... count ... calculate percentage
select round(count(*)*100/(select count(distinct customer_id) from delivery),2) as immediate_percentage
from delivery
where order_date=customer_pref_delivery_date
    and (customer_id, order_date) in(
    select customer_id, min(order_date)
    from Delivery
    group by customer_id
)


