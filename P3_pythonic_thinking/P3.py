"""
PYTHONIC THINKING
-----------------

This file covers concepts that make Python code cleaner, efficient,
and more "Pythonic".

Topics covered:

1. Iterators
2. Generators
3. zip()
4. enumerate()
5. map()
6. filter()
7. reduce()
8. Shallow vs Deep Copy
9. Mutability vs Immutability
10. *args and **kwargs
"""

# =========================================================
# ITERATORS
# =========================================================

"""
An iterator is an object that allows sequential access to elements.

Key methods:
__iter__()  -> returns iterator object
__next__()  -> returns next element

Lists, tuples, sets, dictionaries are iterable objects.
"""

numbers = [1, 2, 3, 4]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))


# =========================================================
# GENERATORS
# =========================================================

"""
Generators are functions that produce values one at a time
using the 'yield' keyword.

Advantages:
- Memory efficient
- Used for large datasets or streams
"""

def number_generator(n):
    for i in range(n):
        yield i

gen = number_generator(5)

for num in gen:
    print(num)


# Generator expression
squares = (x*x for x in range(5))

print(list(squares))


# =========================================================
# ZIP FUNCTION
# =========================================================

"""
zip() combines multiple iterables element-wise.
"""

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

combined = zip(names, scores)

print(list(combined))


# =========================================================
# ENUMERATE
# =========================================================

"""
enumerate() provides both index and value during iteration.
"""

fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# =========================================================
# MAP
# =========================================================

"""
map() applies a function to every element of an iterable.
"""

numbers = [1, 2, 3, 4]

squared = map(lambda x: x*x, numbers)

print(list(squared))


# =========================================================
# FILTER
# =========================================================

"""
filter() selects elements that satisfy a condition.
"""

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))


# =========================================================
# REDUCE
# =========================================================

"""
reduce() applies a function cumulatively to elements.

It is located in the functools module.
"""

from functools import reduce

numbers = [1, 2, 3, 4]

product = reduce(lambda x, y: x * y, numbers)

print(product)


# =========================================================
# SHALLOW VS DEEP COPY
# =========================================================

"""
Copying objects can create two types of copies:

Shallow Copy
Deep Copy
"""

import copy

original = [[1, 2], [3, 4]]

# Shallow copy
shallow = copy.copy(original)

# Deep copy
deep = copy.deepcopy(original)

original[0][0] = 100

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)


# =========================================================
# MUTABILITY VS IMMUTABILITY
# =========================================================

"""
Mutable objects can be changed.
Immutable objects cannot be modified.
"""

# Mutable example
my_list = [1, 2, 3]

my_list[0] = 100

print(my_list)

# Immutable example
my_string = "hello"

# my_string[0] = "H" -> ERROR


# =========================================================
# *ARGS
# =========================================================

"""
*args allows a function to accept multiple positional arguments.
"""

def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))


# =========================================================
# **KWARGS
# =========================================================

"""
**kwargs allows functions to accept keyword arguments
as a dictionary.
"""

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

print_info(name="Shivansh", age=21, city="Pune")