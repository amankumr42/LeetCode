# Write your MySQL query statement below

select max(salary) as SecondHighestSalary from (SELECT id, salary , RANK() 
OVER ( ORDER BY id) as rnk 
FROM Employee ) t where rnk = 2;
