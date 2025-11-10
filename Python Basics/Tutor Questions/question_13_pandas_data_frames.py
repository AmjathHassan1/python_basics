# Pandas questions
#
import pandas as pd
import numpy as np
# 1.Create a DataFrame from a Python dictionary.

d={
    "name": ["amjath", "Hassan", "Abu", "SK", "Ambu"],
    "age": [26,27, 26, 27, 100],
    "job": ["SE", "DEVOPS", "FE", "QA", "PM"],
}
df=pd.DataFrame(d)
print(df)

# 2.Display the first 5 rows and last 3 rows of a DataFrame.

print(df.head(5))
print(df.tail(3))

# 3.Find the shape (rows and columns) of a DataFrame.

print(df.shape)

# 4.Get the column names and data types of a DataFrame.

print(df.columns)
print(df.dtypes)

# 5.How do you select a single column and multiple columns from a DataFrame?

print(df['name'])
print(df[['name', 'age']])

# 6.How do you select specific rows using index labels and index positions?

df.insert(loc=0,column="id", value=[1,2,3,4,5])
print(df)

# 7.Add a new column to an existing DataFrame.

df['location'] = ['TVM', 'KLM', 'KTM', 'EKM', 'MLP']
print(df)

# 8.Delete a column from a DataFrame.

df.drop(columns=['age'], inplace=True)
print(df)