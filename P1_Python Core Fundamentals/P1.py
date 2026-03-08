"""
PYTHON BASICS FOR MACHINE LEARNING BEGINNERS
--------------------------------------------

This file covers:

1. Python syntax, indentation, and code style (PEP8)
2. Variables, data types, type casting
3. Input / Output
4. Comments and Docstrings
5. Control Flow (if / else, loops)
6. Functions and arguments
7. Lambda functions
8. List / Dictionary / Set comprehensions

PEP8 (Python Enhancement Proposal 8)
------------------------------------
Official style guide for Python.

Key rules:
- Use 4 spaces for indentation
- Variable names should be lowercase_with_underscores
- Class names should be PascalCase
- Constant names should be UPPERCASE
- Keep lines < 79 characters (recommended)

Example:
good_variable_name = 10
BADVARIABLE = 10  # Not recommended
"""

# ---------------------------------------------------
# VARIABLES AND DATA TYPES
# ---------------------------------------------------

"""
Variables store data values.

Python is dynamically typed:
You don't need to declare the data type.
"""

age = 21
height = 6.2
name = "Shivansh"
is_student = True

print("Name:", name)
print("Age:", age)

"""
Common Data Types

int     -> integers
float   -> decimal numbers
str     -> text
bool    -> True / False
"""

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))


# ---------------------------------------------------
# TYPE CASTING
# ---------------------------------------------------

"""
Type casting means converting one data type to another.
"""

num_str = "25"

num_int = int(num_str)

print(num_int + 5)

float_number = float(10)

print(float_number)

string_number = str(50)

print("Converted to string:", string_number)


# ---------------------------------------------------
# INPUT / OUTPUT
# ---------------------------------------------------

"""
input() takes user input from the console.
Note: input() always returns a string.
"""

# user_name = input("Enter your name: ")
# print("Hello", user_name)

# Example converting input
# age = int(input("Enter your age: "))
# print("Next year you will be", age + 1)


# ---------------------------------------------------
# COMMENTS
# ---------------------------------------------------

# This is a single line comment

"""
This is a multi-line comment.
Usually used for explanations.
"""


# ---------------------------------------------------
# DOCSTRINGS
# ---------------------------------------------------

def greet(name):
    """
    This is a docstring.

    Docstrings describe what a function does.
    Tools like documentation generators read these.

    Parameters
    ----------
    name : str
        Name of the person

    Returns
    -------
    None
    """

    print("Hello", name)


greet("Shivansh")


# ---------------------------------------------------
# CONTROL FLOW
# ---------------------------------------------------

"""
Control flow allows us to control program execution.

Examples:
if / else
loops
"""


# IF ELSE

age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")


# IF ELIF ELSE

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")


# ---------------------------------------------------
# LOOPS
# ---------------------------------------------------

"""
Loops repeat code multiple times.

Two main loops:
1. for loop
2. while loop
"""


# FOR LOOP

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print("Number:", num)


# FOR LOOP WITH RANGE

for i in range(5):
    print("i =", i)


"""
range(start, stop, step)
"""

for i in range(1, 10, 2):
    print(i)


# WHILE LOOP

count = 0

while count < 5:
    print("Count:", count)
    count += 1


# ---------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------

"""
Functions allow code reuse.

Structure:

def function_name(parameters):
    code
    return value
"""


def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


result = add_numbers(5, 3)

print("Sum:", result)


# FUNCTION WITH DEFAULT ARGUMENT


def greet_user(name="Guest"):
    print("Welcome", name)


greet_user()
greet_user("Shivansh")


# ---------------------------------------------------
# LAMBDA FUNCTIONS
# ---------------------------------------------------

"""
Lambda = small anonymous function

Used for short operations.

Syntax:
lambda arguments : expression
"""

square = lambda x: x * x

print(square(5))


add = lambda a, b: a + b

print(add(10, 20))


# ---------------------------------------------------
# LIST COMPREHENSION
# ---------------------------------------------------

"""
List comprehension provides a shorter way to create lists.

Syntax:
[expression for item in iterable]
"""

numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)


# LIST COMPREHENSION WITH CONDITION

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)


# ---------------------------------------------------
# DICTIONARY COMPREHENSION
# ---------------------------------------------------

"""
Dictionary comprehension creates dictionaries quickly.

Syntax:
{key:value for item in iterable}
"""

square_dict = {x: x ** 2 for x in range(5)}

print(square_dict)


# ---------------------------------------------------
# SET COMPREHENSION
# ---------------------------------------------------

"""
Set comprehension creates sets.

Sets automatically remove duplicates.
"""

numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = {x for x in numbers}

print(unique_numbers)