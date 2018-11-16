# Handling Multiple Tables in SQl

**JOIN**

We use `JOIN`s to combine 2 tables in sql.
The combined table only includes rows(with all the values from both tables) that match the `ON` condition, i.e. where the two fields being compared are equal.

```sql
SELECT *
FROM orders
JOIN customers
ON orders.customer_id = customers.customer_id;
```

Note:

- the `customer_id` column appears twice in the resulting table when `SELECT *` is used.
- because column names are often repeated across multiple tables, use the syntax table_name.column_name to be sure that our requests for columns are unambiguous. Here, we use it in the ON statement, but we can also use it in the SELECT or any other statement where we refer to column names.
- this is a simple `JOIN` or `INNER JOIN`.

```sql
SELECT orders.order_id, customers.customer_name
FROM orders
JOIN customers
 ON orders.customer_id = customers.customer_id;
```

```sql
select *
from orders
join subscriptions
on orders.subscription_id = subscriptions.subscription_id
where description = 'Fashion Magazine';
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
