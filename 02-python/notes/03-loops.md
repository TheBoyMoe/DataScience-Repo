# Loops

## For Loops

Iterate through each element in a list using a `for..in` loop

General syntax:

```py
for [temporary variable] in [list]:
  # do something
  # and more

# no longer part of the loop
```

The colon and indentation are required. Everything at the same level of indentation is included in each iteration.

We can also use a `for..in` loop in combination with a `range` to execute a specific action a certain number of times, e.g.

```py
>>>for i in range(4):
>>>  print('BYE!')
BYE!
BYE!
BYE!
BYE!
```

You can also iterate through the characters of a string, e.g.

```py
>>>for i in 'hello':
>>>  print(i)
h
e
l
l
o
```

**Break**
Stop a loop from iterating any further with the `break` keyword. Control returns to the code outside of the loop

```py
items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband", "dinosaur_onesie"]

print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit_dress":
    break
print("End of search!")
```

**Continue**
Allows you to skip a loops iteration if a condition is met, but not terminate the loop. The loop continues from thenext iteration.

```py
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
  if i < 0:
    print('Found less than 0')
    continue # causes all subsequent lines to be skipped
  print(i)
```

## While Loops

Continues iterating through the loop until a condition is met

```py
dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

index = 0
while index < len(dog_breeds):
  print(dog_breeds[index])
  index += 1


all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alex", "Arius", "Loki"]
students_in_poetry = []

index = 6
while len(students_in_poetry) < index:
  students_in_poetry.append(all_students.pop())
```

## Nested Loops

```py
project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

for team in project_teams:
  for student in team:
    print(student)
```

## List Comprehensions

Consider the list

```py
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
```

We want to make a new list, called usernames, that has all of the strings in words with an '@' as the first character. We know we can do this with a for loop:

```py
usernames = []

for word in words:
  if word[0] == '@': # first char in word
    usernames.append(word)

>>>["@coolguy35", "@kewldawg54", "@matchamom"] # result
```

Python has a convenient shorthand way of handling this sort of problem, called `list comprehension`, e.g.

```py
usernames = [word for word in words if word[0] == '@']

>>>["@coolguy35", "@kewldawg54", "@matchamom"] # result
```
