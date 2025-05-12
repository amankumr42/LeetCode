# Write your MySQL query statement below
with cte as (
select  
    delivery_id
    ,customer_id
    ,order_date
    ,customer_pref_delivery_date 
    from 
        ( 
            select 
            * , 
            row_number() over (
            partition by customer_id order by order_date asc
        ) as rw from 
        Delivery 
    ) t where rw = 1
)
select 
    round((count(case when order_date = customer_pref_delivery_date then 1 
    end) / count(*) * 100 ), 2) as immediate_percentage
from cte 