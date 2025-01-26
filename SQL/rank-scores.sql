# Write your MySQL query statement below
select score , rnk as 'rank' from (select score,  dense_rank() 
OVER ( ORDER BY score desc ) as rnk
from scores ) t ; 