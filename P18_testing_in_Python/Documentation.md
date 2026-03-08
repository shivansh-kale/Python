# Testing in Python

Testing ensures that code behaves correctly and prevents bugs from entering production systems.

In modern Python development, testing is considered an essential practice.

Benefits of testing include:

* improved reliability
* easier debugging
* safer refactoring
* better code quality

---

# 1. Why Testing is Important

Without testing, small changes in code may introduce hidden bugs.

Testing allows developers to verify that code behaves as expected.

Example function:

```python
def add(a, b):
    return a + b
```

Testing ensures the function always returns the correct result.

---

# 2. Assertions

Assertions verify that conditions are true.

Example:

```python
assert add(2,3) == 5
```

If the condition fails, Python raises an `AssertionError`.

Assertions are useful for simple testing scenarios.

---

# 3. Pytest

`pytest` is the most popular Python testing framework.

Install pytest:

```bash
pip install pytest
```

Example test:

```python
def test_add():
    assert add(2,3) == 5
```

Run tests:

```bash
pytest
```

Pytest automatically discovers test functions that start with `test_`.

---

# 4. Testing Exceptions

Tests should verify that functions correctly handle errors.

Example:

```python
import pytest

with pytest.raises(ValueError):
    divide(10,0)
```

This confirms that the function raises the expected exception.

---

# 5. Fixtures

Fixtures provide reusable setup for tests.

Example:

```python
@pytest.fixture
def sample_data():
    return [1,2,3]
```

Usage:

```python
def test_sum(sample_data):
    assert sum(sample_data) == 6
```

Fixtures reduce duplicate test setup code.

---

# 6. Mocking

Mocking replaces real dependencies during tests.

Example:

```python
from unittest.mock import Mock
```

Mocking is useful when:

* testing APIs
* testing databases
* simulating external services

Example:

```python
mock_client = Mock()
mock_client.fetch_data.return_value = {"data":123}
```

---

# 7. Test Structure

Typical project structure:

```text
project/
│
├── app/
│   └── functions.py
│
└── tests/
    └── test_functions.py
```

Tests should be kept separate from production code.

---

# Best Practices

1. Write tests for critical logic.
2. Keep tests small and focused.
3. Use fixtures for reusable setup.
4. Use mocks for external dependencies.
5. Run tests automatically in CI pipelines.

---

# Summary

Testing ensures that programs behave correctly.

| Tool     | Purpose               |
| -------- | --------------------- |
| assert   | simple checks         |
| pytest   | testing framework     |
| fixtures | reusable setup        |
| mocking  | simulate dependencies |

Testing is widely used in **production Python systems, ML pipelines, and backend services**.
