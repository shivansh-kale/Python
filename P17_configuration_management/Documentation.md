# Configuration Management in Python

Configuration management allows developers to separate application settings from the main program logic.

This improves:

* maintainability
* security
* portability
* deployment flexibility

Common configuration techniques include:

* environment variables
* `.env` files
* JSON or YAML configuration files
* configuration classes

---

# 1. Environment Variables

Environment variables store configuration outside the application code.

Example:

```python
import os

database_url = os.getenv("DATABASE_URL")
```

Advantages:

* secure storage for secrets
* easy to change without modifying code
* commonly used in production environments

Example use cases:

* API keys
* database URLs
* application modes

---

# 2. `.env` Files

`.env` files store environment variables in a file.

Example `.env` file:

```text
DATABASE_URL=postgres://user:pass@localhost/db
API_KEY=secret_key
```

Using `python-dotenv`:

```python
from dotenv import load_dotenv
load_dotenv()
```

Advantages:

* convenient for development
* avoids hardcoding secrets

---

# 3. JSON Configuration Files

JSON is commonly used to store configuration settings.

Example:

```json
{
  "debug": true,
  "batch_size": 32
}
```

Loading JSON configuration:

```python
import json

with open("config.json") as f:
    config = json.load(f)
```

Advantages:

* structured data
* widely supported

---

# 4. YAML Configuration Files

YAML is often preferred for configuration because it is easier to read.

Example:

```yaml
learning_rate: 0.001
epochs: 10
```

Loading YAML:

```python
import yaml

yaml.safe_load(file)
```

YAML is commonly used in:

* ML experiments
* Docker configuration
* Kubernetes
* CI/CD pipelines

---

# 5. Configuration Classes

Configuration classes centralize application settings.

Example:

```python
class Config:
    DEBUG = True
    DATABASE_URL = "sqlite://local.db"
```

Advantages:

* structured configuration
* easy to access throughout application

---

# Best Practices

1. Never hardcode secrets in source code.
2. Use environment variables for sensitive data.
3. Use `.env` files during development.
4. Store application settings in configuration files.
5. Use configuration classes for structured access.

---

# Summary

Configuration management separates settings from application code.

| Method                | Purpose                      |
| --------------------- | ---------------------------- |
| environment variables | store runtime configuration  |
| `.env` files          | local development settings   |
| JSON                  | structured configuration     |
| YAML                  | human-readable configuration |
| configuration classes | centralized settings         |

These techniques are widely used in **ML pipelines, APIs, and production systems**.
