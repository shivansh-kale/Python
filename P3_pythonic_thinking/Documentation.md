# Pythonic Thinking

Python encourages writing code that is **simple, readable, and expressive**.
This philosophy is often referred to as **Pythonic thinking**.

This section introduces several concepts that help developers write efficient and elegant Python programs.

Topics covered:

* Iterators
* Generators
* zip()
* enumerate()
* map(), filter(), reduce()
* Shallow vs Deep Copy
* Mutability vs Immutability
* *args and **kwargs

---

# 1. Iterators

## Definition

An **iterator** is an object that allows sequential traversal through a collection of elements.

Python internally uses iterators in loops.

Example:

```python
numbers = [1,2,3]

iterator = iter(numbers)

print(next(iterator))
```

Key methods used by iterators:

| Method       | Purpose                 |
| ------------ | ----------------------- |
| `__iter__()` | Returns iterator object |
| `__next__()` | Returns next element    |

---

# 2. Generators

## Definition

A **generator** is a special type of function that produces values **one at a time** using the `yield` keyword.

Example:

```python
def count(n):
    for i in range(n):
        yield i
```

Generators are useful because they:

* Save memory
* Generate values lazily
* Handle large datasets efficiently

Example usage:

```python
for num in count(5):
    print(num)
```

---

# 3. zip()

The `zip()` function combines multiple iterables element-wise.

Example:

```python
names = ["Alice", "Bob"]
scores = [90, 85]

result = zip(names, scores)
```

Output:

```
[('Alice', 90), ('Bob', 85)]
```

Common uses:

* Combining datasets
* Parallel iteration

---

# 4. enumerate()

The `enumerate()` function provides both **index and value** while iterating.

Example:

```python
fruits = ["apple", "banana"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```
0 apple
1 banana
```

This avoids manually managing a counter variable.

---

# 5. map()

`map()` applies a function to every element of an iterable.

Example:

```python
numbers = [1,2,3]

squares = map(lambda x: x*x, numbers)
```

Equivalent list comprehension:

```python
[x*x for x in numbers]
```

---

# 6. filter()

`filter()` selects elements that satisfy a condition.

Example:

```python
numbers = [1,2,3,4]

even = filter(lambda x: x % 2 == 0, numbers)
```

Equivalent comprehension:

```python
[x for x in numbers if x % 2 == 0]
```

---

# 7. reduce()

`reduce()` applies a function cumulatively to elements of an iterable.

It is available in the **functools module**.

Example:

```python
from functools import reduce

numbers = [1,2,3,4]

product = reduce(lambda x,y: x*y, numbers)
```

This multiplies all numbers together.

---

# 8. Shallow vs Deep Copy

Copying objects in Python can behave differently depending on how the copy is performed.

## Shallow Copy

A shallow copy creates a **new object but references the same nested objects**.

Example:

```python
import copy

shallow = copy.copy(original)
```

Changes in nested objects affect both copies.

---

## Deep Copy

A deep copy creates **completely independent copies of nested objects**.

Example:

```python
deep = copy.deepcopy(original)
```

Changes in one object will not affect the other.

---

# 9. Mutability vs Immutability

Objects in Python can be **mutable** or **immutable**.

## Mutable Objects

Mutable objects can be modified after creation.

Examples:

* lists
* dictionaries
* sets

Example:

```python
my_list = [1,2,3]

my_list[0] = 100
```

---

## Immutable Objects

Immutable objects cannot be modified after creation.

Examples:

* strings
* tuples
* integers
* floats

Example:

```python
text = "hello"

# text[0] = "H"   Not allowed
```

---

# 10. *args and **kwargs

These allow functions to accept **variable numbers of arguments**.

---

## *args

`*args` allows multiple **positional arguments**.

Example:

```python
def add(*args):
    return sum(args)
```

Usage:

```python
add(1,2,3,4)
```

---

## **kwargs

`**kwargs` allows **keyword arguments**.

Example:

```python
def print_info(**kwargs):
    print(kwargs)
```

Usage:

```python
print_info(name="Shivansh", age=21)
```

This is often used in:

* configuration systems
* APIs
* machine learning libraries

---

# Summary

Pythonic thinking focuses on writing **clean and efficient code**.

Key tools include:

| Concept      | Purpose                          |
| ------------ | -------------------------------- |
| Iterators    | Sequential data access           |
| Generators   | Memory-efficient data generation |
| zip()        | Combine iterables                |
| enumerate()  | Access index and value           |
| map()        | Apply function to iterable       |
| filter()     | Select elements by condition     |
| reduce()     | Aggregate values                 |
| Shallow copy | Copies reference structure       |
| Deep copy    | Fully independent copy           |
| *args        | Variable positional arguments    |
| **kwargs     | Variable keyword arguments       |

These concepts appear frequently in **data science pipelines and machine learning frameworks**.
