# Statistics in NumPy

The statistical concepts that we'll cover include:

- Mean - is the average
- Median - value lying in the mid-point(middle value) of the set (Mode is the value that occurs most often)
- Percentiles - determine the value a given percentage of observations lie below, 75% of values lie below 4.265
- Interquartile Range
- Outliers - sort the data set, look for any outliers
- Standard Deviation - a value expressing by how much the members of a group differ from the mean for the group(determine how similar or different the members of the dataset are)

We'll be analyzing single-variable datasets.

```py
water_height = np.array([4.01, 4.03, 4.27, 4.29, 4.19,
                        4.15, 4.16, 4.23, 4.29, 4.19,
                        4.00, 4.22, 4.25, 4.19, 4.10,
                        4.14, 4.03, 4.23, 4.08, 14.20,
                        14.03, 11.20, 8.19, 6.18, 4.04,
                        4.08, 4.11, 4.23, 3.99, 4.23])

np.mean(water_height) # 5.251
np.sort(water_height) # by default sort in asc order
np.median(water_height) # 4.19
np.percentile(water_height, 75) # 4.265
np.std(water_height) # 2.784
```

**Mean/Average**

`.mean` - built in function of numpy arrays used to calculate the mean/avg of a numpy array

```py
>>>survey_responses = [5, 10.2, 4, .3 ... 6.6]
>>> survey_array = np.array(survey_responses)
>>> np.mean(survey_array)
5.220
```

We can also execute a condition on each element in the array in turn prior to determining the `mean`. If the condition is matched, True, the value is included in the calculation, otherwise it is not. The percentage of values in the data set returning 'True' will be calculated by dividing the total number of 'True' values by the 'Total' data set size.

```py
class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015, 2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])

millenials = np.mean(class_year >= 2005)
print(millenials) # percentage of millenials 0.21
```
