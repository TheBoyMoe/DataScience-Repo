# List Methods

- get the length of a list
- select subsets of a list (called slicing)
- count the number of times that an element appears in a list
- sort a list of items

**List length**
Use the `len()` method - pass the list to the method

```py
list1 = range(2, 20, 2)
print(len(list1)) # 9
```

**Selecting elements**
Select elements using [], lists are zero-indexed e.g. `list[2]` retruns the 3rd element in the list.

Selecting an element that does not exist throws an `IndexError: list index out of range`

Select the lst element with the index `-1`, e.g. `list[-1]`

**Slicing lists**
We can slice lists using the following syntax, `list[start:end]`

- start is the index of the 1st element we want to include in the list
- end is the index last element(upto but NOT including)

```py
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
>>> sublist = letters[2:6]
>>> print(sublist)
['c', 'd', 'e', 'f']
```

Note:

When starting from the beginning of a list, e.g. `[0:3]`, you can omit the '0', e.g. `[:3`]

When you want to go upto and include the end of the list, you can omit the index of the last element, e.g. `[2:]`

We can also use 'negative' indexes to count backward from the last element, e.g. `[-3:]` returns the last 3 elements of the list

```py
>>>suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
>>>start = suitcase[:3]
>>>print(start)
['shirt', 'shirt', 'pants']

>>>end = suitcase[-2:]
>>>print(end)
['pajamas', 'books']

# the original list is unchanged
>>>print(suitcase)
['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
```

**Counting elements**
You can count the number of times a specific element occurs in a list with the `.count()` method

```py
>>> letters = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']
>>> print(letters.count('i'))
4

>>> votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
>>> print(votes.count('Jake'))
9
```

**Sorting lists**
You can sort a list 'in place' (the original list is mutated) using `.sort()`. Sort does NOT return anything(None).

```py
>>> names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
>>> names.sort()
>>> print(names)
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

you can also sort lists with `sorted()`, which returns a NEW list, leaving the original unchanged.

```py
>>> names = ['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
>>> sorted_names = sorted(names)
>>> print(sorted_names)
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
>>> print(names)
['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
```
