# Python Basics for Machine Learning

This document explains the **core Python concepts** required before learning Machine Learning.
These fundamentals form the base for working with libraries such as **NumPy, Pandas, Scikit-learn, and PyTorch**.

---

# 1. Python Syntax, Indentation, and Code Style (PEP8)

## Python Syntax

Python syntax is designed to be **simple, readable, and minimalistic**.

Unlike languages like **C, C++, or Java**, Python **does not use curly braces `{}`** to define code blocks.

Instead, Python uses **indentation**.

Example:

```python
x = 10

if x > 5:
    print("x is greater than 5")
```

Here, the indentation indicates that the `print()` statement belongs to the `if` block.

If indentation is incorrect, Python will raise an **IndentationError**.

Example:

```python
if x > 5:
print("Incorrect indentation")
```

---

## Indentation Rules

Python requires **consistent indentation**.

Standard rule:

* Use **4 spaces per indentation level**

Example:

```python
if condition:
    do_something()
    do_another_thing()
```

Avoid mixing **tabs and spaces**, as it can lead to syntax errors.

---

## PEP8 – Python Style Guide

PEP8 stands for **Python Enhancement Proposal 8**.

It defines the **standard coding style for Python** to make code readable and consistent.

Key PEP8 guidelines:

### Variable Naming

Use **snake_case**

```python
user_age = 21
total_marks = 450
```

Avoid unclear names:

```python
a = 21
tm = 450
```

---

### Class Naming

Classes should use **PascalCase**

```python
class StudentProfile:
    pass
```

---

### Constants

Constants should be written in **UPPER_CASE**

```python
PI = 3.14159
MAX_USERS = 100
```

---

### Line Length

Recommended maximum line length:

```
79 characters
```

---

# 2. Variables, Data Types, and Type Casting

## Variables

A **variable** stores a value in memory.

Example:

```python
age = 21
name = "Shivansh"
```

Python automatically determines the type of the variable.

This is called **dynamic typing**.

---

## Common Data Types

| Data Type | Description     | Example   |
| --------- | --------------- | --------- |
| int       | Integer numbers | `10`      |
| float     | Decimal numbers | `3.14`    |
| str       | Text data       | `"Hello"` |
| bool      | True or False   | `True`    |

Example:

```python
age = 21
height = 6.2
name = "Shivansh"
is_student = True
```

Check the type using:

```python
print(type(age))
```

---

## Type Casting

Type casting means **converting one data type to another**.

### String to Integer

```python
num = "25"
num_int = int(num)
```

### Integer to Float

```python
float_value = float(10)
```

### Integer to String

```python
string_value = str(100)
```

---

# 3. Input / Output, Comments, and Docstrings

## Input

Python provides the `input()` function to accept user input.

Example:

```python
name = input("Enter your name: ")
print("Hello", name)
```

Important note:

```
input() always returns a string
```

If numeric input is needed:

```python
age = int(input("Enter your age: "))
```

---

## Output

The `print()` function is used to display output.

Example:

```python
print("Hello World")
```

Multiple values:

```python
print("Age:", 21)
```

---

## Comments

Comments help explain code.

### Single-line comment

```python
# This is a comment
```

### Multi-line comment

```python
"""
This is a multi-line comment
"""
```

Comments are ignored during execution.

---

## Docstrings

Docstrings are **documentation strings** used to describe functions, classes, and modules.

Example:

```python
def greet(name):
    """
    Greets the user with their name.

    Parameters
    ----------
    name : str
        Name of the user
    """

    print("Hello", name)
```

Docstrings help tools automatically generate documentation.

---

# 4. Control Flow (if / else)

Control flow allows programs to **make decisions**.

Example:

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

## if – elif – else

Used when multiple conditions are present.

```python
marks = 85

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

else:
    print("Grade C")
```

---

# 5. Loops

Loops allow repeating tasks.

Two main types:

1. `for` loop
2. `while` loop

---

## For Loop

Used for iterating over sequences.

Example:

```python
numbers = [1,2,3,4,5]

for num in numbers:
    print(num)
```

Using `range()`:

```python
for i in range(5):
    print(i)
```

---

## While Loop

Runs while a condition is true.

Example:

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

---

# 6. Functions

Functions help organize and reuse code.

Structure:

```python
def function_name(parameters):
    code
    return value
```

Example:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
```

---

## Default Arguments

Functions can have default values.

```python
def greet_user(name="Guest"):
    print("Hello", name)
```

---

# 7. Lambda Functions

Lambda functions are **anonymous one-line functions**.

Syntax:

```python
lambda arguments : expression
```

Example:

```python
square = lambda x: x * x
print(square(5))
```

Multiple arguments:

```python
add = lambda a, b: a + b
```

Lambda functions are commonly used with:

* `map()`
* `filter()`
* `sorted()`

---

# 8. List, Dictionary, and Set Comprehensions

Comprehensions provide a **concise way to create collections**.

---

## List Comprehension

Syntax:

```python
[expression for item in iterable]
```

Example:

```python
numbers = [1,2,3,4,5]

squares = [x**2 for x in numbers]
```

With condition:

```python
even_numbers = [x for x in numbers if x % 2 == 0]
```

---

## Dictionary Comprehension

Syntax:

```python
{key:value for item in iterable}
```

Example:

```python
square_dict = {x: x**2 for x in range(5)}
```

---

## Set Comprehension

Sets automatically remove duplicates.

Example:

```python
numbers = [1,2,2,3,4,4]

unique_numbers = {x for x in numbers}
```

---

# Summary

This section covered the most important Python fundamentals:

* Python syntax and indentation
* PEP8 coding style
* Variables and data types
* Type casting
* Input and output
* Comments and docstrings
* Control flow
* Loops
* Functions
* Lambda functions
* Comprehensions

These concepts form the **foundation required before learning data science and machine learning libraries**.
