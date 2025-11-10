# #pandas
# from operator import index
#
# # built in top of numpy
# # manipulating data and time
# # popular importing analyzing data
# # 3 data structures : series, data frames, panel
#
#
# # 1. Series
# # one dimensional labeled array that can store any data types.
#
# import pandas as pd
# data=pd.Series([1,2,3,4,5,6,7,8,9,10], index=['a','b','c','d','e','f','g','h','i','j'])
#
# print(data)
# print(data.loc['a']) # Accessing with label (label based indexing)
# data1=pd.Series([1,2,3,4,5,6,7,8,9,10])
# print(data1)
#
# # indexing
# print(data1.iloc[0]) # Accessing without label (integer based indexing)
#
#
# # slicing
# print(data['b':'c'])
# print(data[1:3])
#
# data['k']=11
# print(data)
#
# data['c']=30
# print(data)
#
# data.drop('c',inplace=True) # inplace True only removes the label from data,
# print(data)
#
# data.drop('b') # inplace False doesn't remove from data,  returned value have doesnt have dropped label
# d = data.drop('b')
# print(data)
# print(d)
#
#
# # Series Attributes
#
# print(data.index)
# print(data.values)
# print(data.dtypes)
# print(data.size)
# print(data.shape)
#
# # Series Methods
# print(data.head(2))
# print(data.tail(2))
#
# print(data.sum())
# print(data.mean())
# print(data.median())
# print(data.sort_values())
# print(data.sort_index(ascending=False))
#

# DataFrame

# two-dimensional , labeled data structure in  pandas
# rows and columns, similar to an excel spred sheet
# easy manipulation, analysis, and visualization

import pandas as pd
data={
    "name":["amjath"," hassan", "sk"],
    "age": [12,11,14],
    "city":["tvm", "klm","ekm"]
}
df=pd.DataFrame(data)
print(df)

print(df['name'])  # Accessing a single column
print(df[['name', 'age']])  # Accessing a multiple column
print(df[['name', 'age', 'city']])  # Accessing a multiple column

print(df.loc[0, "name"]) # label based indexing
print(df.iloc[0, 2]) # label based indexing

print(df['age']>11)
print(df[df['age']>11])  # boolian based indexing/filtering

print(df)

print(df.iloc[0:2, 1:]) # First 2 rows, all columns except first df.iloc[row,column]

print(df)
df['salary']= [1000,2000,3000] # adding new column to data
print(df)

df.loc[df['name']=='amjath', 'salary']=10000000  # updating data
print(df)

df.drop(columns=['city'], inplace=True)
print(df)

df.drop(index=[1], inplace=True)
print(df)


# Data Frame Attributes and methods

print(df.shape)
print(df.columns)
print(df.dtypes)

print(df.info())
print(df.describe())


















