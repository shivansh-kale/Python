"""
PYTHON STANDARD LIBRARY (HIGH-ROI MODULES)
------------------------------------------

This file covers important built-in modules:

1. os
2. sys
3. pathlib
4. datetime and time
5. math
6. random
7. logging

These modules are part of Python's standard library
and do not require installation.
"""

# =========================================================
# 1. OS MODULE
# =========================================================

"""
The os module allows interaction with the operating system.
Useful for file and directory operations.
"""

import os

# Current working directory
print("Current directory:", os.getcwd())

# List files in directory
print("Files in directory:", os.listdir("."))

# Create directory
os.makedirs("example_folder", exist_ok=True)


# =========================================================
# 2. SYS MODULE
# =========================================================

"""
The sys module provides access to Python runtime environment.
"""

import sys

# Python version
print("Python version:", sys.version)

# Command line arguments
print("Command line arguments:", sys.argv)

# Python module search paths
print("Module search paths:", sys.path)


# =========================================================
# 3. PATHLIB (MODERN FILE PATH HANDLING)
# =========================================================

"""
pathlib provides an object-oriented interface
for working with filesystem paths.
"""

from pathlib import Path

path = Path("example.txt")

# Check if file exists
print("File exists:", path.exists())

# File name
print("File name:", path.name)

# Absolute path
print("Absolute path:", path.resolve())


# =========================================================
# 4. DATETIME MODULE
# =========================================================

"""
datetime is used for working with dates and times.
"""

from datetime import datetime, date

# Current date and time
now = datetime.now()

print("Current datetime:", now)

# Current date
today = date.today()

print("Today's date:", today)

# Formatting date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

print("Formatted time:", formatted)


# =========================================================
# 5. TIME MODULE
# =========================================================

"""
The time module is useful for timestamps and delays.
"""

import time

print("Current timestamp:", time.time())

# Pause execution
print("Waiting for 2 seconds...")
time.sleep(2)

print("Resumed execution")


# =========================================================
# 6. MATH MODULE
# =========================================================

"""
The math module provides mathematical functions.
"""

import math

print("Square root:", math.sqrt(16))
print("Factorial:", math.factorial(5))
print("Value of PI:", math.pi)

# Trigonometry
print("Cosine of 0:", math.cos(0))


# =========================================================
# 7. RANDOM MODULE
# =========================================================

"""
The random module generates pseudo-random numbers.
"""

import random

# Random float between 0 and 1
print("Random float:", random.random())

# Random integer
print("Random integer:", random.randint(1, 10))

# Random choice
print("Random choice:", random.choice(["apple", "banana", "cherry"]))

# Shuffle list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print("Shuffled list:", numbers)


# =========================================================
# 8. LOGGING MODULE
# =========================================================

"""
Logging helps track program behavior and errors.
It is essential for debugging and production systems.
"""

import logging

logging.basicConfig(
    filename="application.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("This is a warning message")
logging.error("This is an error message")