# Write your MySQL query statement below
select a.id from Weather a , weather b 
WHERE DATEDIFF(a.recordDate, b.recordDate) = 1
  AND a.temperature > b.temperature;
