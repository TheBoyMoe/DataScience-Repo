# More Python

### Lambda Function

A lambda function is a way of defining a function in a single line of code, which is usually assigned to a variable, e.g.

```py
mylambda = lambda x: (x * 2) + 3
```

Note:

1. there is an implicit return
2. 'x' is the parameter passed to the codeblock, which starts after the ':'
3. you can pass in any type of variable

```py;
# return the 1st and last letter of a string
mylambda = lambda x: x[0] + x[-1]
```

We can add some logic and include conditionals in our lambdas:

```py
mylambda =  lambda x: 40 + (x - 40) * 1.50 if x > 40 else x
```

The general pattern:

```py
lambda x: [OUTCOME IF TRUE] \
    if [CONDITIONAL] \
    else [OUTCOME IF FALSE]

mylambda = lambda x: 'Welcome to BattleCity!' if x >= 13 else 'You must be over 13'
```
