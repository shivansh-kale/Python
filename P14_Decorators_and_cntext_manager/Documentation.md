# Decorators and Context Managers in Python

Decorators and context managers are advanced Python features used to **modify function behavior and manage resources efficiently**.

They are widely used in modern Python frameworks and libraries.

Examples include:

* FastAPI route decorators
* logging wrappers
* authentication middleware
* resource management

---

# 1. Decorators

A **decorator** is a function that wraps another function to modify its behavior.

Basic example:

```python
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
```

Usage:

```python
@decorator
def greet():
    print("Hello")
```

Equivalent to:

```python
greet = decorator(greet)
```

---

# 2. Decorators with Arguments

Most real-world decorators need to handle function parameters.

Example:

```python
def logger(func):

    def wrapper(*args, **kwargs):
        print("Function called")
        return func(*args, **kwargs)

    return wrapper
```

This allows the decorated function to receive arguments normally.

---

# 3. Timing Decorator

Decorators are commonly used for performance monitoring.

Example:

```python
import time

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print("Execution time:", end - start)
        return result

    return wrapper
```

---

# 4. Multiple Decorators

Functions can have multiple decorators.

Example:

```python
@decorator_one
@decorator_two
def function():
```

Execution order:

1. `decorator_two`
2. `decorator_one`

---

# 5. Context Managers

Context managers handle resource management automatically.

Common example:

```python
with open("file.txt") as f:
    data = f.read()
```

Advantages:

* automatic cleanup
* prevents resource leaks
* simpler syntax

---

# 6. Custom Context Managers

A custom context manager implements two methods:

| Method        | Purpose               |
| ------------- | --------------------- |
| `__enter__()` | runs at start         |
| `__exit__()`  | runs when block exits |

Example:

```python
class ResourceManager:

    def __enter__(self):
        print("Resource opened")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource closed")
```

---

# 7. Contextlib

The `contextlib` module simplifies creating context managers.

Example:

```python
from contextlib import contextmanager

@contextmanager
def resource():
    print("Acquire resource")
    yield
    print("Release resource")
```

Usage:

```python
with resource():
    print("Using resource")
```

---

# Real-World Usage

Decorators are used in many Python frameworks.

Example (FastAPI):

```python
@app.get("/users")
def get_users():
```

Example (Flask):

```python
@app.route("/")
def home():
```

These are decorators that modify function behavior.

---

# Summary

Decorators and context managers are powerful Python features.

| Feature            | Purpose                             |
| ------------------ | ----------------------------------- |
| decorator          | modify function behavior            |
| wrapper function   | extend functionality                |
| stacked decorators | apply multiple behaviors            |
| context manager    | manage resources automatically      |
| contextlib         | simplified context manager creation |

These patterns are widely used in **modern Python applications and frameworks**.
