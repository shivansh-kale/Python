"""
TYPE HINTS AND STATIC TYPING IN PYTHON
--------------------------------------

Type hints allow developers to specify expected data types
for variables, function arguments, and return values.

Benefits:
- improves code readability
- helps detect bugs early
- enables static analysis tools like mypy
"""

# =========================================================
# BASIC TYPE HINTS
# =========================================================

"""
Basic type annotations can be added to variables and functions.
"""

def add(a: int, b: int) -> int:
    return a + b

result = add(5, 3)

print(result)


# =========================================================
# TYPE HINTS FOR VARIABLES
# =========================================================

age: int = 21
name: str = "Shivansh"
height: float = 6.1
is_student: bool = True

print(age, name, height, is_student)


# =========================================================
# USING TYPING MODULE
# =========================================================

"""
The typing module provides advanced types.
"""

from typing import List, Dict, Tuple

# List type
numbers: List[int] = [1, 2, 3, 4]

# Dictionary type
student: Dict[str, int] = {"math": 90, "science": 85}

# Tuple type
coordinates: Tuple[int, int] = (10, 20)

print(numbers, student, coordinates)


# =========================================================
# OPTIONAL TYPE
# =========================================================

"""
Optional means the value may also be None.
"""

from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None

print(find_user(1))
print(find_user(2))


# =========================================================
# UNION TYPE
# =========================================================

"""
Union allows multiple possible types.
"""

from typing import Union

def process(value: Union[int, float]) -> float:
    return value * 2

print(process(5))
print(process(3.5))


# =========================================================
# TYPE ALIASES
# =========================================================

"""
Type aliases create reusable type definitions.
"""

from typing import List

Vector = List[float]

def vector_sum(v: Vector) -> float:
    return sum(v)

print(vector_sum([1.0, 2.0, 3.0]))


# =========================================================
# TYPEDDICT
# =========================================================

"""
TypedDict allows defining dictionary structure with types.
"""

from typing import TypedDict

class User(TypedDict):
    name: str
    age: int
    city: str

user: User = {
    "name": "Alice",
    "age": 25,
    "city": "London"
}

print(user)


# =========================================================
# PROTOCOL (STRUCTURAL TYPING)
# =========================================================

"""
Protocols define required methods for objects.
"""

from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        ...


class Circle:
    def draw(self) -> None:
        print("Drawing circle")


def render(shape: Drawable):
    shape.draw()


circle = Circle()
render(circle)