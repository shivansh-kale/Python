"""
BUILT-IN DATA STRUCTURES IN PYTHON
----------------------------------

This file covers the most important Python data structures:

1. Lists
2. Tuples
3. Sets
4. Dictionaries
5. Strings

These structures are heavily used in data processing,
machine learning pipelines, and general Python programming.
"""

# =========================================================
# LISTS
# =========================================================

"""
A list is an ordered, mutable collection of elements.

Key properties:
- Ordered
- Mutable (can be modified)
- Allows duplicate elements
"""

numbers = [1, 2, 3, 4, 5]

print("List:", numbers)

print(numbers[0])   # first element
print(numbers[-1])  # last element

# (lists are mutable)
numbers[0] = 100
print("Modified list:", numbers)

# Add elements
numbers.append(6)  # add at end
print(numbers)

numbers.insert(1, 50)  # insert at specific index
print(numbers)

# Remove elements
numbers.remove(50)
print(numbers)

# List length
print("Length:", len(numbers))

# Iterating over list
for num in numbers:
    print(num)


# =========================================================
# TUPLES
# =========================================================

"""
A tuple is an ordered but immutable collection.

Key properties:
- Ordered
- Immutable (cannot change elements)
- Allows duplicates
"""

coordinates = (10, 20)

print("Tuple:", coordinates)

# Access elements
print(coordinates[0])

# Tuples cannot be modified
# coordinates[0] = 5  -> This will raise an error

# Tuple unpacking
x, y = coordinates
print("x:", x)
print("y:", y)


# =========================================================
# SETS
# =========================================================

"""
A set is an unordered collection of unique elements.

Key properties:
- Unordered
- Mutable
- No duplicate elements
"""

numbers_set = {1, 2, 3, 4, 4, 5}

print("Set:", numbers_set)

# Add element
numbers_set.add(6)

print(numbers_set)

# Remove element
numbers_set.remove(3)

print(numbers_set)

# Set operations (important in probability and ML)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A.union(B))
print("Intersection:", A.intersection(B))
print("Difference:", A.difference(B))


# =========================================================
# DICTIONARIES
# =========================================================

"""
A dictionary stores data in key-value pairs.

Key properties:
- Unordered (before Python 3.7)
- Mutable
- Keys must be unique
"""

student = {
    "name": "Shivansh",
    "age": 21,
    "course": "IT Engineering"
}

print(student)

# Access values using keys
print(student["name"])

# Add new key-value pair
student["city"] = "Pune"

print(student)

# Update value
student["age"] = 22

print(student)

# Iterate through dictionary

for key, value in student.items():
    print(key, ":", value)

# Get keys and values
print(student.keys())
print(student.values())


# =========================================================
# STRINGS
# =========================================================

"""
Strings are sequences of characters.

Key properties:
- Ordered
- Immutable
"""

text = "Machine Learning"

print(text)

# Access characters
print(text[0])

# String slicing
print(text[0:7])
print(text[:7])
print(text[8:])

# Strings are immutable
# text[0] = "m"  -> This will cause an error

# String formatting

name = "Shivansh"
age = 21

message = f"My name is {name} and I am {age} years old."

print(message)

# Common string methods

sentence = "python is powerful"

print(sentence.upper())
print(sentence.capitalize())
print(sentence.split())