"""
TESTING IN PYTHON
-----------------

This file demonstrates basic testing techniques in Python.

Topics covered:

1. Why testing is important
2. Writing simple tests
3. Using pytest
4. Assertions
5. Fixtures
6. Mocking basics

Testing ensures code behaves correctly and prevents bugs.
"""


# =========================================================
# 1. SIMPLE FUNCTION TO TEST
# =========================================================

def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# =========================================================
# 2. BASIC ASSERTIONS
# =========================================================

"""
Assertions check whether a condition is true.
"""

assert add(2, 3) == 5
assert divide(10, 2) == 5

print("Basic assertions passed")


# =========================================================
# 3. PYTEST STYLE TEST FUNCTIONS
# =========================================================

"""
Pytest automatically discovers functions that start with 'test_'.
"""

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_divide():
    assert divide(10, 2) == 5


# =========================================================
# 4. TESTING EXCEPTIONS
# =========================================================

import pytest


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# =========================================================
# 5. FIXTURES
# =========================================================

"""
Fixtures provide reusable test setup.
"""

@pytest.fixture
def sample_numbers():
    return [1, 2, 3, 4]


def test_sum(sample_numbers):
    assert sum(sample_numbers) == 10


# =========================================================
# 6. MOCKING EXAMPLE
# =========================================================

"""
Mocking allows replacing real dependencies during testing.
"""

from unittest.mock import Mock


def get_data(api_client):
    return api_client.fetch_data()


def test_mock_api():
    mock_client = Mock()
    mock_client.fetch_data.return_value = {"data": 123}

    result = get_data(mock_client)

    assert result["data"] == 123