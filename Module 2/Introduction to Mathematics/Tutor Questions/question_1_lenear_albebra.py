# Linear algebra questions.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#
# 1.create this matrix
#   A=[4    5
#      6     7]

matrix=np.array([[4,5], [6,7]])
print(matrix)
print(type(matrix))
print(matrix.shape)

# 2.find transpose of A

matrix_t = matrix.transpose()

print(matrix_t)

# 3.find determinant if A

det = np.linalg.det(matrix)
print(det)

# 4.multiply A with a scalar 5

print(5 * matrix)


# 5.check if the matrix is singular or non singular

def check_singular(matrix):
    if np.linalg.det(matrix) != 0:
        return False
    else:
        return True

print(check_singular(matrix))

# 6.find eigen values,eigen vectors.

eig_values, eig_vectors = np.linalg.eig(matrix)
print(eig_values, eig_vectors)

# 7.create a 3*3 matrix with random values

matrix = np.random.rand(3, 3)
print(matrix)

# 8.find it's determinant

det=np.linalg.det(matrix)
print(det)