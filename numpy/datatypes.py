import numpy as np


# ============================================
# NumPy automatically determines the dtype
# ============================================

# The array contains integers AND a decimal number (3.1).
# NumPy needs all elements to have a compatible data type.
#
# Because 3.1 is a float, NumPy converts the integers
# to floats as well.

arr = np.array([1, 2, 3.1, 4, 5, 6])

print(arr.dtype)

# Output:
# float64
#
# The array actually becomes:
# [1.  2.  3.1  4.  5.  6.]


# ============================================
# Mixed data types
# ============================================

# This list contains:
# "string" → string
# 1, 2, 3 → integers
# 4.5 → float

lst = ["string", 1, 2, 3, 4.5]

arr1 = np.array(lst)

print(arr1.dtype)

# Output will typically be:
# <U21
#
# NumPy converts everything into strings because
# the array contains a string.
#
# For example:
# ["string", "1", "2", "3", "4.5"]


# ============================================
# Specifying dtype while creating an array
# ============================================

# Normally NumPy chooses the dtype automatically.
#
# Here we explicitly tell NumPy:
# "Store these numbers as float32."

arr2 = np.array(
    [1, 2, 3, 4, 5],
    dtype=np.float32
)

print(arr2.dtype)

# Output:
# float32


# ============================================
# Converting dtype using astype()
# ============================================

# First create a normal integer array.

arr2 = np.array([1, 2, 3, 4, 5])

# Convert the array to float64.
#
# astype() creates a NEW array with the
# requested data type.

newarr2 = arr2.astype(np.float64)

print(newarr2.dtype)

# Output:
# float64