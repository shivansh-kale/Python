# Numerical Computing with NumPy

NumPy (Numerical Python) is the core library for numerical computing in Python.

It provides efficient tools for:

* multidimensional arrays
* mathematical operations
* linear algebra
* random number generation

Most machine learning libraries are built on top of NumPy.

Examples include:

* Pandas
* Scikit-learn
* TensorFlow
* PyTorch

---

# 1. NumPy Arrays

The central object in NumPy is the **ndarray (N-dimensional array)**.

Example:

```python
import numpy as np

arr = np.array([1,2,3])
```

Compared to Python lists, NumPy arrays are:

| Feature     | Python List | NumPy Array |
| ----------- | ----------- | ----------- |
| Speed       | slower      | much faster |
| Memory      | inefficient | optimized   |
| Vector math | limited     | built-in    |

---

# 2. Array Shape and Dimensions

NumPy arrays have several important attributes.

Example:

```python
matrix = np.array([[1,2,3],[4,5,6]])
```

Attributes:

| Attribute | Description          |
| --------- | -------------------- |
| shape     | dimensions of array  |
| ndim      | number of dimensions |
| size      | total elements       |

Example:

```python
matrix.shape
matrix.ndim
matrix.size
```

---

# 3. Data Types (dtype)

NumPy arrays store elements with fixed types.

Example:

```python
arr = np.array([1,2,3], dtype=np.float64)
```

Common NumPy data types:

| Type    | Meaning        |
| ------- | -------------- |
| int32   | integer        |
| float64 | floating point |
| bool    | boolean        |

Convert type:

```python
arr.astype(np.int32)
```

---

# 4. Array Creation Functions

NumPy provides several functions for creating arrays.

Examples:

```python
np.zeros((2,3))
np.ones((3,3))
np.arange(0,10,2)
np.linspace(0,1,5)
```

Explanation:

| Function | Purpose                 |
| -------- | ----------------------- |
| zeros    | array filled with zeros |
| ones     | array filled with ones  |
| arange   | range of values         |
| linspace | evenly spaced numbers   |

---

# 5. Broadcasting

Broadcasting allows operations between arrays of different shapes.

Example:

```python
arr = np.array([1,2,3])
arr + 10
```

Output:

```
[11 12 13]
```

NumPy automatically expands the scalar value.

Broadcasting enables efficient operations without loops.

---

# 6. Vectorized Operations

Vectorization means applying operations to entire arrays at once.

Example:

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

a + b
a * b
```

Advantages:

* faster computation
* cleaner code
* optimized memory usage

---

# 7. Linear Algebra Basics

Linear algebra is fundamental to machine learning algorithms.

Example matrices:

```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
```

Common operations:

| Operation             | Function           |
| --------------------- | ------------------ |
| Matrix multiplication | `np.dot(A,B)`      |
| Determinant           | `np.linalg.det(A)` |
| Matrix inverse        | `np.linalg.inv(A)` |
| Eigenvalues           | `np.linalg.eig(A)` |

These operations appear in algorithms such as:

* linear regression
* PCA
* neural networks

---

# 8. Random Sampling

Random numbers are widely used in machine learning.

Examples include:

* model initialization
* train/test splitting
* stochastic gradient descent

NumPy provides a random module.

Examples:

```python
np.random.rand(3)
np.random.randint(0,10,5)
np.random.normal(0,1,5)
```

---

## Random Seed

Setting a seed ensures reproducible results.

Example:

```python
np.random.seed(42)
```

This ensures the same random values are generated every time the code runs.

---

# Summary

NumPy is the foundation of numerical computing in Python.

| Concept         | Purpose                            |
| --------------- | ---------------------------------- |
| ndarray         | efficient multidimensional arrays  |
| shape & dtype   | array structure and data type      |
| broadcasting    | operations across different shapes |
| vectorization   | fast array computations            |
| linear algebra  | matrix operations                  |
| random sampling | probabilistic algorithms           |

Understanding NumPy is essential before learning:

* Pandas
* machine learning algorithms
* deep learning frameworks
