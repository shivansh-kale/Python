"""
MODULES, PACKAGES, AND ENVIRONMENTS IN PYTHON
---------------------------------------------

This file explains how Python projects are structured and managed.

Topics covered:

1. Import system (import, from, as)
2. Creating modules
3. Creating packages
4. Virtual environments (venv, conda)
5. Dependency management (pip, requirements.txt, poetry)
6. Understanding __main__

Understanding these topics is essential for building
real-world Python applications and machine learning projects.
"""

# =========================================================
# 1. IMPORT SYSTEM
# =========================================================

"""
Python allows importing functionality from other modules.

Common import styles:

1. import module
2. from module import object
3. import module as alias
"""

# Example: importing entire module
import math

print("Square root:", math.sqrt(16))
print("Value of PI:", math.pi)


# Import specific objects
from math import sqrt, pi

print("Square root:", sqrt(25))
print("PI:", pi)


# Import with alias
import math as m

print("Using alias:", m.sqrt(36))


# =========================================================
# 2. CREATING YOUR OWN MODULE
# =========================================================

"""
A module is simply a Python file containing functions, classes,
or variables that can be reused in other programs.

Example:

math_utils.py

----------------
def add(a,b):
    return a+b

def multiply(a,b):
    return a*b
----------------

You can import this module into another file.
"""

# Example usage (if math_utils.py exists)

# import math_utils
# print(math_utils.add(2,3))


# =========================================================
# 3. CREATING PACKAGES
# =========================================================

"""
A package is a folder that contains multiple modules.

Example project structure:

project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py

__init__.py marks the directory as a Python package.
"""

# Example import from package

# from utils.math_utils import add
# print(add(3,4))


# =========================================================
# 4. UNDERSTANDING __name__ AND __main__
# =========================================================

"""
Every Python file contains a special variable called __name__.

If the file is run directly:
__name__ = "__main__"

If the file is imported:
__name__ = module_name
"""


def greet():
    print("Hello from the module!")


def main():
    print("Running this file directly")
    greet()


# This ensures the code runs only when the script
# is executed directly, not when imported.
if __name__ == "__main__":
    main()


# =========================================================
# 5. PYTHON MODULE SEARCH PATH
# =========================================================

"""
When Python imports modules, it searches in several locations:

1. Current directory
2. Installed packages
3. Python standard library
4. Paths defined in sys.path
"""

import sys

print("Module search paths:")
print(sys.path)


# =========================================================
# 6. VIRTUAL ENVIRONMENTS
# =========================================================

"""
Virtual environments isolate project dependencies.

Without virtual environments, package conflicts occur between projects.

Example:

Project A → numpy 1.24
Project B → numpy 1.20

Virtual environments allow each project to use its own dependencies.
"""

"""
Creating virtual environment with venv:

python -m venv myenv
"""

"""
Activate environment:

Windows:
myenv\\Scripts\\activate

Mac/Linux:
source myenv/bin/activate
"""

"""
Deactivate environment:

deactivate
"""

"""
Conda environment example:

conda create -n myenv python=3.11
conda activate myenv
"""


# =========================================================
# 7. DEPENDENCY MANAGEMENT
# =========================================================

"""
Dependency management ensures all required packages
are installed for a project.
"""

"""
Install package using pip:

pip install numpy
"""

"""
List installed packages:

pip list
"""

"""
Save dependencies to file:

pip freeze > requirements.txt
"""

"""
Install dependencies from file:

pip install -r requirements.txt
"""


# =========================================================
# 8. POETRY (MODERN DEPENDENCY MANAGER)
# =========================================================

"""
Poetry is a modern tool for dependency management.

Advantages:
- automatic dependency resolution
- lock files
- project packaging
"""

"""
Install poetry:

pip install poetry
"""

"""
Create project:

poetry new my_project
"""

"""
Add dependency:

poetry add numpy
"""


# =========================================================
# BEST PRACTICES
# =========================================================

"""
Best practices for modules and packages:

1. Keep modules focused on one responsibility
2. Use clear and descriptive names
3. Avoid 'import *'
4. Organize related modules into packages
5. Use virtual environments for every project
6. Maintain dependencies using requirements.txt or poetry
"""