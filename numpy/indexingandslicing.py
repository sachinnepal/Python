import numpy as np

# ============================
# NUMPY INDEXING & SLICING
# ============================

# Create a 1D array
arr1 = np.array([10, 20, 30, 40, 50, 60])

print("Original 1D Array:", arr1)

# ----------------------------
# 1. INDEXING (1D)
# ----------------------------

print(arr1[0])      # First element
print(arr1[2])      # Third element
print(arr1[-1])     # Last element
print(arr1[-2])     # Second last element

# ----------------------------
# 2. BASIC SLICING
# Syntax: array[start:stop:step]
# ----------------------------

print(arr1[1:4])    # Index 1 to 3
print(arr1[:3])     # Beginning to index 2
print(arr1[3:])     # Index 3 to end
print(arr1[:])      # Entire array

# ----------------------------
# 3. STEP SLICING
# ----------------------------

print(arr1[::2])    # Every 2nd element
print(arr1[1::2])   # Every 2nd element starting from index 1
print(arr1[::-1])   # Reverse array
print(arr1[::-2])   # Reverse every second element

# ----------------------------
# 4. MODIFY USING SLICING
# ----------------------------

arr1[1:4] = 99      # Replace elements with 99
print(arr1)

# Reset array
arr1 = np.array([10,20,30,40,50,60])

arr1[::2] = 0       # Replace even index values
print(arr1)


# ==================================================
# 2D ARRAY
# ==================================================

arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("\n2D Array")
print(arr2)

# ----------------------------
# 5. ROW INDEXING
# ----------------------------

print(arr2[0])      # First row
print(arr2[1])      # Second row
print(arr2[-1])     # Last row

# ----------------------------
# 6. COLUMN INDEXING
# ----------------------------

print(arr2[:,0])    # First column
print(arr2[:,1])    # Second column
print(arr2[:,2])    # Third column

# ----------------------------
# 7. SINGLE ELEMENT
# ----------------------------

print(arr2[1,2])    # Row 1, Column 2
print(arr2[2,1])    # Row 2, Column 1

# ----------------------------
# 8. ROW SLICING
# ----------------------------

print(arr2[0:2])    # First two rows
print(arr2[1:])     # Last two rows

# ----------------------------
# 9. COLUMN SLICING
# ----------------------------

print(arr2[:,0:2])  # First two columns
print(arr2[:,1:])   # Last two columns

# ----------------------------
# 10. ROW + COLUMN SLICING
# ----------------------------

print(arr2[0:2,1:3])
# Rows 0-1 and Columns 1-2

# Output:
# [[2 3]
#  [5 6]]

# ----------------------------
# 11. EVERY SECOND ROW/COLUMN
# ----------------------------

print(arr2[::2,:])      # Every second row
print(arr2[:,::2])      # Every second column
print(arr2[::2,::2])    # Every second row & column

# ----------------------------
# 12. REVERSE
# ----------------------------

print(arr2[::-1])       # Reverse rows
print(arr2[:,::-1])     # Reverse columns
print(arr2[::-1,::-1])  # Reverse entire matrix

# ----------------------------
# 13. MODIFY PART OF MATRIX
# ----------------------------

arr2[0:2,0:2] = 100
print(arr2)

# Reset
arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


# ==================================================
# 3D ARRAY
# ==================================================

arr3 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print("\n3D Array")
print(arr3)

# Shape = (2,2,2)

print(arr3[0])         # First 2D block
print(arr3[1])         # Second block

print(arr3[0,1])       # Second row of first block

print(arr3[1,0,1])     # Block1 Row0 Col1 = 6

print(arr3[:,:,0])     # First column from every block


# ==================================================
# FANCY INDEXING
# ==================================================

arr = np.array([10,20,30,40,50])

print("\nFancy Indexing")

print(arr[[0,2,4]])    # Select multiple indexes

arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr2[[0,2]])     # Select row 0 and row 2

print(arr2[:,[0,2]])   # Select first & third columns


# ==================================================
# BOOLEAN INDEXING
# ==================================================

arr = np.array([5,10,15,20,25,30])

print("\nBoolean Indexing")

print(arr > 15)         # Returns True/False

print(arr[arr > 15])    # Values greater than 15

print(arr[arr % 2 == 0])    # Even numbers

print(arr[arr != 20])       # Everything except 20


# ==================================================
# SUMMARY
# ==================================================

# arr[start:stop]
# arr[start:stop:step]
# arr[::-1]              -> Reverse
# arr[:,1]               -> Column
# arr[1,:]               -> Row
# arr[1,2]               -> Single value
# arr[[0,2]]             -> Fancy indexing
# arr[arr>10]            -> Boolean indexing