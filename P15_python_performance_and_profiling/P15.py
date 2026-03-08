"""
PYTHON PERFORMANCE AND PROFILING
--------------------------------

This file covers techniques for analyzing and improving
Python program performance.

Topics covered:

1. Why profiling matters
2. Measuring execution time (time module)
3. timeit module
4. cProfile
5. Memory considerations
6. Vectorization vs loops
7. Basic optimization strategies
"""

# =========================================================
# 1. MEASURING EXECUTION TIME (TIME MODULE)
# =========================================================

"""
The time module allows measuring execution duration.
"""

import time

start = time.time()

total = 0
for i in range(1_000_000):
    total += i

end = time.time()

print("Execution time:", end - start)


# =========================================================
# 2. TIMEIT MODULE
# =========================================================

"""
The timeit module is the recommended way to measure
small code snippets.
"""

import timeit

execution_time = timeit.timeit(
    stmt="sum(range(1000))",
    number=10000
)

print("Timeit result:", execution_time)


# =========================================================
# 3. PROFILING WITH CPROFILE
# =========================================================

"""
cProfile analyzes how long functions take to execute.
"""

import cProfile


def slow_function():
    total = 0
    for i in range(1_000_000):
        total += i
    return total


cProfile.run("slow_function()")


# =========================================================
# 4. MEMORY CONSIDERATIONS
# =========================================================

"""
Memory usage affects performance significantly.
Using generators instead of lists can reduce memory usage.
"""

# List example
numbers_list = [i for i in range(1_000_000)]

# Generator example
numbers_generator = (i for i in range(1_000_000))

print("List example created")
print("Generator example created")


# =========================================================
# 5. NUMPY VECTORIZATION VS LOOPS
# =========================================================

"""
Vectorized operations are significantly faster than Python loops.
"""

import numpy as np

# Python loop
start = time.time()

result = []
for i in range(1_000_000):
    result.append(i * 2)

end = time.time()

print("Loop time:", end - start)


# NumPy vectorization
arr = np.arange(1_000_000)

start = time.time()

vectorized_result = arr * 2

end = time.time()

print("Vectorized time:", end - start)


# =========================================================
# 6. BASIC OPTIMIZATION STRATEGIES
# =========================================================

"""
General strategies to improve Python performance:

1. Use built-in functions (faster than manual loops)
2. Use NumPy for numerical operations
3. Avoid unnecessary object creation
4. Use generators for large datasets
5. Profile before optimizing
"""

# Example: using built-in sum instead of loop

numbers = list(range(1_000_000))

start = time.time()
total = sum(numbers)
end = time.time()

print("Built-in sum time:", end - start)