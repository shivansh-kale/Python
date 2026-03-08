# Modules, Packages & Environments in Python

As Python projects grow, writing everything in a single file becomes impractical.
Python solves this problem using **modules**, **packages**, and **environment management**.

These tools allow developers to:

* organize code into logical units
* reuse functionality across files
* manage dependencies
* isolate project environments

This section explains the complete workflow used in real Python projects.

---

# 1. Python Import System

Python provides several ways to import code from other modules.

## 1.1 Import Entire Module

The simplest way is importing the whole module.

```python
import math

print(math.sqrt(16))
print(math.pi)
```

Here:

* `math` is the module
* functions must be accessed using `module.function`.

---

## 1.2 Import Specific Objects

Instead of importing the entire module, you can import specific functions or variables.

```python
from math import sqrt, pi

print(sqrt(25))
print(pi)
```

Advantages:

* cleaner syntax
* avoids long module prefixes

---

## 1.3 Import with Alias

Aliases allow shortening module names.

```python
import math as m

print(m.sqrt(36))
```

This is very common in data science:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

---

## 1.4 Import Everything (Not Recommended)

Python allows importing everything from a module.

```python
from math import *
```

However this practice should be avoided because:

* it pollutes the namespace
* it reduces readability
* debugging becomes harder

---

# 2. Creating Your Own Modules

A **module** is simply a Python file containing reusable code.

Example file:

```text
math_utils.py
```

Example content:

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
```

This module can be used in another file.

```python
import math_utils

print(math_utils.add(2,3))
```

Benefits of modules:

* reuse code across projects
* better organization
* easier debugging

---

# 3. Packages

A **package** is a directory that contains multiple modules.

Packages allow organizing large projects.

Example project structure:

```text
project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

Explanation:

* `utils` → package
* `math_utils.py` → module
* `__init__.py` → marks the folder as a package

Import example:

```python
from utils.math_utils import add

print(add(4,5))
```

Packages help organize code into **logical components**.

---

# 4. Understanding `__name__` and `__main__`

Every Python module contains a built-in variable:

```python
__name__
```

Its value depends on how the file is executed.

| Situation               | Value of `__name__` |
| ----------------------- | ------------------- |
| File executed directly  | `"__main__"`        |
| File imported as module | module name         |

Example:

```python
def main():
    print("Program started")

if __name__ == "__main__":
    main()
```

Purpose:

* ensures code runs only when the script is executed directly
* prevents execution when the file is imported as a module

This pattern is extremely common in Python programs.

---

# 5. Python Module Search Path

When Python imports a module, it searches several locations.

Search order:

1. Current working directory
2. Python standard library
3. Installed third-party packages
4. Directories listed in `sys.path`

Example:

```python
import sys
print(sys.path)
```

Understanding the module search path helps debug **import errors**.

---

# 6. Virtual Environments

A **virtual environment** isolates dependencies for a specific project.

Without virtual environments, different projects may require different versions of the same library.

Example problem:

| Project   | Required Version |
| --------- | ---------------- |
| Project A | numpy 1.24       |
| Project B | numpy 1.20       |

Virtual environments solve this conflict.

---

## 6.1 Creating Virtual Environment (venv)

Python includes a built-in tool called `venv`.

Create environment:

```bash
python -m venv myenv
```

Activate environment:

Windows:

```bash
myenv\Scripts\activate
```

Mac/Linux:

```bash
source myenv/bin/activate
```

Deactivate environment:

```bash
deactivate
```

---

## 6.2 Conda Environments

Another popular environment manager is **Conda**.

Create environment:

```bash
conda create -n myenv python=3.11
```

Activate environment:

```bash
conda activate myenv
```

Conda is commonly used in **data science and machine learning**.

---

# 7. Dependency Management

Projects often require multiple external libraries.

Example:

* numpy
* pandas
* scikit-learn
* fastapi

Dependency management ensures all required packages are installed.

---

## 7.1 Installing Packages

Using pip:

```bash
pip install numpy
```

---

## 7.2 Listing Installed Packages

```bash
pip list
```

---

## 7.3 Creating `requirements.txt`

This file stores project dependencies.

Generate file:

```bash
pip freeze > requirements.txt
```

Example file:

```text
numpy==1.26.0
pandas==2.1.0
scikit-learn==1.3.0
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 8. Poetry (Modern Dependency Management)

Poetry is a modern dependency manager and build system.

Advantages:

* automatic dependency resolution
* lock files for reproducibility
* cleaner project management

Install Poetry:

```bash
pip install poetry
```

Create project:

```bash
poetry new my_project
```

Add dependency:

```bash
poetry add numpy
```

Poetry manages dependencies using:

```text
pyproject.toml
```

---

# 9. Best Practices

When working with modules, packages, and environments:

1. Use clear module names.
2. Avoid `import *`.
3. Organize related modules into packages.
4. Always use virtual environments.
5. Track dependencies using `requirements.txt` or Poetry.
6. Use `__name__ == "__main__"` for executable scripts.

---

# Summary

Python provides powerful tools for organizing and managing projects.

| Concept               | Purpose                                |
| --------------------- | -------------------------------------- |
| Module                | A Python file containing reusable code |
| Package               | A directory containing modules         |
| Import system         | Allows using code from other modules   |
| Virtual environment   | Isolates project dependencies          |
| Dependency management | Tracks required packages               |
| `__main__`            | Controls script execution behavior     |

Mastering these concepts is essential for building **scalable Python applications and machine learning projects**.
