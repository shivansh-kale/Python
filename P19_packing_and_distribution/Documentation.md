# Packaging and Distribution in Python

Packaging allows Python code to be distributed as reusable libraries.

Examples of packaged Python libraries include:

* NumPy
* Pandas
* FastAPI
* Scikit-learn

Packaging ensures code can be easily installed using tools like `pip`.

---

# 1. Python Package Structure

A typical Python package looks like this:

```text
my_package/
│
├── my_package/
│   ├── __init__.py
│   ├── math_utils.py
│   └── string_utils.py
│
├── tests/
│
├── pyproject.toml
├── README.md
└── LICENSE
```

Explanation:

| File             | Purpose                    |
| ---------------- | -------------------------- |
| `__init__.py`    | marks directory as package |
| `pyproject.toml` | project metadata           |
| `tests/`         | unit tests                 |
| `README.md`      | project documentation      |

---

# 2. Creating a Package

Modules are organized inside a package directory.

Example module:

```python
def add(a, b):
    return a + b
```

Usage:

```python
from my_package.math_utils import add
```

This structure allows code reuse across multiple projects.

---

# 3. The `__init__.py` File

`__init__.py` marks a folder as a Python package.

Example:

```python
from .math_utils import add
```

This allows importing directly:

```python
from my_package import add
```

---

# 4. `pyproject.toml`

Modern Python packaging uses `pyproject.toml`.

Example:

```toml
[project]
name = "my_package"
version = "0.1.0"
description = "Example Python package"
```

It defines:

* project name
* version
* dependencies
* metadata

---

# 5. Installing a Local Package

Install your package locally using:

```bash
pip install -e .
```

The `-e` flag means **editable mode**, allowing changes without reinstalling.

---

# 6. Versioning

Python packages follow **semantic versioning**.

Format:

```
MAJOR.MINOR.PATCH
```

Example:

| Version | Meaning              |
| ------- | -------------------- |
| 1.0.0   | first stable release |
| 1.1.0   | new features         |
| 1.1.1   | bug fixes            |

---

# 7. Publishing to PyPI

PyPI is the official Python package repository.

Example installation:

```bash
pip install numpy
```

Publishing steps:

1. Build package:

```bash
python -m build
```

2. Upload to PyPI:

```bash
twine upload dist/*
```

---

# Best Practices

1. Use clear project structure.
2. Maintain proper versioning.
3. Include tests and documentation.
4. Use `pyproject.toml` for modern packaging.
5. Avoid publishing unfinished packages.

---

# Summary

Packaging allows Python projects to be distributed and reused.

| Concept          | Purpose                           |
| ---------------- | --------------------------------- |
| package          | reusable Python module collection |
| `__init__.py`    | package initialization            |
| `pyproject.toml` | project metadata                  |
| pip install      | install packages                  |
| PyPI             | Python package repository         |

Understanding packaging allows developers to build **professional Python libraries and tools**.
