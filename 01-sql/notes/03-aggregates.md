# Aggregate Functions

Are calculations performed on multiple rows of a table - calculate a single result from a set of values.
Examples of sql aggregates:

- count() - number of rows
- sum() - sum column values
- max()/min() - return largest/smallest column value
- avg() - average column values
- round() - round column values, takes two args, column name and int indicating number of decimals to round to

Aggregate functions can be combined with `WHERE`.

```sql
-- calculate the average budget of all films
SELECT AVG(budget)
FROM films;

-- fetch the row with the highest budget
SELECT MAX(budget)
FROM films;

-- calculate the sum of the budget column
SELECT SUM(budget)
FROM films;

-- the amount grossed by the worst performing film in 1994
SELECT MIN(gross)
FROM films
WHERE release_yr = 1994

-- sum grossed for films from 2000 or later
SELECT SUM(gross)
FROM films
WHERE release_year >= 2000;

-- avg grossed for films whose title starts with 'A'
SELECT AVG(gross)
FROM films
WHERE title LIKE 'A%';

-- max grossed by a film between 200 and 2012
SELECT MAX(gross)
FROM films
WHERE release_year 
BETWEEN 2000 AND 2012;
```

**BASIC ARITHMETIC**

We can perform basic arithmetic with operators like `+`, `-`, `*`, and `/`.

NOTE:

SQL assumes that if you divide an integer by an integer, you want to get an integer back. So `SELECT (4/3);` return `1`. If you want more precision when dividing, you can add decimal places to your numbers, e.g. `SELECT (4.0/3.0)` returns `1.333`. When you're dividing make sure at leaset one of the numbers has a decimal.

```sql
-- calculate the avg gross and budget for films released in 2004
SELECT AVG(gross) as 'Avg Gross', AVG(budget) AS 'Avg Budget'
FROM films
WHERE release_year = 2004;

-- fetch title and net profit
SELECT title, (gross - budget) AS net_profit
FROM films;

-- fetch title and duration in hours
SELECT title, (duration / 60.0) AS duration_hours
FROM films;

-- get the average duration in hours
SELECT (AVG(duration)/ 60.0) AS avg_duration_hours
FROM films;

-- calculate the percentage of people who are no longer alive
SELECT COUNT(deathdate) * 100.0 / COUNT(*) AS percentage_dead
FROM people;

-- Get the number of years between the newest film and oldest film
SELECT (MAX(release_year) - MIN(release_year)) AS difference
FROM films;

-- Get the number of decades the films table covers.
SELECT (MAX(release_year) - MIN(release_year)) / 10 AS number_of_decades
FROM films;
```


**GROUP BY**

- clause that is used with aggregate function
- used to arrange identical data into groups

Note: `GROUP BY` comes after any `WHERE` statement but before any `ORDER BY` or `LIMIT`

```sql
SELECT AVG(imdb_rating)
FROM movies
WHERE year = 1999;

SELECT AVG(imdb_rating)
FROM movies
WHERE year = 2000;

SELECT AVG(imdb_rating)
FROM movies
WHERE year = 2001;
```

becomes

```sql
SELECT year, AVG(imdb_rating) AS 'avg rating'
FROM movies
GROUP BY year
ORDER BY year;
```

Example: return number of items for each price point

```sql
select price, count(*) as 'items'
from fake_apps
group by price;
```

Example: return number of items that were downloaded more than 20000 times at each price point

```sql
select price, count(*) as 'items'
from fake_apps
where downloads > 20000
group by price;
```

Example: return total number of downloads for each category

```sql
select category, sum(downloads) as 'total downloads'
from fake_apps
group by category;
```

We can `GROUP BY` a column on which a calculation has been performed, e.g

```sql
SELECT ROUND(imdb_rating), COUNT(name)
FROM movies
GROUP BY ROUND(imdb_rating)
ORDER BY ROUND(imdb_rating);
```

SQL allows columns to be referenced by the order in which they appear in the `SELECT` statement.
Thus, 'imdb_rating' would be '1' and 'name' would be '2' and so on, e.g. the above example would be

```sql
SELECT ROUND(imdb_rating), COUNT(name)
FROM movies
GROUP BY 1
ORDER BY 1;
```

**HAVING**

- used when you want to limit the results of a query based on an aggregate property
- when you want to limit the results of a query based on values of the individual row, use `WHERE`
- when you want to limit the results of a query based on aggregate property, use `HAVING`

`WHERE` clause filters ROWS, `HAVING` clause filters GROUPS.

Note: `HAVING` comes after `GROUP BY`, but before `ORDER BY` and `LIMIT`

```sql
SELECT year, genre, COUNT(name)
FROM movies
GROUP BY 1, 2
HAVING COUNT(name) > 10;
```

Example: return the avg downloads and the number of apps, at different price points, restricting the query to price points that have more than 10 apps

```sql
select price, round(avg(downloads)), count(*)
from fake_apps
group by price
having count(*) > 10;
```

**Formating Time**
SQL includes the `strftime()` method for formating datetime results.
It takes two arguments, format and the column:

`strftime('%d %m %Y, %H : %M', timestamp)`

If the timestamp format is YYYY-MM-DD HH:MM:SS

- %Y returns the year (YYYY)
- %m returns the month (01-12)
- %d returns the day of the month (1-31)
- %H returns 24-hour clock (00-23)
- %M returns the minute (00-59)
- %S returns the seconds (00-59)
