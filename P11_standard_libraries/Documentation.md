# Python Standard Library (High-ROI Modules)

Python includes a powerful **standard library** that provides many useful tools without requiring external packages.

These modules help with:

* filesystem management
* system interaction
* date and time handling
* mathematical operations
* randomness
* logging and debugging

Learning these modules significantly increases productivity.

---

# 1. OS Module

The `os` module provides functions to interact with the operating system.

Example:

```python
import os

os.getcwd()
os.listdir()
```

Common functions:

| Function        | Purpose                       |
| --------------- | ----------------------------- |
| `os.getcwd()`   | get current working directory |
| `os.listdir()`  | list files in directory       |
| `os.makedirs()` | create directory              |

Example:

```python
os.makedirs("data_folder", exist_ok=True)
```

---

# 2. SYS Module

The `sys` module interacts with the Python interpreter.

Example:

```python
import sys

print(sys.version)
```

Useful attributes:

| Attribute     | Purpose                |
| ------------- | ---------------------- |
| `sys.version` | Python version         |
| `sys.argv`    | command line arguments |
| `sys.path`    | module search paths    |

---

# 3. Pathlib

`pathlib` provides a modern way to handle filesystem paths.

Example:

```python
from pathlib import Path

path = Path("data.txt")
```

Common operations:

```python
path.exists()
path.name
path.resolve()
```

Advantages:

* object-oriented interface
* cross-platform compatibility
* cleaner syntax than `os.path`

---

# 4. Datetime Module

The `datetime` module is used for working with dates and times.

Example:

```python
from datetime import datetime

now = datetime.now()
```

Common uses:

* timestamps
* scheduling tasks
* logging events
* time-series analysis

Date formatting example:

```python
now.strftime("%Y-%m-%d %H:%M:%S")
```

---

# 5. Time Module

The `time` module provides lower-level time functions.

Example:

```python
import time

time.time()
```

Useful functions:

| Function       | Purpose           |
| -------------- | ----------------- |
| `time.time()`  | current timestamp |
| `time.sleep()` | pause execution   |

Example:

```python
time.sleep(2)
```

---

# 6. Math Module

The `math` module provides mathematical functions.

Example:

```python
import math

math.sqrt(16)
math.factorial(5)
math.pi
```

Common functions:

| Function         | Purpose      |
| ---------------- | ------------ |
| `sqrt()`         | square root  |
| `factorial()`    | factorial    |
| `sin()`, `cos()` | trigonometry |

---

# 7. Random Module

The `random` module generates pseudo-random numbers.

Example:

```python
import random

random.randint(1,10)
```

Common functions:

| Function    | Purpose        |
| ----------- | -------------- |
| `random()`  | random float   |
| `randint()` | random integer |
| `choice()`  | random element |
| `shuffle()` | shuffle list   |

Random numbers are used in:

* simulations
* sampling
* machine learning experiments

---

# 8. Logging Module

Logging tracks events that occur during program execution.

Example:

```python
import logging

logging.info("Application started")
```

Logging levels:

| Level    | Purpose                        |
| -------- | ------------------------------ |
| DEBUG    | detailed debugging information |
| INFO     | general events                 |
| WARNING  | potential issues               |
| ERROR    | error occurred                 |
| CRITICAL | severe failure                 |

Logging is essential for:

* debugging
* monitoring applications
* production systems

---

# Summary

The Python standard library provides many essential tools.

| Module   | Purpose                      |
| -------- | ---------------------------- |
| os       | operating system interaction |
| sys      | Python runtime environment   |
| pathlib  | filesystem paths             |
| datetime | working with dates and times |
| time     | timestamps and delays        |
| math     | mathematical functions       |
| random   | random number generation     |
| logging  | application logging          |

These modules are commonly used in **data science, backend development, and machine learning workflows**.
