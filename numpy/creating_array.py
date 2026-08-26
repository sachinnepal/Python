import numpy as np


# ============================================
# 1D ARRAY
# ============================================

# Creating a 1-dimensional NumPy array
array = np.array([1, 2, 3])

# ndim tells us the number of dimensions
print(array.ndim)       # Output: 1


# ============================================
# 0D ARRAY
# ============================================

# A single value is called a scalar
# A scalar has 0 dimensions
array1 = np.array(30)

print(array1.ndim)      # Output: 0


# ============================================
# 3D ARRAY
# ============================================

# Creating a 3-dimensional array
array2 = np.array([[[]]])

print(array2.ndim)      # Output: 3

# shape tells us the size along each dimension
print(array2.shape)     # Output: (1, 1, 0)


# ============================================
# np.arange()
# ============================================

# np.arange(start, stop, step)
#
# start = 1
# stop = 10
# step = 2
#
# stop value is NOT included

array4 = np.arange(1, 10, 2)

print(array4)

# Output:
# [1 3 5 7 9]


# ============================================
# np.linspace()
# ============================================

# np.linspace(start, stop, number_of_values)
#
# Creates equally spaced values
# from 0 to 1
# and generates exactly 5 values.

array5 = np.linspace(0, 1, 5)

print(array5)

# Output:
# [0.   0.25 0.5  0.75 1.  ]


# ============================================
# np.logspace()
# ============================================

# np.logspace(start, stop, number_of_values)
#
# Uses powers of 10.
#
# 10^1 = 10
# 10^2 = 100
# 10^3 = 1000

array6 = np.logspace(1, 3, 3)

print(array6)

# Output:
# [10. 100. 1000.]


# ============================================
# np.zeros()
# ============================================

# Creates an array filled with zeros.
#
# zeros(5)
# means:
# create 5 zeros

array7 = np.zeros(5)

print(array7)

# Output:
# [0. 0. 0. 0. 0.]


# ============================================
# 2D ARRAY USING np.zeros()
# ============================================

# zeros([rows, columns])
#
# [2, 3] means:
# 2 rows
# 3 columns

array8 = np.zeros([2, 3])

print(array8)

# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]


# ============================================
# np.ones()
# ============================================

# Creates an array filled with ones.
#
# [2, 3] = 2 rows and 3 columns
#
# dtype=int changes the values from
# floating-point numbers to integers.

array9 = np.ones([2, 3], dtype=int)

print(array9)

# Output:
# [[1 1 1]
#  [1 1 1]]


# ============================================
# np.full()
# ============================================

# Creates an array filled with a specific value.
#
# full(shape, value)
#
# 10 = number of elements
# 2 = value to fill them with

array10 = np.full(10, 2)

print(array10)

# Output:
# [2 2 2 2 2 2 2 2 2 2]


# ============================================
# 2D ARRAY USING np.full()
# ============================================

# [2, 4] means:
# 2 rows
# 4 columns
#
# Every element will be 7.

array11 = np.full([2, 4], 7)

print(array11)

# Output:
# [[7 7 7 7]
#  [7 7 7 7]]


# ============================================
# np.empty()
# ============================================

# Creates an array with the requested shape
# WITHOUT initializing its values.
#
# The values you see are whatever data happened
# to already exist in that memory location.
#
# Therefore, DO NOT expect zeros here.

array12 = np.empty([2, 3])

print(array12)

# Output will contain unpredictable values.

# ============================================
# np.random.rand()
# ============================================

# Generates random numbers between 0 and 1.
#
# rand(10)
# → creates 10 random numbers
#
# The values are:
# 0 <= value < 1

array13 = np.random.rand(10)

print(array13)

# Example output:
# [0.42 0.81 0.13 0.67 0.29 0.91 0.05 0.34 0.73 0.18]


# ============================================
# np.random.rand() - 2D
# ============================================

# rand(3, 3)
#
# Creates:
# 3 rows
# 3 columns
#
# Every value is between 0 and 1.

array14 = np.random.rand(3, 3)

print(array14)

# Example:
#
# [[0.12 0.54 0.72]
#  [0.91 0.23 0.44]
#  [0.35 0.81 0.17]]


# ============================================
# np.random.randn()
# ============================================

# randn() generates random numbers
# from a STANDARD NORMAL DISTRIBUTION.
#
# Mean ≈ 0
# Standard deviation ≈ 1
#
# Values can be positive OR negative.

array15 = np.random.randn(2, 3)

print(array15)

# Example:
#
# [[ 0.42 -1.21  0.35]
#  [-0.72  1.54 -0.18]]


# ============================================
# np.random.randint()
# ============================================

# randint(low, high, size)
#
# Generates RANDOM INTEGER values.
#
# 10 = minimum value (included)
# 100 = maximum value (NOT included)
#
# size=(2,3)
# → 2 rows
# → 3 columns

array15 = np.random.randint(10, 100, size=(2, 3))

print(array15)

# Example:
#
# [[45 78 12]
#  [91 34 67]]