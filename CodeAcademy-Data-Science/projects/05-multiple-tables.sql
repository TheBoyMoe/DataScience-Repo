  select * from trips;
select * from riders;
select * from riders2;
select * from cars;

--select *
--from riders
--cross join cars;

--select trips.date, trips.pickup, trips.dropoff, trips.cost, riders.first, riders.last, riders.username
--from trips
--left join riders
--on trips.rider_id = riders.id;

--select trips.date, trips.pickup, trips.dropoff, trips.cost, trips.type, cars.model, cars.OS
--from trips
--join cars
--on trips.car_id = cars.id;

--select *
--from riders
--union
--select *
--from riders2;

--select round(avg(cost),2) as 'avg cost'
--from trips;

--with all_riders as (
--   select *
--  from riders
--  union
--  select *
--  from riders2
--)
--select first, last, total_trips
--from all_riders
--where total_trips < 500
--order by 3 desc;

select count(status) as 'active'
from cars
where status = 'active';

select *
from cars
order by trips_completed desc
limit 2;