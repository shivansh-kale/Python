# Asynchronous & Parallel Python

Modern Python applications often need to handle **multiple tasks simultaneously**.

Examples include:

* serving many web requests
* downloading multiple files
* processing large datasets
* running machine learning pipelines

Python provides several tools for concurrency:

* multithreading
* multiprocessing
* asynchronous programming

---

# 1. Multithreading

Multithreading allows a program to run multiple threads within the same process.

Example:

```python
import threading

thread = threading.Thread(target=task)
thread.start()
```

Threads share the same memory space.

Advantages:

* lightweight
* efficient for I/O operations

Common use cases:

* network requests
* file reading
* database operations

---

## The GIL

Python has a **Global Interpreter Lock (GIL)**.

The GIL ensures that only one thread executes Python bytecode at a time.

Because of this:

* threads are **not ideal for CPU-heavy tasks**

However, they still work well for **I/O-bound tasks**.

---

# 2. Multiprocessing

Multiprocessing creates **separate processes** instead of threads.

Example:

```python
from multiprocessing import Process

process = Process(target=compute)
process.start()
```

Advantages:

* true parallelism
* utilizes multiple CPU cores

Common use cases:

* machine learning training
* large numerical computations
* data processing pipelines

---

# 3. Asynchronous Programming

Asynchronous programming allows tasks to run **without blocking the program**.

Python uses:

* `async`
* `await`
* event loop

Example:

```python
async def task():
    await asyncio.sleep(1)
```

Tasks pause during waiting periods and allow other tasks to run.

---

# 4. Async / Await

The `async` keyword defines asynchronous functions.

Example:

```python
async def fetch_data():
    await asyncio.sleep(1)
```

The `await` keyword pauses execution until the task completes.

Multiple tasks can run concurrently using:

```python
asyncio.gather()
```

---

# 5. Async I/O

Async I/O is useful for handling many I/O operations simultaneously.

Example tasks:

* API requests
* web scraping
* database queries
* message queues

Async frameworks include:

* FastAPI
* aiohttp
* asyncio

---

# 6. Comparison

| Technique       | Best For         | Example Use  |
| --------------- | ---------------- | ------------ |
| Threading       | I/O tasks        | web requests |
| Multiprocessing | CPU tasks        | ML training  |
| Async I/O       | high concurrency | APIs         |

---

# 7. When to Use Each

Use **multithreading** when:

* tasks wait on I/O
* many network calls are made

Use **multiprocessing** when:

* tasks are CPU-heavy
* parallel computation is required

Use **async programming** when:

* many concurrent I/O tasks exist
* building scalable APIs

---

# Summary

Concurrency techniques allow Python programs to perform multiple tasks efficiently.

| Technique         | Key Idea                        |
| ----------------- | ------------------------------- |
| Multithreading    | multiple threads in one process |
| Multiprocessing   | multiple CPU processes          |
| Async programming | non-blocking concurrency        |

These tools are widely used in **modern AI systems, web servers, and data pipelines**.
