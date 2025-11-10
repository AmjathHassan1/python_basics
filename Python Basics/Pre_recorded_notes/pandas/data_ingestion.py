# Data ingestion
# process of reading data from various source into pandas data frame
# common formates includes csv, Excel, JSON, SQL, etc
# 'read_csv() ' is one of the most commonly used methods to load data



import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(2))   # first 2 rows
print(df.tail(2))
print(df.shape)  # rows columns
print(df.columns())  # shows the columns
print(df.index)
print(df.info())
print(df.describe())

print(df['age'].value_counts())  # counts the value based in columns