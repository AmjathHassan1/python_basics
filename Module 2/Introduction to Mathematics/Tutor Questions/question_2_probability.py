# Probability questions

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1.load iris dataset from seaborn

df=pd.read_csv('iris.csv')
print(df)
print(df.columns)
# 2.consider sepal_length

print(df['SepalLengthCm'])

# Find mean,median,mode

print(np.mean(df['SepalLengthCm']))
print(np.median(df['SepalLengthCm']))

print(df['SepalLengthCm'].mean())
print(df['SepalLengthCm'].median())
print(df['SepalLengthCm'].mode()[0])

# 3.standard deviation

print(np.std(df['SepalLengthCm']))

# 4.variance

print(np.var(df['SepalLengthCm']))

# 5.range

print(np.max(df['SepalLengthCm']) - np.min(df['SepalLengthCm']))

# 6.plot it's distribution.

sns.histplot(df['SepalLengthCm'], kde=True)
plt.show()

# 7.calcate skewness
from scipy.stats import skew
print(skew(df['SepalLengthCm']))


# 8.check whether this column distribution is positively skewed, negative skewed or normal.

s = skew(df['SepalLengthCm'])

if s > 0:
    print("Distribution is positively skewed.")
elif s < 0:
    print("Distribution is negatively skewed.")
else:
    print("Distribution is approximately normal.")

# 9.check the distributions of other features also by using histplot.


numeric_cols = df.select_dtypes(include='number').columns
#
# for col in numeric_cols:
#     sns.histplot(df[col], kde=True)
#     plt.title(f"Distribution of {col}")
#     plt.show()


# 10.calculate the correlation and display by using heatmap

corr = df.select_dtypes(include='number').corr()

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
