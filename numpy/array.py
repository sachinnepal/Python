import numpy as np

# Create a 2-dimensional NumPy array
# 2 rows and 3 columns
arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# Print the complete array
print(arr)

# ndim = number of dimensions
# This array has 2 dimensions (rows and columns)
print(arr.ndim)

# shape = tells us the number of rows and columns
# (2, 3) means 2 rows and 3 columns
print(arr.shape)

# size = total number of elements in the array
# 2 × 3 = 6 elements
print(arr.size)

# itemsize = size of each element in bytes
# For int64, each element normally takes 8 bytes
print(arr.itemsize)


# Create a 1-dimensional array
arr1 = np.array([1, 2, 3, 4, 5, 6])


# Reshape the array into 2 rows and 3 columns
#
# Original:
# [1 2 3 4 5 6]
#
# After reshape:
# [[1 2 3]
#  [4 5 6]]
#
# NOTE: You are using 'arr' here, not 'arr1'
reshaped = arr.reshape(2, 3)

print(reshaped)


# Reshape the 2×3 array into 3×2
#
# Before:
# [[1 2 3]
#  [4 5 6]]
#
# After:
# [[1 2]
#  [3 4]
#  [5 6]]
reshaped1 = reshaped.reshape(3, 2)

print(reshaped1)


# ravel() converts a multi-dimensional array into a 1D array
#
# Before:
# [[1 2]
#  [3 4]
#  [5 6]]
#
# After:
# [1 2 3 4 5 6]
#
# IMPORTANT:
# ravel() usually returns a VIEW of the original array,
# so changing 'revel' can also change 'reshaped1'.
revel = reshaped1.ravel()

print(revel)


# Change the first element of the ravel array
# 1 becomes 10
revel[0] = 10


# Because ravel() usually gives a VIEW,
# reshaped1 is also changed.
#
# reshaped1 becomes:
# [[10  2]
#  [ 3  4]
#  [ 5  6]]


# flatten() converts the array into a 1D array
#
# IMPORTANT:
# flatten() creates a COPY of the array.
# Therefore, changes made to 'flat' will NOT affect reshaped1.
flat = reshaped1.flatten()

print(flat)