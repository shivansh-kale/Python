"""
DECORATORS AND CONTEXT MANAGERS
-------------------------------

This file covers:

1. What decorators are
2. Creating decorators
3. Decorators with arguments
4. Multiple decorators
5. Context managers
6. Creating custom context managers
7. Using contextlib

These patterns are widely used in:
- web frameworks
- logging
- performance measurement
- resource management
"""

# =========================================================
# 1. BASIC FUNCTION DECORATOR
# =========================================================

"""
A decorator is a function that wraps another function
to extend or modify its behavior.
"""

def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@simple_decorator
def greet():
    print("Hello!")


greet()


# =========================================================
# 2. DECORATORS WITH ARGUMENTS
# =========================================================

"""
Most real decorators need to accept arguments.
"""

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper


@logger
def add(a, b):
    return a + b


print(add(3, 5))


# =========================================================
# 3. DECORATOR FOR TIMING FUNCTIONS
# =========================================================

"""
Decorators are often used to measure execution time.
"""

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")

        return result
    return wrapper


@timer
def compute():
    total = sum(i * i for i in range(1_000_000))
    return total


compute()


# =========================================================
# 4. MULTIPLE DECORATORS
# =========================================================

"""
Multiple decorators can be stacked.
"""

def decorator_one(func):
    def wrapper():
        print("Decorator One")
        func()
    return wrapper


def decorator_two(func):
    def wrapper():
        print("Decorator Two")
        func()
    return wrapper


@decorator_one
@decorator_two
def say_hello():
    print("Hello World")


say_hello()


# =========================================================
# 5. CONTEXT MANAGERS
# =========================================================

"""
Context managers manage resources automatically.

Example:
with open("file.txt") as f:
"""

with open("example.txt", "w") as file:
    file.write("Hello from context manager!")


# =========================================================
# 6. CUSTOM CONTEXT MANAGER
# =========================================================

"""
Context managers use two methods:

__enter__()
__exit__()
"""

class FileManager:

    def __enter__(self):
        print("Opening resource")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing resource")


with FileManager() as manager:
    print("Using the resource")


# =========================================================
# 7. CONTEXT MANAGERS USING CONTEXTLIB
# =========================================================

"""
The contextlib module provides utilities
for creating context managers easily.
"""

from contextlib import contextmanager


@contextmanager
def managed_resource():
    print("Resource acquired")
    yield
    print("Resource released")


with managed_resource():
    print("Using resource")