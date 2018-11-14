create table friends (
	id integer primary key,
  name text,
  birthday date
);

insert into friends
values(1, 'Jane Doe', '1990/05/30');

insert into friends
values(2, 'Tom Smith', '1908/12/01');

insert into friends
values(3, 'John Smith', '1976/09/23');

select * from friends;

update friends
set name = 'Jane Smith'
where id = 1;

alter table friends
add column email text;

update friends
set email = 'jane@codeacademy.com'
where id = 1;

update friends
set email = 'tom@codeacademy.com'
where id = 2;

update friends
set email = 'john@codeacademy.com'
where id = 3;

delete from friends
where id = 1;

select * from friends;