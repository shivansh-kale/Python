# File Handling & Serialization in Python

Python programs often need to interact with files and external data.
File handling allows programs to **read, write, and store data**, while serialization allows saving complex objects.

This section covers:

* reading and writing text files
* handling CSV and JSON files
* serialization using pickle
* working with directories
* logging program activity

---

# 1. Reading and Writing Text Files

Python provides the `open()` function for file operations.

Example:

```python
file = open("example.txt", "r")
content = file.read()
file.close()
```

However, the recommended approach uses the **context manager** `with`.

```python
with open("example.txt", "r") as file:
    content = file.read()
```

Advantages:

* automatically closes the file
* prevents resource leaks

---

## File Modes

| Mode | Purpose                |
| ---- | ---------------------- |
| r    | Read file              |
| w    | Write file (overwrite) |
| a    | Append to file         |
| b    | Binary mode            |

Example:

```python
with open("example.txt", "w") as file:
    file.write("Hello Python")
```

---

# 2. CSV Handling

CSV files store tabular data.

Example CSV:

```
Name,Age,City
Alice,21,New York
Bob,22,London
```

Python provides the `csv` module.

Write CSV:

```python
import csv

with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
```

Read CSV:

```python
with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

CSV files are commonly used in **datasets for machine learning**.

---

# 3. JSON Handling

JSON is a lightweight data-interchange format.

Example JSON:

```json
{
    "name": "Alice",
    "age": 21
}
```

Python uses the `json` module.

Write JSON:

```python
json.dump(data, file)
```

Read JSON:

```python
data = json.load(file)
```

JSON is widely used in:

* APIs
* configuration files
* web applications

---

# 4. Pickle Serialization

Serialization converts objects into a format that can be stored or transmitted.

Python uses the **pickle module**.

Example:

```python
import pickle

pickle.dump(object, file)
```

Load object:

```python
pickle.load(file)
```

Pickle is frequently used to save **trained machine learning models**.

---

## Pickle Advantages

* fast
* supports complex Python objects
* easy to use

---

## Pickle Disadvantages

* not secure for untrusted data
* Python-specific format
* not human readable

---

# 5. Working with Directories

Python provides tools for filesystem operations.

## os Module

```python
import os

os.getcwd()
os.listdir()
os.makedirs("folder")
```

---

## pathlib Module

`pathlib` provides a modern object-oriented interface.

Example:

```python
from pathlib import Path

path = Path("data.txt")

print(path.exists())
print(path.name)
```

`pathlib` is recommended for modern Python code.

---

# 6. Logging to Files

Logging helps track application behavior and errors.

Example:

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Application started")
```

Logging levels:

| Level    | Purpose                  |
| -------- | ------------------------ |
| DEBUG    | Detailed diagnostic info |
| INFO     | General events           |
| WARNING  | Potential issues         |
| ERROR    | Error occurred           |
| CRITICAL | Severe failure           |

Logging is essential for **production systems and debugging**.

---

# Summary

File handling and serialization allow Python programs to store and retrieve data.

| Concept      | Purpose                   |
| ------------ | ------------------------- |
| Text files   | Read and write plain text |
| CSV          | Store tabular data        |
| JSON         | Data exchange format      |
| Pickle       | Serialize Python objects  |
| os / pathlib | Filesystem operations     |
| logging      | Track application events  |

These tools are widely used in **data science, machine learning pipelines, and backend systems**.
