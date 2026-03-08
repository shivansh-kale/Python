"""
ASYNCHRONOUS & PARALLEL PYTHON
------------------------------

Modern Python applications often need to handle multiple tasks efficiently.

This file covers:

1. Multithreading
2. Multiprocessing
3. async / await
4. Async I/O
5. When to use each technique

These techniques are used in:
- web servers
- machine learning pipelines
- data processing systems
"""

# =========================================================
# 1. MULTITHREADING
# =========================================================

"""
Multithreading allows multiple threads to run concurrently
within the same process.

Threads share memory.

Best suited for:
I/O-bound tasks (network requests, file reading).
"""

import threading
import time


def task(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} finished")


t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Threads completed")


# =========================================================
# 2. MULTIPROCESSING
# =========================================================

"""
Multiprocessing uses multiple CPU processes.

Each process has its own memory space.

Best suited for:
CPU-bound tasks (heavy computation).
"""

from multiprocessing import Process


def compute():
    print("Process starting")
    total = sum(i * i for i in range(10_000_000))
    print("Process finished:", total)


p = Process(target=compute)

p.start()
p.join()


# =========================================================
# 3. ASYNC / AWAIT
# =========================================================

"""
async / await enables asynchronous programming.

It allows programs to perform other tasks while waiting
for slow operations like network calls.
"""

import asyncio


async def async_task(name):
    print(f"Task {name} started")
    await asyncio.sleep(2)
    print(f"Task {name} finished")


async def main():
    await asyncio.gather(
        async_task("A"),
        async_task("B")
    )


asyncio.run(main())


# =========================================================
# 4. ASYNC I/O BASICS
# =========================================================

"""
Async I/O is useful when performing many I/O operations
such as API requests or database calls.
"""


async def fetch_data(id):
    print(f"Fetching data {id}")
    await asyncio.sleep(1)
    return f"Data {id}"


async def fetch_all():
    tasks = [fetch_data(i) for i in range(5)]

    results = await asyncio.gather(*tasks)

    print(results)


asyncio.run(fetch_all())


# =========================================================
# 5. WHEN TO USE EACH
# =========================================================

"""
Threading
---------
Best for I/O-bound tasks:
- file operations
- web requests
- database queries

Multiprocessing
---------------
Best for CPU-bound tasks:
- numerical computations
- machine learning training
- image processing

Async / Await
-------------
Best for high-concurrency I/O:
- web APIs
- chat servers
- web scraping
"""