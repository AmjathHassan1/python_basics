# Series questions
#
import numpy as np
import pandas as pd
# 1.Create a Pandas Series from a list of numbers [10, 20, 30, 40, 50].

s=pd.Series([10, 20, 30, 40, 50], dtype='int')
print(s)

# 2.Create a Series from a Python dictionary {'a':100, 'b':200, 'c':300}.
data = {'a':100, 'b':200, 'c':300}
s1=pd.Series(list(data.values()), index=list(data.keys()), dtype='int')
print(s1)

# 3.Create a Series from a NumPy array [1, 2, 3, 4, 5].

arr=np.array([1, 2, 3, 4, 5])
s2=pd.Series(arr)
print(s2)

# 4.Display the index and values of a Series.

s4=pd.Series(arr)
print(s4)
print(s4.values)
print(s4.index)

# 5.Change the index of a Series to custom labels like ['A', 'B', 'C', 'D', 'E']

s5=pd.Series(arr, index=['A', 'B', 'C', 'D', 'E'])
print(s5)

# 6.Access the first three elements of a Series.

print(s5.head(3))

# 7.Access elements using label-based indexing (.loc[]).

print(s5.loc['A'])
print(s5.loc['B'])
print(s5.loc['C'])

# 8.Access elements using position-based indexing (.iloc[]).

print(s5.iloc[0])
print(s5.iloc[1])
print(s5.iloc[2])

# 9.Retrieve a single element using both .loc and .iloc.

print(s5.loc['A'], s5.iloc[0])

# 10.Slice a Series from index 2 to 4.

print(s5[2:5])

# 11.Create a Series of marks [50, 60, 70, 80] and add 10 to each element.

s6=pd.Series([50, 60, 70, 80])
added_mark=s6+10
print(added_mark)

# 12.Find the mean, max, and min of a numeric Series.

print(s6.mean())
print(s6.max())
print(s6.min())


# 13.Convert a Series into a Python list.

print(list(s6))
print(s6.to_list())

# 14.Sort a Series in ascending and descending order.

print(s6.sort_values(ascending=False))