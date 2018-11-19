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

**Inserting elements**
`.insert()` - insert an element at the specified index, in-place - mutates the original list.

First arg is the index, 2nd the element.

```py
>>> lst = [1,2,3,4,5,6,7,8]
>>> lst.insert(3, 12)
>>> print(lst)
[1, 2, 3, 12, 4, 5, 6, 7, 8]
```

**Remove elements**
`.remove()` - remove the specified element, mutates the original list.

```py
>>> lst = [1,2,3,12,4,5,6,7,8]
>>> lst.remove(12) # specific element
>>> print(lst)
[1, 2, 3, 4, 5, 6, 7, 8]
```

`.pop()` - removes the specified element if the index is provided, otherwise removes the last element. Mutates the list and returns the element removed.

```py
>>> lst = [1,2,3,4,5,6,7,8]
>>> lst.pop(4) # element index
5
>>> print(lst)
[1, 2, 3, 4, 6, 7, 8]
>>> lst.pop()
8
>>> print(lst)
[1, 2, 3, 4, 6, 7]
```

`del` keyword removes the element, specify the index. Mutates the original list.

```py
>>>lst = [1, 2, 3, 4, 6, 7]
>>> del lst[2]
>>> print(lst)
[1, 2, 4, 6, 7]
```

If you don't supply an index value, `del` removes the whole list

```py
>>>lst = [1, 2, 4, 6, 7]
>>> del lst
>>> print(lst)
NameError: name 'lst' is not defined
```

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

When sorting lists of tuples, `.sort()` compares the first element in each tuple.

```py
>>>toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
>>>prices= [2,6,1,3,2,7,2]
>>>pizzas = list(zip(prices, toppings))
>>>print(pizzas)
[(2, 'pepperoni'), (6, 'pineapple'), (1, 'cheese'), (3, 'sausage'), (2, 'olives'), (7, 'anchovies'), (2, 'mushrooms')]

>>>pizzas.sort()
>>>print(pizzas)
[(1, 'cheese'), (2, 'mushrooms'), (2, 'olives'), (2, 'pepperoni'), (3, 'sausage'), (6, 'pineapple'), (7, 'anchovies')]
```

**Check if a item is in a list**
Use the `in` keyword to determine if a particular item can be found in a list, returns a boolean

```py
lst = [1,3,5,7,9,10]
if 1 in lst:
 // do something
```

## List examples

```py
#Write your function here
def double_index(lst, index):
	try:
		value = lst[index] * 2
		lst[index] = value
		return lst
	except IndexError:
		return lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
```

Remove elements from list, returning the 'remainder

```py
#Write your function here
def remove_middle(lst, start, end):
  front = lst[:start]
  back = lst[end + 1:]
  return front + back

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
```

If there are an odd number of elements in lst, the function should return the middle element. If there are an even number of elements, the function should return the average of the middle two elements.

```py
#Write your function here
def middle_element(lst):
 num = len(lst)
 if num % 2 == 0:
   print(lst[int(num/2) - 1], lst[int(num/2) ])
   return (lst[int(num/2) - 1] + lst[int(num/2)])/2
 else:
   return lst[int(num/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
```

The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.

For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

```py
#Write your function here
def append_sum(lst):
  last_two = lst[-2:]
  sum = last_two[0] + last_two[-1]
  lst.append(sum)
  last_two = lst[-2:]
  sum = last_two[0] + last_two[-1]
  lst.append(sum)
  last_two = lst[-2:]
  sum = last_two[0] + last_two[-1]
  lst.append(sum)
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))
```

The function should return a list of every third number between start and 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list.

```py
#Write your function here
def every_three_nums(start):
  if start > 100:
    return []
  else:
  	return list(range(start, 103, 3))

#Uncomment the line below when your function is done
print(every_three_nums(91))
```
