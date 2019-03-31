# SQL Queries


## Basic SQL Queries

- queries are used to retrieve information - a result set
- use the `SELECT` clause

**AS**

- keyword that allows you to rename a column using an alias
- the alias can be any thing, as long as it appears in single quotes.
- it ONLY appears in the result set - the actual column is NOT renamed.

```sql
SELECT column_name AS 'alias_name'
FROM table_name

SELECT name as 'Title', imdb_rating as 'IMDB'
FROM films
WHERE release_year BETWEEN 2000 AND 2005;
```

**DISTINCT**

- filter out duplicate values - returning only unique values.

```sql
SELECT DISTINCT column_name
FROM table_name

SELECT DISTINCT tools
FROM inventory;
```

**COUNT**

- return the number of rows in one or more columns that match the query.

```sql
-- returns the number of rows in the table
SELECT COUNT(*)
FROM table_name
```

Count the number of fields in a column where a value is present, i.e, are not NULL.

```sql
-- count number of birthdates, NOT NULL (number of rows that DO NOT have a NULL bithdate field)
SELECT COUNT(birthdates)
FROM people;
```

We can also combine `COUNT` with `DISTINCT` to count the number of unique values in a column.

```sql
-- count the number of unique values in 'country' column
SELECT COUNT(DISTINCT country)
FROM films;
```

## Filtering Results

SQL provides a number of keywords that support filtering queries based on both text and numeric values in a table, such as `WHERE`, `LIKE`, `BETWEEN`, `AND` , `OR`, etc, which can be used individually or in combination. There are a number of comparison operatrs that are also available: `=` (equal), `<>` (not equal), `>`, `<`, `>=`, and `<=`.\


**WHERE**

