# Type Hints and Static Typing in Python

Type hints allow developers to specify expected data types for variables, function arguments, and return values.

They were introduced in **Python 3.5 (PEP 484)** and are widely used in modern Python codebases.

Type hints improve:

* code readability
* maintainability
* static analysis
* IDE support

Note: Python remains **dynamically typed**. Type hints do not enforce types at runtime.

---

# 1. Basic Type Hints

Functions can specify types for parameters and return values.

Example:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Explanation:

| Part     | Meaning        |
| -------- | -------------- |
| `a: int` | parameter type |
| `b: int` | parameter type |
| `-> int` | return type    |

---

# 2. Variable Type Hints

Variables can also include type annotations.

Example:

```python
age: int = 21
name: str = "Alice"
height: float = 5.9
is_student: bool = True
```

This helps tools understand expected data types.

---

# 3. Using the `typing` Module

Python provides advanced type hints through the `typing` module.

Example:

```python
from typing import List, Dict, Tuple
```

Examples:

```python
numbers: List[int]
student_scores: Dict[str, int]
coordinates: Tuple[int, int]
```

---

# 4. Optional Types

`Optional` indicates that a value may also be `None`.

Example:

```python
from typing import Optional

def find_user(id: int) -> Optional[str]:
```

Equivalent meaning:

```python
Union[str, None]
```

---

# 5. Union Types

`Union` allows multiple possible types.

Example:

```python
from typing import Union

def process(value: Union[int, float]) -> float:
```

This function accepts either:

* integer
* float

---

# 6. Type Aliases

Type aliases allow defining reusable type names.

Example:

```python
Vector = List[float]
```

Usage:

```python
def vector_sum(v: Vector) -> float:
```

This improves readability when dealing with complex types.

---

# 7. TypedDict

`TypedDict` defines the structure of dictionaries.

Example:

```python
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
```

Usage:

```python
user: User = {"name": "Alice", "age": 25}
```

This helps ensure dictionaries follow a defined schema.

---

# 8. Protocols

Protocols enable **structural typing**.

Instead of checking inheritance, Python checks whether an object implements required methods.

Example:

```python
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...
```

Any class with a `draw()` method satisfies this protocol.

Example:

```python
class Circle:
    def draw(self):
        print("Drawing circle")
```

---

# Static Type Checking

Type hints become powerful when used with tools like:

* **mypy**
* **pyright**
* **pylance**

Example command:

```bash
mypy program.py
```

These tools detect type errors before runtime.

---

# Best Practices

1. Use type hints for public functions.
2. Avoid excessive complexity in annotations.
3. Use `Optional` when values may be missing.
4. Use type aliases for complex types.
5. Use static type checkers in large projects.

---

# Summary

Type hints provide optional static typing in Python.

| Feature       | Purpose                      |
| ------------- | ---------------------------- |
| basic hints   | annotate function parameters |
| typing module | advanced types               |
| Optional      | value may be None            |
| Union         | multiple possible types      |
| TypedDict     | structured dictionaries      |
| Protocol      | structural typing            |

Type hints are widely used in modern frameworks such as:

* FastAPI
* Pydantic
* TensorFlow
* PyTorch
