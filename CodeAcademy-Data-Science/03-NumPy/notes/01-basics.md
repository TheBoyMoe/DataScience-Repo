# NumPy

NumPy(Numerical Python) has many uses including:

- efficiently working with many numbers at once
- generating random numbers
- performing many different numerical functions (i.e., calculating sin, cos, tan, mean, median, etc.)

We'll be looking at `single variable` datasets - contains a singe value for each property/data point.

Start by importing the NumPy package at the top of your file:
`import numpy as np`

Numpy uses an `array` data structure to organise data items.

- can be any data type, including strings, numbers and other arrays - MUST be same data type, otherwise numpy will try and upcast the value, e.g. ints cast to floats.
- transform a regular list into a NumPy array by using `.array()`
- common data types(dtype) include int8/16/32/64, float16/32/64/128, bool and string(fixed length)
- special numerical types nan(NaN) and inf(Infinity) - use isnan() and isinf() to identify nan and inf values, do not use ==.

```py
# create an numpy array from a python list
my_array = np.array([1,2,3,4])
```

To explicitly set the data type, use the `dtype` keyword

```py
>>>my_array = np.array([1,2,3,4,5], dtype='float32)
[1., 2., 3., 4., 5.]
```

Normally we'll import data directly into np arrays from csv files using the `.genfromtxt()`

```py
csv_array = np.genfromtxt('sample.csv', delimiter=',')
```

**Performing operations on NumPy arrays**

Numpy arrays are more efficient than lists when performing operations. Numpy arrays allow you to perform 'element-wise operations', e.g. addition on elements in the array directly.

Note: these operations depend on ALL the elements in the arrays being of the SAME type

```py
# With a list
l = [1, 2, 3, 4, 5]
l_plus_3 = []
for i in range(len(l)):
  l_plus_3.append(l[i] + 3)

# With an array
# add 3 to each element in the array(same is true of substraction, multiplication and division)
a = np.array(l)
a_plus_3 = a + 3

# to square each value
>>>a ** 2
array([16, 25, 36, 49, 64])

# taking the square root of each value
>>>np.sqrt(a)
array([4, 5, 6, 7, 8])
```

**Adding/Substracting NumPy arrays**

Numpy arrays can be added together or subtracted(2 or more), must have the same number of elements. Individual elements in the same positions will be added/subtracted.

```sql
>>> a = np.array([1, 2, 3, 4, 5])
>>> b = np.array([6, 7, 8, 9, 10])
>>> a + b
array([ 7,  9, 11, 13, 15])
```

```py
import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

total_grade = test_1 + test_2 + test_3_fixed
print(total_grade)
>>>[260 281 248 276 272]

# find the average for each student
final_grade = total_grade / 3 # divide each value by num tests
print(final_grade)
>>>[86 93 82 92 90]
```

**2-D NumPy arrays**

Numpy supports 2-D arrays - nested arrays are all the SAME size. 2-D arrays are often used to represent a set of samples.

```sql
np.array([[92, 94, 88, 91, 87],
         [79, 100, 86, 93, 91],
         [87, 85, 72, 90, 92]])
```

**Selecting elements from 1-D array**

We can select elements from 1-D arrays using their indices, numpy arrays are zero index.

```py
a = np.arrays([1,2,3,4,5,6])
value = a[3]
>>> 4
```

Like python lists you can use negative indices, and select multiple elements with ranges

```py
 a = np.arrays([1,2,3,4,5,6])
 val1 = a[-1] # last element
 >>> 6

 val2 = a[-2]
 >>> 5

# selecting multiple elements returns an array
 b = a[1:4]
 >>> array([2,3,4])

 c = a[-3:]
 >>> array([4,5,6])
```

**Selecting elements from a 2-D array**

Specify both the `row` and the `column` index(rows start from zero)

NOTE:

In a 2-D array, the axes correspond to the interior arrays in the following way:

axis=0 are values that share an index (in the same column) and axis=1 are values share an array (in the same row) - the answer is flipped!

We can also think of axis=0 as the columns and axis=1 as the rows.

```py
a = np.array([[32, 15, 6, 9, 14],
             [12, 10, 5, 23, 1],
             [2, 16, 13, 40, 37]])

>>>a[2,1] # returns a single element at the intersection of the two indices
16
```

To select an entire column, insert `:` as the row index

```py
>>>a[:, 0] # return the 1st column
array([32, 12, 2])
```

To select an entire row, insert `:` as the column index

```py
>>>a[1, :] # return the 2nd row
array([12, 10, 5, 23, 1])
```

To select a range from a row:

```py
>>>a[0, 0:3] # 1st row, 1st 3 elements
array([32, 15, 6])
```

**Logical operations**

We can perform element-wise logical operations on NumPy arrays

```py
# determine how many elements are > 5
>>> a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
>>> a > 5
array([True, False, False, False, False, False, True, True, True, True], dtype=bool)

# To select all elements that are > 5
>>>a[a > 5]
array([10, 9, 8, 9, 7])

# We can combine logical & and or
>>> a[(a > 5) | (a < 2)] # elements > 5 OR < 2
array([10, 9, 8, 9, 7])
```

```py
import numpy as np

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]
hot = porridge[porridge > 80]
just_right = porridge[(porridge >= 60) & (porridge <= 80)]
```
