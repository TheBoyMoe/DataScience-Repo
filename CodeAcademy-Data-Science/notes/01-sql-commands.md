# SQL

[CodeAcademy SQLite Command Cheatsheet](https://www.codecademy.com/articles/sql-commands)

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

- fetch data from a table

```sql
SELECT column_name(s) FROM table_name;
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
