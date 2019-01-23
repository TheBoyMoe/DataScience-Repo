# SQL

[CodeAcademy SQLite Command Cheatsheet](https://www.codecademy.com/articles/sql-commands)

A relational database is a database that organizes information into one or more tables or `relations`.

A table is a collection of data organized into rows and columns.

## SQL Introduction

**SQL Data types**
Interger
Real - float
Text - string
Date - formatted as 'YYYY-MM-DD'

Note: SQLite does not have booleans - stored as 0(false), 1(true)

Reference:
[SQLite Data types](https://www.tutorialspoint.com/sqlite/sqlite_data_types.htm)

**SQL Statements**

- text that the database recognises as a valid command
- always ends in a semicolon ';'

```sql
CREATE TABLE table_name (
 column_1 data_type,
 column_2 data_type,
 column_3 data_type
);
```

`CREATE TABLE`

- is a 'clause', performs a specific task, e.g. `CREATE/ALTER/DROP TABLE`.
- by convention are written in CAPITALS.

`table_name`

- name of the table

`column_1 data_type`

- defines each column
- pass in one or more parameters
- each parameter is a column name and it's data type that are passed as an argument

```sql
CREATE TABLE celebs (
   id INTEGER,
   name TEXT,
   age INTEGER
);
```

**Insert statements**

- inserts a new row/record into the table

```sql
INSERT INTO celebs (id, name, age)
VALUES (1, 'Justin Bieber', 22);
```

`INSERT INTO`

- clause that adds a new record to the specified table

`VALUES`

- clause that indicates the data being inserted
- in the same order as the columns

**Select statements**

- fetch data from a table- query a table.

```sql
SELECT column_name(s) FROM table_name;

SELECT * FROM table_name WHERE column_name = value;

select * from celebs where id = 1;
select * from celebs limit 10; -- limit result set to 1st 10 records
```

`SELECT`

- is a clause used in every database query
- specify one or more columns with a comma separated list
- always return a new table called a 'Result Set'
- use the '\*' wild card to specify all columns

**Alter statements**

- used to add a new column to a table
- for rows that existed before the addition, value will to NULL

```sql
ALTER TABLE table_name
ADD COLUMN column_name data_type

ALTER TABLE celebs
ADD COLUMN twitter_handle TEXT
```

`ADD COLUMN` clause used to specify the column name and data type

**Update statements**

- edit and existing record/row

```sql
UPDATE table_name
SET column_1 = new_value
WHERE column_2 = value;

UPDATE celebs
SET twitter_handle = '@taylorswift13'
WHERE id = 4;
```

`SET` - indicates the column to edit, and the new value to insert
`WHERE` - clause that identifies the record to update

**Delete statements**

- delete one or more rows

```sql
DELETE FROM table_name
WHERE column_name = value;

DELETE FROM celebs
WHERE twitter_handle IS NULL;
```

`DELETE FROM` is the clause that deletes the rows
`WHERE` used to select the appropriate rows
`IS NULL` sql condition that returns `true` when that columns value is NULL

**Constraints**

- add a constraint/restriction on how a column can be used(define how a column can be used)

```sql
CREATE TABLE celebs (
  id INTEGER PRIMARY KEY,
  name TEXT UNIQUE,
  date_of_birth TEXT NOT NULL,
  date_of_death TEXT DEFAULT 'Not Applicable'
);
```

`PRIMARY KEY` - used to uniquely identify a row, your prevented from inserting another row with the same value
`UNIQUE` - similar to primary key, except a table can have many unique values but only one primary key
`NOT NULL` - column MUST have a value, prevented from inserting a row without a value for the column
`DEFAULT` - value applied, if none is supplied

**Copy an SQL Table**

Use the `CREATE...AS` command to create a copy of an existing table, e.g. copy over only certain columns, use '\*' to make an exact copy.

```sql
CREATE TABLE TestTable AS
SELECT customername, contactname
FROM customers;
```

To copy only specific rows based on a condition:

```sql
CREATE TABLE new_table_name AS
SELECT column1, column2,...
FROM existing_table_name
WHERE ....;
```

References:
[SQL commands](https://www.w3schools.com/sql/default.asp)

**Rename a Table**

```sql
ALTER TABLE [existing_table_name]
RENAME TO [new_table_name];
```