- use the `WHERE` clause to restrict(filter) the results returned
- filters the result set to only include the rows where the condition is true
- comparison operators used with `WHERE` - >, <, >=, <=, =, <> (you can use !=, but it's not part of the SQL std)
- NOTE: the `WHERE` clause ALWAYS comes after `FROM`.


Filtering numeric values:

```sql

-- return all films with an 'IMDB' rating > 8
SELECT imdb_rating AS 'IMDB'
FROM movies
WHERE imdb_rating > 8;

-- return all films (title and year) released after 2014
SELECT name AS 'Title', year
FROM movies
WHERE year > 2014;

-- return all films released in 2015
SELECT *
FROM films
WHERE year = 2016;

-- return the number of films released prior to 2000
SELECT COUNT(*)
FROM films
WHERE year < 2000;

-- return the title and release yr for films released after 2000
SELECT title, year
FROM films
WHERE year > 2000;

-- return all films with a budget greater than 100 million
SELECT *
FROM films
WHERE budget > 100000000;
```

Filtering of text:

NOTE: with PostgreSQL, you must use single quotes with `WHERE`.

```sql
-- return all films with the title 'Metropolis
SELECT title
FROM films
WHERE title = 'Metropolis';

-- select all French language films
SELECT *
FROM films
WHERE language = 'French';

-- count the number of French language films
SELECT COUNT(*)
FROM films
WHERE language = 'French';

-- return the name and birthdate of the person born on Nov 11th, 1974 (use ISO format)
SELECT name, birthdate
FROM people
WHERE birthdate = '1974-11-11';
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

**AND**

- operator used in combination with `WHERE` clause to combine multiple conditions.
- displays the row if ALL conditions are met (True).
- you need to specify the column name separately for every `AND` condition.
- you can use as many `AND` conditions as req'd.

Thus the following is valid:

```sql
SELECT title, year
FROM films
WHERE year > 1994
AND year < 2000;
```

But the following IS NOT:

```sql
SELECT title, year
FROM films
WHERE year > 1994 AND < 2000;
```

```sql
--- fetch the title and year for Spanish langauge films prior to 2000
SELECT title, release_year
FROM films
WHERE language = 'Spanish'
AND release_year < 2000;

-- fetch all details for Spanish language films released after 2000
SELECT *
FROM films
WHERE language = 'Spanish'
AND release_year > 2000;

-- fetch all details for Spanish language films released after 2000, but before 2010
SELECT *
FROM films
WHERE language = 'Spanish'
AND release_year > 2000
AND release_year < 2010;

SELECT *
FROM films
WHERE release_year < 1985
AND genre = 'horror'
AND imdb_rating > 7;
```


**OR**

SQL provides the `OR` operator to select rows based on multiple conditions where some but not all need to be met.

- used in combination with the `WHERE` clause to combine multiple conditions
- returns a row if ANY of the conditions are met (at leaset one of the condittions need to be met)
- as with `AND`, you need to specify the column for every `OR` condition.

This is valid:

```sql
SELECT *
FROM films
WHERE release_year = 2014
OR release_year = 2016;
```

But this is NOT:

```sql
SELECT *
FROM films
WHERE release_year = 2014 OR 2016;
```

Wwhen combining `AND` and `OR`, make sure to enclose the indiidual clauses in parantheses:

```sql
SELECT title
FROM films
WHERE (release_year = 1994 OR release_year = 1995)
AND (certification = 'PG' OR certification = 'R')
```

```sql
SELECT *
FROM films
WHERE genre = 'romance'
OR genre = 'comedy';

SELECT *
FROM films
WHERE release_year > 2014
AND (genre = 'action' OR genre = 'comedy');

-- fetch the title and release yr for 90's French or Spanish language films and grossed more than 2 million
SELECT title, release_year
FROM films
WHERE release_year >= 1990
AND release_year < 2000
AND (language = 'French' OR language = 'Spanish')
AND gross > 2000000;
```

**BETWEEN**

- used in conjunction with the `WHERE` clause to filter the result set within a certain RANGE.
- can be used to **filter numbers, strings(text) or dates**.
- it is case sensitive
- can be used with multiple `AND` and/or `OR` operators
- BETWEEN two letters is not inclusive of the 2nd letter(upto but not including)
- BETWEEN two numbers is inclusive of the 2nd number, up to and including


```sql
-- all the movies released in the 1970's
SELECT *
FROM films
WHERE release_year 
BETWEEN '1970' and '1979';

-- fetch all details on 90's 'Action' films 
SELECT *
FROM films
WHERE release_year 
BETWEEN 1990 AND 1999 -- 1st condition (range >= 1990 and <= 1999)
AND genre = 'action';  -- 2nd condition

-- fetch all details on 90's 'Action' films with a rating > 6.5
SELECT *
FROM films
WHERE release_year 
BETWEEN 1990 and 1999
AND genre = 'action'
AND imdb_rating > 6.5;

-- return movies starting with 'A', upto 'I' (upto but not including 'J')
SELECT *
FROM films
WHERE title 
BETWEEN 'A' AND 'J';

-- fetch the names of all British nationals between 20 and 40 yrs of age
SELECT name
FROM people
WHERE age
BETWEEN 20 and 40 -- inclusive
AND nationality = 'British';

-- fetch title and release yr of Spanish/French films released 
-- between 1990 and 2000(inclusive) with a budget > 100 million
SELECT title, release_year
FROM films
WHERE release_year
BETWEEN 1990 AND 2000
AND budget > 100000000
AND language = 'Spanish';
```

**IN**

The `IN` operator allows you to specify multiple values in a `WHERE` clause, making it easier and quicker to specify multiple `OR` conditions - resulting in simpler to read code, e.g. we can replace the following :

```sql
SELECT title
FROM films
WHERE release_year = 1970
OR release_year = 1974
OR release_year = 1976
OR release_year = 1978;
```

With the following:

```sql
SELECT title
FROM films
WHERE release_year IN (1970, 1974, 1976, 1978);
```

```sql
-- fetch title and release yr of all films from 1990 or 2000 that were longer than 2hrs
SELECT title, release_year
FROM films
WHERE release_year IN (1990, 2000)
AND duration > 120;

-- fetch the title and language of all English, French and Spanish language films
SELECT title, language
FROM films
WHERE language IN ('English', 'Spanish', 'French');


```

**NULL, IS NULL and IS NOT NULL**

`NULL` represents a missing or unknown value. We can check for NULL values using `IS NULL`.

- combine `IS NULL` with `WHERE` to identify missing values within your dataset
- use `IS NOT NULL` to return those results that are NOT null

```sql
-- count the number of people whose birthdate is missing:
SELECT COUNT(*)
FROM people
WHERE birthdate IS NULL;

-- count the number of people whose birthdate is NOT missing
SELECT COUNT(*)
FROM people
WHERE birthdate IS NOT NULL;

-- fetch the title of every film that does not have a budget
SELECT title
FROM films
WHERE budget IS NULL;

-- count the number of films that do not have an associated language
SELECT COUNT(*)
FROM films
WHERE language IS NULL;
```

**LIKE and NOT LIKE**

Using the `WHERE` statement when can filter text by specifying the exact text we're interested in.
The `LIKE` operator supports searching for text based on a pattern using wildcards `_` and `%` as a placeholder for some other value.

- `%` will match zero, one or more characters in text

```sql
-- will match film titles, 'The Last Samurai, The Last Stand, The Last of the Mohicans, etc
SELECT title
FROM films
WHERE title LIKE 'The LAS%';
```

- `_` will match for a single character.

```sql
-- match for DataCamp and DataComp
SELECT name
FROM companies
WHERE name LIKE 'DataC_mp';
```

You can also use `NOT LIKE` operator to find records that don't match the pattern you specify.

```sql
-- fetch the names of all people that begins with 'B'
SELECT name
FROM people
WHERE name LIKE 'B%';

-- fetch the names of all people whose names have 'r' as the 2nd letter
SELECT name
FROM people
WHERE name LIKE '_r%';

-- fetch the names of people whose names do not start with 'A'
SELECT name
FROM people
WHERE name NOT LIKE 'A%';
```


**ORDER BY**

- sort the returned result set either alphabetically or numerically
- `DESC` -> 'Z-A', '9-0' (high-low), `ASC` -> 'A-Z', '0-9' (low-high)

Note:

- `ORDER BY` ALWAYS appears after `WHERE`, when `WHERE` is used
- the column that you `ORDER BY` does not have to be one of the columns being displayed

```sql
SELECT name, imdb_rating as 'IMDb'
FROM films
WHERE imdb_rating > 8.0
ORDER BY release_year DESC;
```

**LIMIT**

- clause that caps the number of records returned(max number returned) - limits size of the data set returned
- ALWAYS appears at the end of a query
- not all SQL database implementations supports it.

```sql
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 3;
```

**CASE**

- used to handle `IF..THEN` logic

```sql
SELECT name,
CASE
    WHEN imdb_rating > 8 THEN 'Fantastic'
    WHEN imdb_rating > 6 THEN 'Poorly Received'
    ELSE 'Avoid at All Costs'
END AS 'Review'
FROM movies;
```

The above code block allows you to 'condense' the ratings to create a second column, 'Review':

- Each `WHEN` tests a condition and the following THEN gives us the string if the condition is true
- The `ELSE` gives us the string if all the above conditions are false.
- The `CASE` statement must end with `END`

```sql
SELECT name,
CASE
    WHEN genre = 'romance' THEN 'Chill'
    WHEN genre = 'comedy' THEN 'Chill'
    ELSE 'Intense'
END AS 'Mood'
FROM movies;
```

**Summary**

`SELECT` is the clause we use every time we want to query information from a database.
`AS` renames a column or table.
`DISTINCT` return unique values.
`WHERE` filter results of the query based on conditions that you specify.
`LIKE` return similar records, search for patterns.
`BETWEEN` return results that are within a specific range.
`AND` and `OR` combines multiple conditions.
`IN` alternative to using multiple `OR` operators
`IS NULL` and `IS NOT NULL` - identify missing values within the data.
`ORDER BY` sorts the result.
`LIMIT` specifies the maximum number of rows that the query will return.
`CASE` creates different outputs.
