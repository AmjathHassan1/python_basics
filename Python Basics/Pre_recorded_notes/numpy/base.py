import numpy as np
arr=np.array([1,2,3,4,5])  # one dimensional array
print(arr)

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)

arr=np.arange(1,10,2)
print(arr)

zeros_array=np.zeros((3, 3))
print(zeros_array)

ones_array=np.ones((3, 3))
print(ones_array)

identity_matrix=np.eye(3)
print(identity_matrix)


a=np.array([1,2,3])
b=np.array([4,5,6])

print(a+b) # addition
print(a-b) # substraction
print(a*b) # Element wise multiplication
print(a/b)  # element-wise division

# Mathematical Functions
print(np.sqrt(a))
print(np.exp(a))
print(np.log(a))
print(np.sin(a))

# Aggreagate Function

print(np.sum(a))
print(np.mean(a))
print(np.median(a))
print(np.std(a))
print(np.var(a))
print(np.max(a))
print(np.min(a))


# Indexing and Slicing

arr=np.array([1,2,3,4,5])
print(arr[0])
print(arr[-1])

# Slicing
print(arr[1:3])
print(arr[:3])
print(arr[::2])

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)
print(arr_2d[1,2])
print(arr_2d[:,1])


arr=np.array([1,2,3,4,5,6])
print(arr)
reshape_arr=np.reshape(arr,(3,2))
print(reshape_arr)


arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)
print(arr_2d.T)

# Spliting
arr=np.array([1,2,3,4,5,6])
print(np.split(arr,3))

# Copy

arr=np.array([1,2,3,4,5,6])
arr_copy=arr.copy()
print(arr)
arr_copy[0]=91
print(arr_copy)


arr=np.array([1,2,3,4,5,6])
arr_copy=arr.view()

arr_copy[0]=91
print(arr)
print(arr_copy)




