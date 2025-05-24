# Write your MySQL query statement below

select employee_id, name, count(name) as reports_count  , round(avg(age),0) as average_age from 
(select a.employee_id, a.name, b.reports_to, b.age 
 from Employees a inner join Employees b 
on a.employee_id = b.reports_to ) t 
group by 1 ,2  order by 1 asc 