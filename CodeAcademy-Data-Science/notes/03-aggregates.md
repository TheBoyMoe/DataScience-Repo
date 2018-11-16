# Aggregate Functions

Are calculations performed on multiple rows of a table - calculate a single result from a set of values.
Examples of sql aggregates:

- count() - number of rows
- sum() - sum column values
- max()/min() - return largest/smallest column value
- avg() - average column values
- round() - round column values, takes two args, column name and int indicating number of decimals to round to

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
