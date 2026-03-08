"""
PACKAGING AND DISTRIBUTION IN PYTHON
------------------------------------

This file explains how Python projects can be packaged
and distributed as installable libraries.

Topics covered:

1. Python project structure
2. Creating a package
3. Using __init__.py
4. pyproject.toml
5. Installing local packages
6. Versioning
7. Publishing to PyPI
"""

# =========================================================
# 1. BASIC PROJECT STRUCTURE
# =========================================================

"""
Typical Python package structure:

my_package/
│
├── my_package/
│   ├── __init__.py
│   ├── math_utils.py
│   └── string_utils.py
│
├── tests/
│   └── test_math_utils.py
│
├── pyproject.toml
├── README.md
└── LICENSE
"""

print("Python packages organize reusable code.")


# =========================================================
# 2. CREATING A MODULE
# =========================================================

"""
Example module inside package:

math_utils.py
"""

def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


print(add(2, 3))


# =========================================================
# 3. __init__.py
# =========================================================

"""
__init__.py marks a directory as a Python package.

Example:

my_package/
    __init__.py
    math_utils.py

Inside __init__.py we can expose functions.
"""

# Example import style
# from my_package.math_utils import add


# =========================================================
# 4. PYPROJECT.TOML
# =========================================================

"""
Modern Python packaging uses pyproject.toml.

Example pyproject.toml:

[project]
name = "my_package"
version = "0.1.0"
description = "Example Python package"
authors = [{name="Your Name"}]

dependencies = [
    "numpy",
    "pandas"
]
"""

print("pyproject.toml defines project metadata.")


# =========================================================
# 5. INSTALLING LOCAL PACKAGE
# =========================================================

"""
Install local package using pip:

pip install -e .

The -e flag installs the package in editable mode.
"""


# =========================================================
# 6. VERSIONING
# =========================================================

"""
Python packages follow semantic versioning.

Format:

MAJOR.MINOR.PATCH

Example:

1.0.0
"""

version = "1.0.0"

print("Package version:", version)


# =========================================================
# 7. PUBLISHING TO PYPI
# =========================================================

"""
Steps to publish package:

1. Build distribution
2. Upload to PyPI
"""

"""
Build package:

python -m build
"""

"""
Upload package:

pip install twine
twine upload dist/*
"""

print("Package ready for distribution.")