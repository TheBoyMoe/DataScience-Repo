
select department, count(*) as 'total'
from met
group by department;

select count(*) as 'count'
from met
where category like '%celery%';

select title, medium, min(date) as 'date'
from met;

select title, medium, date
from met
where date like '%1600%';

select country, count(*) as count
from met
where country is not null
group by 1
order by 2 desc
 limit 10;
 
 select category
, count
(*) as 'count'
 from met
 group by 1
 having count
(*) > 100
 order by 2 desc;

select medium, count(*) as 'count'
from met
where medium like '%gold%'
  or medium like '%silver%'
group by 1
order by 2 desc;

SELECT CASE
   WHEN medium LIKE '%gold%'   THEN 'Gold'
   WHEN medium LIKE '%silver%' THEN 'Silver'
   ELSE NULL
  END AS 'Bling',
  COUNT(*)
FROM met
WHERE Bling IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;