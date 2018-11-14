select distinct neighborhood
from nomnom;

select distinct cuisine
from nomnom;

select *
from nomnom
where cuisine = 'Chinese';

select *
from nomnom
where review >= 4;

select *
from nomnom
where cuisine = 'Italian'
and price = '$$$';

select *
from nomnom
where name like '%meatball%';

select *
from nomnom
where neighborhood = 'Midtown'
or neighborhood = 'Downtown'
or neighborhood = 'Chinatown'
order by name;

select *
from nomnom
where health is null
order by name;

select *
from nomnom
order by review desc
limit 10;

select name,
case
	when review > 4.5 then 'Extraordinary'
  when review > 4 then 'Excellent'
  when review > 3 then 'Good'
  when review > 2 then 'Fair'
  else 'Poor'
end as 'The View'
from nomnom
order by name;

select *
from transaction_data
limit 10;

select full_name, email
from transaction_data
where zip = '20252';

select full_name , email
from transaction_data
where full_name = 'Art Vandelay'
or full_name like '% der %';

select email, ip_address
from transaction_data
where ip_address like '10%'
order by email;

select *
from transaction_data
where email like '%temp_email.com'
order by full_name;

select *
from transaction_data
where ip_address like '120.%'
and full_name like 'John%';

select *
from users
limit 20;

select email, birthday
from users
where birthday between '1980-01-01' and '1989-12-31'
order by birthday asc;

select email, created_at
from users
where created_at < '2017-05-01'
order by created_at desc;

select email, test
from users
where test = 'bears'
order by email;

select email, campaign
from users
where campaign like 'BBB%'
order by email;

select email, campaign
from users
where campaign = 'AAA-2'
order by email;

select email, campaign, test
from users
where campaign is not null
and test is not null
order by email;