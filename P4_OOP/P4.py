"""
OBJECT ORIENTED PROGRAMMING IN PYTHON
-------------------------------------

OOP is a programming paradigm that organizes code using objects.

Main concepts covered in this file:

1. Classes and Objects
2. Constructors (__init__)
3. Instance vs Class Variables
4. Methods and Dunder Methods
5. Inheritance
6. Method Overriding
7. Polymorphism
8. Encapsulation
9. Abstraction
10. Dataclasses
"""

# =========================================================
# CLASSES AND OBJECTS
# =========================================================

"""
A class is a blueprint for creating objects.

Example:
A class "Car" defines properties and behavior of cars.

An object is an instance of the class.
"""

class Car:

    # constructor initializes object attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")


# creating objects
car1 = Car("Tesla", "Model S", 2022)
car2 = Car("Toyota", "Corolla", 2020)

car1.display_info()
car2.display_info()


# =========================================================
# INSTANCE VS CLASS VARIABLES
# =========================================================

"""
Instance variables
------------------
Belong to individual objects.

Class variables
---------------
Shared across all instances.
"""

class Student:

    # class variable
    school_name = "ABC University"

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age, Student.school_name)


s1 = Student("Alice", 21)
s2 = Student("Bob", 22)

s1.show_info()
s2.show_info()


# =========================================================
# METHODS
# =========================================================

"""
Methods are functions defined inside a class.
"""

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print(calc.add(2, 3))
print(calc.multiply(3, 4))


# =========================================================
# DUNDER METHODS
# =========================================================

"""
Dunder = "Double underscore"

These are special methods that define behavior of objects.

Examples:
__init__   -> constructor
__str__    -> string representation
__len__    -> length behavior
"""

class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __len__(self):
        return self.pages


book = Book("Python Basics", 300)

print(book)
print(len(book))


# =========================================================
# INHERITANCE
# =========================================================

"""
Inheritance allows a class to inherit properties and methods
from another class.

Parent class -> Base class
Child class -> Derived class
"""

class Animal:

    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):

    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()


# =========================================================
# METHOD OVERRIDING
# =========================================================

"""
Method overriding allows a child class to redefine
a method from the parent class.
"""

class Bird:

    def move(self):
        print("Bird flies")


class Penguin(Bird):

    def move(self):
        print("Penguin swims")


p = Penguin()

p.move()


# =========================================================
# POLYMORPHISM
# =========================================================

"""
Polymorphism means "many forms".

Different objects can respond to the same method in different ways.
"""

class Cat:
    def speak(self):
        print("Meow")


class Cow:
    def speak(self):
        print("Moo")


animals = [Cat(), Cow()]

for animal in animals:
    animal.speak()


# =========================================================
# ENCAPSULATION
# =========================================================

"""
Encapsulation means restricting access to certain attributes.

Convention:
_single_underscore  -> protected
__double_underscore -> private
"""

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance   # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())


# =========================================================
# ABSTRACTION
# =========================================================

"""
Abstraction means hiding implementation details
and exposing only essential functionality.
"""

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rect = Rectangle(4, 5)

print(rect.area())


# =========================================================
# DATACLASSES
# =========================================================

"""
Dataclasses automatically generate boilerplate code
like __init__, __repr__, and __eq__.
"""

from dataclasses import dataclass

@dataclass
class Person:

    name: str
    age: int
    city: str


person = Person("Shivansh", 21, "Pune")

print(person)