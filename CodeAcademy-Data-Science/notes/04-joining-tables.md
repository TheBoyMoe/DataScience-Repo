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

```sql
SELECT *
FROM table1
LEFT JOIN table2
 ON table1.c2 = table2.c2;
```
