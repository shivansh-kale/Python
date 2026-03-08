# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming (OOP) is a programming paradigm that organizes code using **objects and classes**.

OOP helps developers build **modular, reusable, and maintainable code**.

It is heavily used in:

* Machine learning libraries
* Backend frameworks
* Game development
* Large software systems

---

# 1. Classes and Objects

## Class

A **class** is a blueprint for creating objects.

Example:

```python
class Car:
    pass
```

---

## Object

An **object** is an instance of a class.

Example:

```python
car1 = Car()
```

Objects represent **real-world entities**.

Example:

| Class   | Object |
| ------- | ------ |
| Car     | Tesla  |
| Student | Alice  |
| Product | Laptop |

---

# 2. Constructors (`__init__`)

A **constructor** is a special method automatically executed when an object is created.

In Python the constructor is:

```python
__init__()
```

Example:

```python
class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
```

Here:

* `self` refers to the current object
* attributes are initialized during object creation

---

# 3. Instance vs Class Variables

## Instance Variables

Belong to individual objects.

Example:

```python
self.name
self.age
```

Each object can have different values.

---

## Class Variables

Shared across all objects.

Example:

```python
class Student:

    school_name = "ABC University"
```

Every instance can access this value.

---

# 4. Methods

Methods are functions defined inside classes.

Example:

```python
class Calculator:

    def add(self, a, b):
        return a + b
```

Methods define **behavior of objects**.

---

# 5. Dunder Methods

Dunder means **double underscore**.

These methods customize how objects behave.

Examples:

| Method     | Purpose               |
| ---------- | --------------------- |
| `__init__` | Constructor           |
| `__str__`  | String representation |
| `__len__`  | Length of object      |
| `__repr__` | Debug representation  |

Example:

```python
class Book:

    def __str__(self):
        return "Book object"
```

---

# 6. Inheritance

Inheritance allows one class to **reuse code from another class**.

Example:

```python
class Animal:
    pass

class Dog(Animal):
    pass
```

Here:

* `Animal` = Parent class
* `Dog` = Child class

Benefits:

* Code reuse
* Hierarchical design
* Easier maintenance

---

# 7. Method Overriding

A child class can **override a parent method**.

Example:

```python
class Bird:
    def move(self):
        print("Bird flies")

class Penguin(Bird):
    def move(self):
        print("Penguin swims")
```

---

# 8. Polymorphism

Polymorphism means **one interface, many implementations**.

Different objects respond differently to the same method.

Example:

```python
class Cat:
    def speak(self):
        print("Meow")

class Cow:
    def speak(self):
        print("Moo")
```

---

# 9. Encapsulation

Encapsulation means **restricting direct access to data**.

Python uses naming conventions:

| Symbol  | Meaning   |
| ------- | --------- |
| `_var`  | Protected |
| `__var` | Private   |

Example:

```python
class BankAccount:

    def __init__(self, balance):
        self.__balance = balance
```

Private variables cannot be accessed directly.

---

# 10. Abstraction

Abstraction hides internal implementation details.

Python uses **abstract base classes**.

Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Any subclass must implement the `area()` method.

---

# 11. Dataclasses

Dataclasses simplify class creation.

Example:

```python
from dataclasses import dataclass

@dataclass
class Person:

    name: str
    age: int
```

Dataclasses automatically generate:

* `__init__`
* `__repr__`
* `__eq__`

Benefits:

* Less boilerplate
* Cleaner code
* Easier data modeling

---

# Summary

Object-Oriented Programming provides a structured way to build software.

Key concepts include:

| Concept       | Purpose                         |
| ------------- | ------------------------------- |
| Classes       | Blueprint for objects           |
| Objects       | Instances of classes            |
| Constructor   | Initializes objects             |
| Inheritance   | Code reuse                      |
| Polymorphism  | Same method, different behavior |
| Encapsulation | Protect data                    |
| Abstraction   | Hide complexity                 |
| Dataclasses   | Simplify data models            |

Mastering these concepts allows developers to build **scalable and maintainable Python applications**.
