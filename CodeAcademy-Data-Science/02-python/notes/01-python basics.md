# Lists

Lists in python are ordered and mutable, you can have duplicate members (equivalent to Arrays in JS)

- can be of mixed data types

**List methods**
append() - add items it the end of the list

**combine Lists using ZIP**
Takes 2 (or more) lists as inputs and returns a List of tuples, each tuple containing the corresponding elements from each input list, i.e., first tuple will contain the elements with index 0, and so on.

```py
names = ['Jenny', 'Alex', 'Sam', 'Grace']
dogs_names = ['Max', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
print(names_and_dogs_names)

# printing the result returns the objects location in RAM
<zip object at 0x7f1631e86b48>

# use the list() to view the result
print(list(names_and_dogs_names))
[('Jenny', 'Max'), ('Alex', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]
```

**Combine lists**
Combine 2 or more lists with '+'

- does not work if you try and add individual values to a list(returns a `TypeError`), use append(), or place it in [].

```py
[1,2,3,4] + [5,6,7,8] + [9,10,11]
>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

>>> list1 = [1,2,3,4]
>>> list2 = [5,6,7,8]
>>> list3 = list1 + list2
>>> list3
[1, 2, 3, 4, 5, 6, 7, 8]

>>> list4 = list3 + [9,10,11]
>>> list4
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
```

**Creating a range**
Use the `range()` method to create a list of consecutive numbers.

- range() takes a single input and returns an object that can be converted to a list using `list()`
- generates a list starting at 0, and ending at the number before the input value.

```py
>>> my_range = range(10)
>>> list(my_range)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

To generate a list starting at a number other than 0, pass 2 args to `range()`

- the 1st arg is the starting point
- with the list ending at the value before the 2nd arg

```py
>>> my_list = range(4, 10)
>>> list(my_list)
[4, 5, 6, 7, 8, 9]
```

If we pass a 3rd arg to `range()`, we can set the number we want each value in the sequence to increment by:

```py
>>> list(range(0, 100,10))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

>>> list(range(0, 40, 5))
[0, 5, 10, 15, 20, 25, 30, 35]
```
