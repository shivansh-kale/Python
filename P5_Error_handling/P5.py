"""
ERROR HANDLING AND DEBUGGING IN PYTHON
--------------------------------------

This file covers:

1. Exceptions
2. try / except / finally
3. Raising exceptions
4. Custom exceptions
5. Common runtime errors
"""

# =========================================================
# WHAT ARE EXCEPTIONS
# =========================================================

"""
An exception is an error that occurs during program execution.

When Python encounters an error, it raises an exception and
stops the program unless the error is handled.
"""

# Example of runtime error
# print(10 / 0)  # ZeroDivisionError


# =========================================================
# TRY / EXCEPT
# =========================================================

"""
The try block contains code that might raise an exception.

If an error occurs, the except block handles it.
"""

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Invalid input. Please enter a number.")


# =========================================================
# MULTIPLE EXCEPTIONS
# =========================================================

"""
You can catch multiple exception types.
"""

try:
    numbers = [1, 2, 3]
    print(numbers[5])

except IndexError:
    print("Index is out of range.")

except Exception as e:
    print("Something went wrong:", e)


# =========================================================
# ELSE BLOCK
# =========================================================

"""
The else block runs if no exception occurs.
"""

try:
    num = int("10")

except ValueError:
    print("Conversion failed")

else:
    print("Conversion successful:", num)


# =========================================================
# FINALLY BLOCK
# =========================================================

"""
The finally block always executes, whether an error occurs or not.
Commonly used for cleanup operations.
"""

try:
    file = open("sample.txt", "r")

except FileNotFoundError:
    print("File not found")

finally:
    print("Execution finished.")


# =========================================================
# RAISING EXCEPTIONS
# =========================================================

"""
You can manually raise exceptions using the raise keyword.
"""

def check_age(age):

    if age < 18:
        raise ValueError("Age must be 18 or above.")

    return "Access granted"


try:
    print(check_age(16))

except ValueError as e:
    print(e)


# =========================================================
# CUSTOM EXCEPTIONS
# =========================================================

"""
Custom exceptions allow developers to define application-specific errors.
"""

class InsufficientBalanceError(Exception):
    """Custom exception for bank account errors"""
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance")

        self.balance -= amount
        print("Withdrawal successful")


account = BankAccount(1000)

try:
    account.withdraw(1500)

except InsufficientBalanceError as e:
    print("Transaction failed:", e)


# =========================================================
# COMMON RUNTIME ERRORS
# =========================================================

"""
Some common Python runtime errors:
"""

# ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# TypeError
try:
    result = "10" + 5
except TypeError:
    print("Cannot add string and integer")

# IndexError
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range")

# KeyError
try:
    student = {"name": "Alice"}
    print(student["age"])
except KeyError:
    print("Key not found in dictionary")