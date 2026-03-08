# Python Performance and Profiling

Performance optimization becomes important when working with:

* large datasets
* machine learning pipelines
* high-performance applications
* real-time systems

Before optimizing code, developers should **measure performance using profiling tools**.

---

# 1. Measuring Execution Time

The simplest way to measure execution time is using the `time` module.

Example:

```python
import time

start = time.time()

# code to measure

end = time.time()

print(end - start)
```

This method is useful for measuring **large code sections**.

---

# 2. Using the `timeit` Module

`timeit` is designed for accurate benchmarking of small code snippets.

Example:

```python
import timeit

timeit.timeit("sum(range(1000))", number=10000)
```

Advantages of `timeit`:

* more precise measurements
* avoids system noise
* designed for benchmarking

---

# 3. Profiling with cProfile

`cProfile` helps identify performance bottlenecks in programs.

Example:

```python
import cProfile

cProfile.run("function_name()")
```

Output shows:

* number of function calls
* total execution time
* time spent in each function

This helps locate **slow parts of the code**.

---

# 4. Memory Considerations

Memory usage can significantly affect performance.

Example:

List:

```python
numbers = [i for i in range(1_000_000)]
```

Generator:

```python
numbers = (i for i in range(1_000_000))
```

Generators are more memory efficient because they produce values **on demand**.

---

# 5. Vectorization

Vectorization means performing operations on entire arrays instead of loops.

Example using NumPy:

```python
arr = np.arange(1000000)
arr * 2
```

Advantages:

* faster execution
* optimized C implementation
* reduced Python overhead

Vectorization is heavily used in:

* NumPy
* Pandas
* machine learning algorithms

---

# 6. Optimization Strategies

Some common strategies to improve Python performance:

1. Use built-in functions.
2. Avoid unnecessary loops.
3. Use vectorized operations.
4. Use generators for large datasets.
5. Avoid premature optimization.
6. Profile before optimizing.

---

# 7. Common Performance Tools

| Tool            | Purpose               |
| --------------- | --------------------- |
| time            | simple timing         |
| timeit          | accurate benchmarking |
| cProfile        | performance profiling |
| line_profiler   | line-level profiling  |
| memory_profiler | memory usage tracking |

---

# Summary

Performance optimization helps improve efficiency of Python programs.

| Concept       | Purpose                          |
| ------------- | -------------------------------- |
| time          | measure execution time           |
| timeit        | benchmark small code snippets    |
| cProfile      | identify performance bottlenecks |
| generators    | memory-efficient iteration       |
| vectorization | faster numerical computation     |

These techniques are especially useful in **data science and machine learning workflows**.
