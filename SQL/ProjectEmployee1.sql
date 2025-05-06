# Write your MySQL query statement below

with cte as (
select project_id, sum(experience_years) _sum, count(*)  _cnt from  (
select p.project_id, e.employee_id, experience_years from Project p 
inner join Employee E on p.employee_id = e.employee_id
) t group by 1 order by 1 
)

select project_id , round((_sum / _cnt), 2) as average_years from cte