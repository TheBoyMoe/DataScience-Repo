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
- is a parameter, the column name and it's data type that are passed as an argument

```sql
CREATE TABLE celebs (
   id INTEGER,
   name TEXT,
   age INTEGER
);
```
