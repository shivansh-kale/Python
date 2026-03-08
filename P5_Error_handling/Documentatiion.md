# Error Handling and Debugging in Python

Errors are inevitable in software development.
Python provides a powerful **exception handling system** that allows programs to detect and handle errors gracefully.

Without error handling, a program would terminate whenever an unexpected issue occurs.

---

# 1. What Are Exceptions?

An **exception** is an error that occurs during program execution.

Example:

```python
10 / 0
```

This raises:

```
ZeroDivisionError
```

Python stops execution when an exception occurs unless it is handled.

---

# 2. try / except

The `try` block contains code that might raise an exception.

The `except` block catches and handles the error.

Example:

```python
try:
    num = int(input("Enter number"))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero is not allowed")
```

---

# 3. Handling Multiple Exceptions

Programs often need to handle different types of errors.

Example:

```python
try:
    numbers = [1,2,3]
    print(numbers[5])
except IndexError:
    print("Invalid index")
except Exception as e:
    print("Error:", e)
```

`Exception` is the **base class of most Python errors**.

---

# 4. else Block

The `else` block executes if **no exception occurs**.

Example:

```python
try:
    num = int("10")
except ValueError:
    print("Conversion failed")
else:
    print("Conversion successful")
```

---

# 5. finally Block

The `finally` block always executes regardless of whether an exception occurred.

Example:

```python
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File missing")
finally:
    print("Cleanup completed")
```

Common uses:

* closing files
* releasing resources
* cleaning up connections

---

# 6. Raising Exceptions

Sometimes developers need to **trigger errors intentionally**.

This is done using the `raise` keyword.

Example:

```python
def check_age(age):

    if age < 18:
        raise ValueError("Age must be 18 or above")
```

This ensures invalid data does not proceed further.

---

# 7. Custom Exceptions

Developers can create **custom exception classes** for application-specific errors.

Example:

```python
class InsufficientBalanceError(Exception):
    pass
```

Usage:

```python
if amount > balance:
    raise InsufficientBalanceError("Not enough funds")
```

Custom exceptions improve:

* readability
* debugging
* domain-specific error handling

---

# 8. Common Runtime Errors

Python programs commonly encounter the following errors.

| Error             | Cause                           |
| ----------------- | ------------------------------- |
| ZeroDivisionError | Division by zero                |
| TypeError         | Invalid operation between types |
| ValueError        | Incorrect value type            |
| IndexError        | Index out of range              |
| KeyError          | Missing dictionary key          |
| FileNotFoundError | File does not exist             |

Example:

```python
numbers = [1,2,3]

print(numbers[10])
```

This produces an **IndexError**.

---

# 9. Best Practices for Exception Handling

Good exception handling practices include:

1. Catch **specific exceptions**, not generic ones.
2. Avoid silent failures.
3. Use custom exceptions for domain-specific errors.
4. Use `finally` for resource cleanup.
5. Log errors for debugging.

Example:

```python
try:
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero is invalid")
```

---

# Summary

Error handling helps make programs robust and reliable.

Key concepts include:

| Concept           | Purpose                        |
| ----------------- | ------------------------------ |
| try               | Wrap risky code                |
| except            | Handle exceptions              |
| else              | Run code if no error occurs    |
| finally           | Always execute cleanup         |
| raise             | Trigger exceptions manually    |
| custom exceptions | Domain-specific error handling |

Effective exception handling is essential for **building stable Python applications and machine learning pipelines**.
