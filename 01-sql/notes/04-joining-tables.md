# Handling Multiple Tables in SQl

**JOIN/INNER JOIN**

We use `JOIN`s to combine 2 tables in sql.
The combined table only includes rows(with all the values from both tables) that match the `ON` condition, i.e. where the two fields being compared are equal the **INERSECTION**.

```sql
SELECT *
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

Note:

- the order of the tables, e.g. left and right, does not matter.
- the `customer_id` column appears twice in the resulting table when `SELECT *` is used.
- because column names are often repeated across multiple tables, use the syntax table_name.column_name to be sure that our requests for columns are unambiguous. Here, we use it in the ON statement, but we can also use it in the SELECT or any other statement where we refer to column names.

```sql
SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;

select *
from orders
join subscriptions
on orders.subscription_id = subscriptions.subscription_id
where description = 'Fashion Magazine';

-- select countries that have both prime minister and president
SELECT p1.country, p1.continent, prime_minister, president -- columns from both tables to display
FROM prime_ministers AS p1 -- table on left
INNER JOIN presidents AS p2 -- table on right
ON p1.country = p2.country; -- specify keys you want to match on

SELECT cities.name AS city, countries.name AS country, countries.region
FROM cities
INNER JOIN countries
ON cities.country_code = countries.code;
```

Instead of writing the full table name, you can use table aliasing. Use `AS` to add the alias immediately after the table name with a space. The aliased table names can then be used with the `SELECT` and `ON` statements.

```sql
SELECT c1.name AS city, c2.name AS country
FROM cities AS c1
INNER JOIN countries AS c2
ON c1.country_code = c2.code;

SELECT c.code AS country_code, name, year, inflation_rate
FROM countries AS c
INNER JOIN economies AS e
ON c.code = e.code;
```

SQL supports the ability to combine multiple joins in a single query.

```sql
SELECT *
FROM left_table
  INNER JOIN right_table
    ON left_table.id = right_table.id
  INNER JOIN another_table
    ON left_table.id = another_table.id;

SELECT c.code, name, region, e.year, fertility_rate, unemployment_rate
  FROM countries AS c
  INNER JOIN populations AS p
    ON c.code = p.country_code
  INNER JOIN economies AS e
    ON c.code = e.code
    AND e.year = p.year;
```

When the column name that your joining the left and right tables are the same, e.g. both tables have a column called `id`, we can use the `USING` keyword instead of `ON`. The parentheses around the column name, e.g. `(id)` are req'd.

```sql
SELECT l.id AS id, l.val AS left_val, r.val AS right_val  
FROM left_table AS l
  INNER JOIN right_table AS r
    USING (id);

SELECT c.name AS country, continent, l.name AS language, official
  FROM countries AS c
    INNER JOIN languages AS l
        USING (code)
```

**SELF JOIN**

Self join are used to compare values in a field to other values of the same field within the same table.

NOTE:

- you are required to alias the tables with self-joins.
- sql will not allow same name fields, so `p1.size`and `p2.size` need to be aliased.

```sql
-- calculate the percentage increase in population from 2010 to 2015 for each country code
SELECT p1.country_code,
       p1.size AS size2010, 
       p2.size AS size2015,
       -- 1. calculate growth_perc
       ((p2.size - p1.size)/p1.size * 100.0) AS growth_perc
FROM populations AS p1
  INNER JOIN populations AS p2
    -- 4. Match on country code
    ON p1.country_code = p2.country_code
        -- 5. and year (with calculation)
        AND p1.year = p2.year - 5;
```

**CASE**

Often it's useful to look at a numerical field not as raw data, but instead as being in different categories or groups.

You can use `CASE` with `WHEN`, `THEN`, `ELSE`, and `END` to define a new grouping field.

Example 1:

Using the countries table, create a new field `AS geosize_group` that groups the countries into three groups:

If `surface_area` is greater than 2 million, `geosize_group` is `'large'`.
If `surface_area` is greater than 350 thousand but not larger than 2 million, `geosize_group` is `'medium'`.
Otherwise, `geosize_group` is `'small'`.

```sql
SELECT name, continent, code, surface_area,
  -- 1. First case
  CASE WHEN surface_area > 2000000 THEN 'large'
    -- 2. Second case
    WHEN surface_area > 350000 THEN 'medium'
    -- 3. Else clause + end
    ELSE 'small' END
    -- 4. Alias name
    AS geosize_group
-- 5. From table
FROM countries;
```

Example 2:

Using the populations table focused only for the `year` 2015, create a new field `AS popsize_group` to organize population `size` into

`'large'` (> 50 million),
`'medium'` (> 1 million), and
`'small'` groups.
Select only the country code, population size, and this new `popsize_group` as fields.

```sql
SELECT country_code, size,
    -- 1. First case
    CASE WHEN size > 50000000 THEN 'large'
        -- 2. Second case
        WHEN size > 1000000 THEN 'medium'
        -- 3. Else clause + end
        ELSE 'small' END
        -- 4. Alias name
        AS popsize_group
