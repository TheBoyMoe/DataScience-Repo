# Aggregates

Are calculations performed on multiple rows of a table.
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
