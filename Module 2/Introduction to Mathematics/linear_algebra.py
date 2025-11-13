'''
Vector

A vector is a mathematical quantity that has both magnitude and direction.

In data science and programming , a vector usually means a list of
array of number that represents data or features.

# A scalar is just one number -> e.g : 5
# A vector is a collection of numbers -> e.g: [5,3,2]

Each number in the vector is called a component.

(the entire row in a data-set)

Why Vectors Are Important In Data Science

- They reprecent data points, features or models weights.
- Many machine llearning algorithms compute operations like:
    + Dot product (measures similarity)
    + Norm (length or magnitude of a vector)
    + Matrix-vector multiplication ( used in linear regression, neural networks , ets)


Vector are simply an ordered list of elements

In DS,m, We use vectors to reprecent data.

MATRIX

A matrix is rectangular arrangement of numbers (or data) organized in rows and columns.

It is basically a collection of vectors put together - and
is one of the most important tools in data science , machine learning and linear algebra


Each row = one data point (one vector)

Each column = one feature

whole  dataset = matrix


TENSOR

Tensors are fundamental in deep learning , especially in framework like
TensorFlow and Pytorch

- Scalar -> 0D
- Vector -> 1D
- Matrix -> 2D
- Tensor -> nD (n>=3)

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df=pd.read_csv('iris.csv')
print(df.columns)

# For statical Information
print(df.describe())

df.drop(["Id"], axis=1, inplace=True)
# sns.boxplot(data=df)
# plt.show()


# sns.histplot(data=df['PetalWidthCm'], kde=True)
# plt.show()

# sns.histplot(data=df['SepalWidthCm'], kde=True)
# plt.show()

'''
skewness=0
means the symmetrical the data points are accumulted equally on both sides
histplot is used to find the skewness of the data points
in this case normal distribution skewness is 0

'''

vector=df.iloc[0,0:4]
vector=df.iloc[0,0:4].astype('float').values
# print(vector)

matrix=df.iloc[:,0:4].values
print(matrix, matrix.shape)

# Taking transporse of a matrix T

matrix_transpose=matrix.T
print(matrix_transpose)

# covariance
# - relation between to parameters or feature
# - reprecents the attributes direction postive or negative
# co relation - scalar value (-1 to 1)
# 0 -> no realation beteween two parameter
# -ve-> inverse relation


cov_matrix=np.cov(matrix.T)
print(cov_matrix)

features=["sepal_length","sepal_width","petal_length","petal_width"]
cov_df=pd.DataFrame(cov_matrix, index=features, columns=features)
print(cov_df)

sns.heatmap(cov_df, annot=True)
plt.show()


'''
DETERMINANTS

A determinant is a single number that can be calculated from a
square matrix with the same number of rows and columns

It tells us important properties about the matrix -- such as it is Invertible,
how it scales space and wheather its vector are linearly independent

Used in pca for dimensionality reduction


A = [[ a b ]
    [c d ]]   |A| = ad-bc
    
A=[[ a b c]
    [d e f]
    [g h i]]   |A| = a(ei-fg)-b(di-gf)-c(dh-eg) 
    
    
   

'''

determinat = np.linalg.det(cov_matrix)
print(determinat)

'''
EIGEN VECTORS AND  EIGEN VALUES

Eigen values and Eigen vectors are very inportant concepts in linear algebra,
and they play a huge role in data science , machine learning and deep learning
(especially in dimensionality reduction) like PCA)

When you multiply a matrix by vector , it usually changes the both magnitude and the directiobns of that vectro

But sometimes ,a special vector's direction doesnt change it only gets stretchd or shrunk.
that special vectors is called an eigen vector , and the amount its stretched by is called the eigen value

A -> square matrix

A.v= lambda.v

v= eigen vector
lanbda=eigen vaalue
A= square matrix

'''

eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
print(eigen_values, eigen_vectors)
