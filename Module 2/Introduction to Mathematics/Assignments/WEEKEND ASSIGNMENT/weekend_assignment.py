# WEEKEND ASSIGNMENT
# Create a dataframe with the following columns: name, age, and gender. The
# dataframe
# should have 10 rows of data. (Score: 2)

import numpy as np
import pandas as pd



data = [
        {'name': 'Hari', 'age': 20, 'gender': 'male'},
        {'name': 'Midhila', 'age': 26, 'gender': 'female'},
        {'name': 'Varsha', 'age': 20, 'gender': 'female'},
        {'name': 'Midhun', 'age': 26, 'gender': 'male'},
        {'name': 'Arun', 'age': 21, 'gender': 'male'},
        {'name': 'Gokul', 'age': 30, 'gender': 'male'},
        {'name': 'Anu', 'age': 28, 'gender': 'female'},
        {'name': 'Rahul', 'age': 40, 'gender': 'male'},
        {'name': 'Favas', 'age': 26, 'gender': 'male'},
        {'name': 'Anjali', 'age': 18, 'gender': 'female'},
        ]
df = pd.DataFrame(data)
print("data frame : \n", df)

# 1) Add a new column to the data frame created in question 1, called occupation.

df['occupation'] = 'Unknown'

print("data frame : \n", df)


# The values for this column should be Programmer, Manager, and Analyst,
# corresponding to the rows in the dataframe. (Score: 1)

occupation = ['Programmer', 'Manager', 'Analyst']

df['occupation'] = np.random.choice(occupation, len(df))

print("data frame : \n", df)

# 2) Select the rows of the dataframe where the age is greater than or equal to 30.
# (Score: 1)

print(df[df['age'] >= 30])

# 3) Convert this dataframe to a CSV file and read that CSV file, and finally display
# the contents. (Score: 1)


df.to_csv('data.csv', index=False)

from_csv_df = pd.read_csv('data.csv')
print(from_csv_df)