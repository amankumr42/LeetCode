# Write your MySQL query statement below
select teacher_id , count(distinct(subject_id)) as cnt from
    Teacher group by 1 order by 1 desc