select *
from startups;

select count(*) as 'number of companies', sum(valuation) as 'valuation'
from startups;

select max(raised) as 'max raised'
from startups
where stage = 'Seed';

select min(founded) as 'year'
from startups;

select round(avg(valuation), 0) as 'average valuation'
from startups;

select category, round(avg(valuation), 2) as 'average valuation'
from startups
where category is not null
  and valuation is not null
group by 1
order by 2 desc;

select category, count(category) as 'total'
from startups
where category is not null
group by 1
having count(category) > 3
order by 2 desc;

select location, round(avg(employees), 0) as 'avg employees'
from startups
group by location
order by 2 desc;

select location, round(avg(employees), 0) as 'avg employees'
from startups
group by location
having avg(employees) > 500
order by 2 desc;
