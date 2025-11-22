# Linear Algebra and Probability
#
# In this assignment, you will apply Linear Algebra and Probability techniques to analyze the Wine
# Quality Dataset. The dataset consists of 1599 rows and 12 columns, detailing various chemical
# properties of red and white wines and their quality scores. Your tasks will focus on vectors,
# matrices, eigenvalues, eigenvectors, and basic probability concepts. You can download the
# dataset from the link given below. The dataset contains 1599 samples of wine, with features
# such as acidity, alcohol content, pH, residual sugar, and others, alongside the target variable,
# wine quality.
import pandas as pd
import pandas as pdn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset and handle any missing data by replacing null values with the mean
# value of the respective column. (Score 2)



df = pd.read_csv('winequality-red.csv', sep=';')
print(df.shape, df.columns)

df = df.fillna(df.mean(numeric_only=True))

print("Missing values after filling:")

# 2. Extract the following columns as vectors: alcohol,citric acid. (Score 2)

alcohol_vector = df['alcohol'].values
citric_acid_vector = df['citric acid'].values

print("Alcohol vector:", alcohol_vector)
print("Citric acid vector:", citric_acid_vector)

# 3. Select two features (e.g., alcohol and density) from the dataset and calculate the
# covariance matrix using np.cov(X.T), where X is the feature matrix consisting of the
# selected columns.(Score 2)


X = df[['alcohol', 'density']].values
print(X.shape)
cov_matrix = np.cov(X.T)

print("covariance Matrix:", cov_matrix, cov_matrix.shape)


# 4. Perform eigen decomposition on the covariance matrix you computed in question 3.
# Identify and interpret the results:Identify the top 2 eigenvalues of the covariance
# matrix,Identify the corresponding eigenvectors.(Score 2)

eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
print("eigen_values:", eigen_values)
print("eigen_vectors:", eigen_vectors)


# 5. Which wine quality is most common in the dataset? How can you interpret the
# distribution of wine quality scores? (Score 2)


most_common_quality = df['quality'].mode()[0]
print("most common quality:", most_common_quality)

sns.histplot(x=df['quality'], bins=100, kde=True)
plt.show()


# when analyzing hist plot 5 is the most common quality, the quality is not uniformily distributed
# also it is right skewed. The overall quality is poor because quality 6 and 7 are lesser when comparing to 5 an 6