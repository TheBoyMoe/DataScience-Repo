# SQL Queries

- queries are used to retrieve information - a result set
- use the `SELECT` clause

**AS**

- keyword that allows you to rename a column using an alias

```sql
SELECT column_name AS 'alias_name'
FROM table_name
```

NOTE:

- the alias can be any thing, as long as it appears in single quotes.
- it ONLY appears in the result set - the actual column is NOT renamed.

```sql
select name as 'title', imdb_rating as 'IMDB'
from movies;
```

**DISTINCT**

- filter out duplicate values - returning only unique values.

```sql
SELECT DISTINCT column_name
FROM table_name

SELECT DISTINCT tools
FROM inventory;
```

**WHERE**

- use the `WHERE` clause to restrict the results returned
- filters the result set to only include the rows where the condition is true
- comparison operators used with `WHERE` - >, <, >=, <=, =, !=

```sql
SELECT imdb_rating AS 'IMDB'
FROM movies
WHERE imdb_rating > 8;

select name AS 'Title', year
from movies
where year > 2014;
```

**LIKE**

- used to compare similar values
- used in conjunction with WHERE clause to search for a specific pattern
- '\_' is a wildcard character that can be used to substitute any individual character

Example: 2 movie titles, 'Seven' and 'Se7en'

- select all the movie titles that start with 'Se' and end in 'en'

```sql
SELECT *
FROM movies
WHERE name LIKE 'Se_en';
```

- '%' another wildcard character, matches 0 or more characters, e.g. find all movies that start with 'Se'

```sql
SELECT *
FROM movies
WHERE name LIKE 'Se%';
```

- searches are case insensitive, 'A%' is the same as 'a%'
- '%a' searches for movies that end with 'a'
- '%man%' search for movies that contain 'man' - can start/end or appear in the middle.
- search for moovies that start with the word 'The'

```sql
SELECT *
FROM movies
WHERE name LIKE 'The %';
```

**IS NULL**

- unknown or missing values are indicated with NULL
- you CAN NOT test for NULL with comparison operators such as '=' or '!='
- instead use `IS NULL` and `IS NOT NULL`

Example: filter all movies with no IMDb rating:

```sql
SELECT name, imdb_rating as 'IMDb'
FROM movies
WHERE imdb_rating IS NULL;
```

**BETWEEN**

- used in conjunction with the `WHERE` clause to filter the result set within a certain RANGE.
- can be used to filter numbers, strings(text) or dates
- BETWEEN two letters is not inclusive of the 2nd letter(upto but not including)
- BETWEEN is case sensitive

Example: return movies starting with 'A', upto 'I'.

```sql
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';
```

- BETWEEN two numbers is inclusive of the 2nd number, up to and including

Example: return movies from 1990 upto and including 1999

```sql
SELECT *
FROM movies
WHERE year BETWEEN 1990 AND 1999;
```

Example: all the movies released in the 1970's

```sql
select *
from movies
where year between '1970' and '1979';
```

**AND**

- operator used in combination with the `WHERE` clause to combine multiple conditions
- displays the row if ALL conditions are met

```sql
SELECT *
FROM movies
WHERE year BETWEEN 1990 AND 1999 -- 1st condition
AND genre = 'action';  -- 2nd condition
```

```sql
select *
from movies
where year between 1990 and 1999
and genre = 'action'
and imdb_rating > 6.5;
```

```sql
select *
from movies
where year < 1985
and genre = 'horror'
and imdb_rating > 7;
```

**OR**

- used in combination with the `WHERE` clause to combin multiple conditions
- returns a row if ANY of the conditions are met

```sql
SELECT *
FROM movies
WHERE year > 2014
OR genre = 'action';
```

```sql
select *
from movies
where genre = 'romance'
or genre = 'comedy';
```

```sql
select *
from movies
where year > 2014
and genre = 'action'
or year > 2014
and genre = 'comedy';
```

**ORDER BY**

- sort the returned result set either alphabetically or numerically
- `DESC` -> 'Z-A', '9-0', `ASC` -> 'A-Z', '0-9'

Note:

- `ORDER BY` ALWAYS appears after `WHERE`, whe `WHERE` is used
- the column that you `ORDER BY` does not have to be one of the columns being displayed

```sql
select name, imdb_rating as 'IMDb'
from movies
where imdb_rating > 8.0
order by year desc;
```
