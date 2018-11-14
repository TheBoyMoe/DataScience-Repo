# SQL Queries

- queries are used to retrieve information - a result set
- use the `select` clause

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
