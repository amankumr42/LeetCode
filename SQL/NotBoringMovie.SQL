# Write your MySQL query statement below
WITH cte  AS (
select *, 
case 
    when id % 2 = 0 then 'even'
    else 'odd' end as odd_or_even  
from Cinema
)


select id, movie, description, rating  
 from cte where odd_or_even = 'odd' and description != 'boring'
 order by rating desc
