# Built-in Data Structures in Python

Python provides powerful built-in data structures used to store and manipulate data efficiently.

The most important ones are:

* Lists
* Tuples
* Sets
* Dictionaries
* Strings

These structures are widely used in **data processing, machine learning, and backend development**.

---

# 1. Lists

## Definition

A **list** is an ordered collection of elements.

Lists can store multiple types of data and are **mutable**, meaning their contents can be modified.

Example:

```python
numbers = [1, 2, 3, 4, 5]
```

---

## Properties of Lists

| Property          | Description                            |
| ----------------- | -------------------------------------- |
| Ordered           | Elements maintain their position       |
| Mutable           | Elements can be changed                |
| Allows duplicates | Same element can appear multiple times |
| Indexed           | Elements accessed by index             |

---

## Accessing Elements

```python
numbers[0]
numbers[-1]
```

Indexing starts from **0**.

---

## List Methods

Common operations:

```python
numbers.append(10)
numbers.insert(1, 50)
numbers.remove(50)
len(numbers)
```

These operations are commonly used during **data preprocessing in machine learning**.

---

# 2. Tuples

## Definition

A **tuple** is an ordered collection similar to a list but **immutable**.

Example:

```python
coordinates = (10, 20)
```

---

## Properties

| Property          | Description              |
| ----------------- | ------------------------ |
| Ordered           | Maintains element order  |
| Immutable         | Cannot modify elements   |
| Allows duplicates | Duplicate values allowed |

---

## Tuple Unpacking

```python
x, y = (10, 20)
```

This assigns:

```
x = 10
y = 20
```

Tuples are often used for **fixed data structures**, such as coordinates.

---

# 3. Sets

## Definition

A **set** is an unordered collection of unique elements.

Example:

```python
numbers = {1,2,3,4}
```

---

## Properties

| Property  | Description                   |
| --------- | ----------------------------- |
| Unordered | No fixed order                |
| Mutable   | Elements can be added/removed |
| Unique    | No duplicate values           |

Example:

```python
{1,2,2,3} → {1,2,3}
```

---

## Set Operations

Sets support mathematical operations:

### Union

```python
A.union(B)
```

### Intersection

```python
A.intersection(B)
```

### Difference

```python
A.difference(B)
```

These operations are widely used in **probability and statistics**, which are foundational for machine learning.

---

# 4. Dictionaries

## Definition

A **dictionary** stores data in **key-value pairs**.

Example:

```python
student = {
    "name": "Shivansh",
    "age": 21
}
```

---

## Properties

| Property            | Description                |
| ------------------- | -------------------------- |
| Key-value structure | Data stored as pairs       |
| Mutable             | Values can be modified     |
| Unique keys         | Duplicate keys not allowed |

---

## Accessing Data

```python
student["name"]
```

---

## Dictionary Iteration

```python
for key, value in student.items():
    print(key, value)
```

Dictionaries are heavily used when working with:

* JSON data
* API responses
* Dataset records

---

# 5. Strings

## Definition

A **string** is a sequence of characters.

Example:

```python
text = "Machine Learning"
```

---

## Properties

| Property  | Description                 |
| --------- | --------------------------- |
| Ordered   | Characters have positions   |
| Immutable | Cannot change characters    |
| Iterable  | Can loop through characters |

---

## String Slicing

```python
text[0:7]
text[:7]
text[8:]
```

This extracts substrings from a string.

---

## String Formatting

Modern Python uses **f-strings**.

Example:

```python
name = "Shivansh"
age = 21

message = f"My name is {name} and I am {age}"
```

This is the most readable and efficient formatting method.

---

# Summary

Python's built-in data structures are essential for working with data.

| Data Structure | Key Feature           |
| -------------- | --------------------- |
| List           | Ordered and mutable   |
| Tuple          | Ordered and immutable |
| Set            | Unique elements       |
| Dictionary     | Key-value pairs       |
| String         | Immutable text data   |

These structures form the **foundation of data manipulation in Python and machine learning workflows**.
