"""
FILE HANDLING AND SERIALIZATION IN PYTHON
-----------------------------------------

This file covers:

1. Reading and writing text files
2. Working with CSV files
3. Working with JSON files
4. Pickle serialization
5. Working with directories (os, pathlib)
6. Logging to files

These concepts are widely used in:
- data science
- machine learning pipelines
- backend systems
"""

# =========================================================
# 1. READING AND WRITING TEXT FILES
# =========================================================

"""
Python uses the open() function to work with files.

Modes:
r  -> read
w  -> write (overwrites file)
a  -> append
"""

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a text file.\n")
    file.write("Python file handling example.\n")

# Reading a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())


# =========================================================
# 2. CSV FILE HANDLING
# =========================================================

"""
CSV (Comma Separated Values) files are commonly used
for datasets in data science and machine learning.
"""

import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 21, "New York"],
    ["Bob", 22, "London"]
]

# Writing CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# =========================================================
# 3. JSON HANDLING
# =========================================================

"""
JSON (JavaScript Object Notation) is widely used for:

- APIs
- configuration files
- data storage
"""

import json

student = {
    "name": "Shivansh",
    "age": 21,
    "skills": ["Python", "Machine Learning"]
}

# Writing JSON
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Reading JSON
with open("student.json", "r") as file:
    data = json.load(file)
    print(data)


# =========================================================
# 4. PICKLE SERIALIZATION
# =========================================================

"""
Pickle is used to serialize Python objects into binary format.

It is commonly used for saving trained ML models.
"""

import pickle

model_data = {"model": "LinearRegression", "accuracy": 0.92}

# Save object
with open("model.pkl", "wb") as file:
    pickle.dump(model_data, file)

# Load object
with open("model.pkl", "rb") as file:
    loaded_model = pickle.load(file)
    print(loaded_model)


"""
Pickle Pros:
- Fast serialization
- Supports complex Python objects

Pickle Cons:
- Not secure for untrusted data
- Python-specific format
"""


# =========================================================
# 5. WORKING WITH DIRECTORIES
# =========================================================

"""
Python provides tools for interacting with the filesystem.
"""

import os

# Get current directory
print(os.getcwd())

# List files
print(os.listdir("."))

# Create directory
os.makedirs("new_folder", exist_ok=True)


# pathlib (modern alternative)
from pathlib import Path

path = Path("example.txt")

print("File exists:", path.exists())
print("File name:", path.name)
print("Absolute path:", path.resolve())


# =========================================================
# 6. LOGGING TO FILES
# =========================================================

"""
Logging helps track program execution and errors.
It is essential for debugging and production systems.
"""

import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Application started")
logging.warning("This is a warning message")
logging.error("This is an error message")