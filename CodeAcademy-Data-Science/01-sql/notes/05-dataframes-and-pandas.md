# DataFrames and Panda Library

Pandas are a python library that supports manipulating tables (also panels and series)

- tables are represented as a `DataFrame` (2-D array) of rows(index) and columns
- the columns can be of different data types
- both the size and the data are mutable

```py
import pandas as pd

orders = pd.read_csv('orders.csv')

products = pd.read_csv('products.csv')

customers = pd.read_csv('customers.csv')

print(orders)
print(products)
print(customers)
```

Where in SQL we `join` different tables, with pandas we `merge` two DataFrames.
Pandas uses the `merge()` to merge DataFrames.

- looks for columns that are common between two DataFrames
- then looks for rows where those column's values are the same.
- then combines the matching rows into a single row in a new table.

```py
new_df = pd.merge(orders, customers)
print(new_df)
```

Example:

```py
import pandas as pd

sales = pd.read_csv('sales.csv')
targets = pd.read_csv('targets.csv')

print(sales)
print(targets)

sales_vs_targets = pd.merge(sales, targets)
print(sales_vs_targets)

crushing_it = sales_vs_targets[sales_vs_targets.revenue > sales_vs_targets.target]
```

You can call `merge()` on the DataFrame directly

```py
new_df = sales.merge(targets)
```

is equivalent to:

```py
new_df = pd.merge(sales, targets)
```

You can also merge more than two tables, and chain the the operations:

```py
new_df = orders.merge(products).merge(products)
```

```py
import pandas as pd

sales = pd.read_csv('sales.csv')
targets = pd.read_csv('targets.csv')
men_women = pd.read_csv('men_women_sales.csv')

all_data = sales.merge(targets).merge(men_women)

print(all_data)

results = all_data[(all_data.revenue > all_data.target) & (all_data.women > all_data.men)]
print(results)
```

Generally both the orders and customers tables have an id column, refering to the order_id and customer_id in their respective tables. Using `merge()` in this case would not work. In these cases, Pandas provide the `rename()` method, e.g

```py
pd.merge(
  orders,
  customers.rename(columns={'id': 'customer_id'}))
```
