# Write your MySQL query statement below

select t.name as name  from (
    select e.id, e.name , count(*) as _cnt from 
    Employee e inner join Employee b on e.id = b.managerId 
    group by 1,2 ) 
t where _cnt >= 5
