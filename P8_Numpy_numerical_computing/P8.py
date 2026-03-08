"""
NUMERICAL COMPUTING WITH NUMPY
------------------------------

NumPy (Numerical Python) is the core library for numerical computing in Python.

It provides:
- fast multidimensional arrays
- vectorized mathematical operations
- linear algebra tools
- random sampling utilities

NumPy is the foundation for:
- machine learning
- data science
- scientific computing
"""

import numpy as np


# =========================================================
# 1. CREATING NUMPY ARRAYS
# =========================================================

"""
NumPy arrays are called ndarrays.

They are similar to Python lists but:
- much faster
- support vectorized operations
- store elements in contiguous memory
"""

# Creating array from list
arr = np.array([1, 2, 3, 4])

print(arr)

# Creating 2D array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(matrix)


# =========================================================
# 2. ARRAY SHAPE AND DIMENSIONS
# =========================================================

"""
shape -> dimensions of the array
ndim  -> number of dimensions
size  -> total number of elements
"""

print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Total elements:", matrix.size)


# =========================================================
# 3. DATA TYPES (dtype)
# =========================================================

"""
NumPy arrays store elements with fixed data types.
"""

arr = np.array([1, 2, 3], dtype=np.float64)

print(arr.dtype)

# Convert dtype
arr = arr.astype(np.int32)

print(arr)


# =========================================================
# 4. ARRAY CREATION FUNCTIONS
# =========================================================

# zeros
zeros = np.zeros((2, 3))

print(zeros)

# ones
ones = np.ones((3, 3))

print(ones)

# range
range_arr = np.arange(0, 10, 2)

print(range_arr)

# evenly spaced values
linspace = np.linspace(0, 1, 5)

print(linspace)


# =========================================================
# 5. BROADCASTING
# =========================================================

"""
Broadcasting allows NumPy to perform operations
between arrays of different shapes.
"""

arr = np.array([1, 2, 3])

result = arr + 10

print(result)


# Broadcasting with 2D arrays
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(matrix + arr)


# =========================================================
# 6. VECTORIZED OPERATIONS
# =========================================================

"""
Vectorization means performing operations on entire arrays
without explicit loops.
"""

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a * b)
print(a ** 2)


# Mathematical functions
print(np.sqrt(a))
print(np.exp(a))
print(np.mean(a))


# =========================================================
# 7. LINEAR ALGEBRA BASICS
# =========================================================

"""
Linear algebra is fundamental for machine learning.
"""

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Matrix multiplication
print(np.dot(A, B))

# Determinant
print(np.linalg.det(A))

# Inverse
print(np.linalg.inv(A))

# Eigenvalues
print(np.linalg.eig(A))


# =========================================================
# 8. RANDOM SAMPLING
# =========================================================

"""
Random number generation is used in:
- ML model initialization
- simulations
- stochastic algorithms
"""

# Random numbers
print(np.random.rand(3))

# Random integers
print(np.random.randint(0, 10, size=5))

# Normal distribution
print(np.random.normal(0, 1, 5))

# Random choice
choices = np.random.choice([1, 2, 3, 4], size=5)

print(choices)


# Set random seed (important for reproducibility)
np.random.seed(42)

print(np.random.rand(3))