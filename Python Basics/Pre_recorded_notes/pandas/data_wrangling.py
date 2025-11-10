# Data Wrangling
# process of transforming and combining data for analysis
# provides methods like `merge`, `concat`, `join`, and `group by`
# help in real world data efficiency
from operator import index

import pandas as pd

df1=pd.DataFrame({"ID":[1, 2 , 3], "Name": ["A", "B", "C"]})
df2=pd.DataFrame({"ID":[1, 2 , 4], "Score": [88,45,77]})

print(df1)
print("\n")
print(df2)


# merge() is used to combine two data frame based on common columns (like SQL join)

print(pd.merge(df1, df2, how="left", on="ID"))
print("\n")
print(pd.merge(df1, df2, how="right", on="ID"))
print("\n")
print(pd.merge(df1, df2, how="outer", on="ID"))
print("\n")
print(pd.merge(df1, df2, how="inner", on="ID"))
print("\n")

# concat() append rows or columns of multiple data frames

df1=pd.DataFrame({"ID":[1, 2 , 3], "Name": [1,2,3]})
print(df1)
print("\n")
df2=pd.DataFrame({"ID":[4, 5], "Name": [88,45]})
print("\n")
cancat_df=pd.concat([df1, df2])
print(cancat_df)
print("\n")

# join() : used to combine two DataFrames based on their index

df1=pd.DataFrame({"A": [10, 20] }, index=['x', 'y'])
print(df1)
print("\n")
df2=pd.DataFrame({"B": [30, 40]}, index=['x', 'y'])
print(df2)
print("\n")
joined_df=df1.join(df2)
print(joined_df)
print("\n")

# groupby() : is used to group and aggregate data

df=pd.DataFrame({"Category": ["A", "B", "A", "B"], "Sales": [100, 200, 300, 400] })
grouped_df=df.groupby('Category').sum()
print(grouped_df)









