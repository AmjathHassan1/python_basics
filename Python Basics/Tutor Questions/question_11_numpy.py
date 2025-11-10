# Numpy questions
#
# 1.Create a 2D array and extract:
#
import numpy as np
from numpy.ma.core import where

arr=np.array([[1,2,3,4],[5,6,7,8]])

# The first row.

print(arr[0])

# The last column.
#
print(arr[1])


# The element at 2nd row and 3rd column

print(arr[1,2])


# 2.Create two 2d arrays and perform element-wise addition, subtraction, multiplication,division and dot product.

arr1=np.array([[1,2],[5,6]])
arr2=np.array([[9,10],[13,14]])

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1.dot(arr2))

# 3.Given an array of integers, find:

arr=np.array([1,2,3,4,5,6])

# The mean, median, and standard deviation.

print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))


# The maximum and minimum values.

print(np.min(arr))
print(np.max(arr))

# 4.Create a 1D array of 12 numbers and reshape it into a 3×4 matrix.

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr.reshape(3,4))

# 5.Given a 1d array, extract all elements greater than 10.(loop through elements)

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
for i in arr:
    if i > 10:
        print(i)

print(where(arr > 10), type(where(arr > 10)),len(where(arr > 10)))
print(arr[arr>10])

# 6.Create a 3×3 NumPy array filled with zeros.

zero_33=np.zeros((3,3))
print(zero_33)

# 7.Create a 1D NumPy array of numbers from 10 to 50.

arr=np.arange(10,51)
print(arr)


# 8.create an array of all multiples of 3 from 0 to 30.and reshape that array into all possible shapes.

arr=np.arange(0,31,3)
print(arr)
print(arr[arr>10])
print(arr.reshape(1,11))
print(arr.reshape(11,1))


# 9.create a 3-d array and convert that into base (1d)

arr=np.array([[[1,2,3],[4,5,6]]])
print(arr)
print(arr.ndim)
print(arr.shape)

arr1=arr.flatten()
print(arr1)

# 10.create the array
arr=np.array([[20,30,40],[10,15,25],[35,45,50]])
#
# Extract 40

print(arr[0,-1])

# Extract  15

print(arr[1,1])

# Extract  [35,45]

print(arr[2,:2])
#
# Extract [40,25]

print(arr[:2,-1])
#
# Extract [30,15,45]

print(arr[:,1:2])

# Extract [15,25
#                 45,50]

print(arr[1:,1:])

# 11.create 2*3 array and find its transpose.

arr=np.array([[1,2,3],[4,5,6]])
print(arr.transpose())

# 12.calculate the mean of a 2d array.and explain how the mean is generated.

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.mean())



# 13.find the mean of a 2d array column wise.
print(np.mean(arr, axis=0))
