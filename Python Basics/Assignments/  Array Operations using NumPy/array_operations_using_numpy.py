# 1. Import numpy as np and see the version (Score 1)

import numpy as np
print("numpy version", np.__version__)

# 2. Create a numpy array containing the numbers from 1 to 10, and then reshape it to a 2x5
# matrix. (Score:1)

lst=list(range(1,11))
arr1=np.array(lst)
print(arr1)
arr2=arr1.reshape(2,5)
print(arr2, arr2.shape)

# 3. Create a numpy array containing the numbers from 1 to 20, and then extract the

lst=list(range(1,20))

# elements between the 5th and 15th index. (Score :2)
arr=np.array(lst)
print(arr[5:16])

# 4. How to compute the mean, median, standard deviation of a numpy array?Use the array
# you created above (Score 3)

print("mean :", np.mean(arr))
print("median :", np.median(arr))
print("SD :", np.std(arr))

# 5. Write a NumPy program that creates a 2D array x of shape (3, 4) and a 1D array y of
# shape (4,). Subtract y from each row of x using broadcasting. (Score : 2)

x=np.arange(12).reshape(3,4)
print(x, x.shape, x.ndim)
y=np.arange(start=2, stop=6)
print(y, y.shape, y.ndim)

print(y-x)

# Note : Score 1
# for timely submission.