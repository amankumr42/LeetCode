# Write your MySQL query statement below
select employee_id, department_id  from 
(
    select * , row_number() over (partition by employee_id order by primary_flag_num asc ) 
    as rw_num 
    from (select * , 
    case when primary_flag = 'Y' then 0
    else 1 end as primary_flag_num 
from  Employee
) t 
) abc where rw_num = 1