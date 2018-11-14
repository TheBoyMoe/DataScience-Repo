# SQL Queries

- queries are used to retrieve information - a result set
- use the `SELECT` clause

**AS keyword**

```sql
SELECT column_name AS 'alias_name'
FROM table_name
```

`AS` keyword that allows you to rename a column using an alias

NOTE:

- can be any thing, as long as it is in single quotes.
- the alias ONLY appears in the result set - the actual column is NOT renamed.

```sql
select name as 'title', imdb_rating as 'IMDB'
from movies;
```

**Distinct**

- filter out duplicate values - returning only unique values.

```sql
SELECT DISTINCT column_name
FROM table_name

SELECT DISTINCT tools
FROM inventory;
```

**Where**

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

**Like**

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