-- 5. From table
FROM populations
-- 6. Focus on 2015
WHERE year = 2015;
```

Use `INTO` to save the result of the previous query as `pop_plus`.

Then, include another query below your first query to display all the records in `pop_plus` using `SELECT * FROM pop_plus`; so that you generate results.

```sql
SELECT country_code, size,
  CASE WHEN size > 50000000 THEN 'large'
    WHEN size > 1000000 THEN 'medium'
    ELSE 'small' END
    AS popsize_group
-- 1. Into table
INTO pop_plus
FROM populations
WHERE year = 2015;

-- 2. Select all columns of pop_plus
SELECT *
FROM pop_plus
```

Keep the first query intact that creates `pop_plus` using `INTO`.
Write a query to join `countries_plus AS c` on the left with `pop_plus AS p` on the right matching on the country code fields.
Sort the data based on `geosize_group`, in ascending order so that large appears on top.
Select the `name`, `continent`, `geosize_group`, and `popsize_group` fields.

```sql
SELECT country_code, size,
  CASE WHEN size > 50000000
            THEN 'large'
       WHEN size > 1000000
            THEN 'medium'
       ELSE 'small' END
       AS popsize_group
INTO pop_plus       
FROM populations
WHERE year = 2015;

-- 5. Select fields
SELECT name, continent, geosize_group, popsize_group
-- 1. From countries_plus (alias as c)
FROM countries_plus AS c
  -- 2. Join to pop_plus (alias as p)
  INNER JOIN pop_plus AS p
    -- 3. Match on country code
    ON c.code = p.country_code
-- 4. Order the table    
ORDER BY geosize_group;
```


**LEFT JOIN**

SQL provides a means of `keeping` the rows of a `JOIN` that do not match the `ON` condition - us the `LEFT JOIN` command.

Note:

- will keep all rows from the first table(and values), regardless of whether there is a matching row in the second table.
- any rows from the right table not matching the `ON` condition are dropped.
- if the join condition is not met, NULL values are used to fill in the columns from the right table.

```sql
SELECT *
FROM table1
LEFT JOIN table2
 ON table1.c2 = table2.c2;
```

**Primary Key vs Foreign Keys**

Primary key:

- uniquely identifies the rows in a table
- None of the values can be NULL.
- Each value must be unique (i.e., you can't have two customers with the same customer_id in the customers table).
- A table can not have more than one primary key column.

Foreign key:

- a column that contains the primary key of another table

The most common types of joins will be joining a foreign key from one table with the primary key from another table, e.g. when we join orders and customers, we join on customer_id, which is a foreign key in orders and the primary key in customers.

```sql
select *
from classes
join students
on classes.id = students.class_id;
```

**CROSS JOIN**

Allow you to combine all rows from one table with that of another where there is no matching information, e.g. primary-foreign key pairing.

```sql
SELECT shirts.shirt_color, pants.pants_color
FROM shirts
CROSS JOIN pants;
```

Note:

- the tables do not need to have the same number of rows
- we're simply creating a table with all possible combinations of the fields from each column
- thus if you have a table with 3 rows and another with 2, 6 combinations/rows results.

**UNION**

SQL command that allows you to combine two tables(all rows or a selection of rows) - allows you to 'stack' one data set on top of another.

Note:

- Each SELECT statement within UNION must have the same number of columns
- The columns must also have similar data types
- The columns in each SELECT statement must also be in the same order

```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

```sql
SELECT 'Customer' As Type, ContactName, City, Country
FROM Customers
UNION
SELECT 'Supplier', ContactName, City, Country
FROM Suppliers;
```

Results in a table with the 'Type', 'ContactName', 'City' and 'Country' columns.

**WITH**

Allows you to combine two tables where one is the result of a calculation - define one or more temporary tables that can be used in a subsequent query.

```sql
WITH previous_query AS (
  SELECT customer_id,
     COUNT(subscription_id) AS 'subscriptions'
  FROM orders
  GROUP BY customer_id
)
SELECT customers.customer_name, previous_query.subscriptions
FROM previous_query
JOIN customers
 ON previous_query.customer_id = customers.customer_id;
```

- `WITH` statement allows you to perform a separate query, such as aggregating a customers subscriptions
- `previous_query` is the alias that will be used to reference those results(a temporary table) in subsequent queries
- you can do whatever you want with the results, including joining them to another table

Essentially, we are putting a whole first query inside the parentheses () and giving it a name. After that, we can use this name as if it's a table and write a new query using the first query.
