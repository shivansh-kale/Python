---

#  Example Workflow (UV)

## 1️ Create a New Project

```bash
uv init demo_project
cd demo_project
```

Project structure:

```text
demo_project/
│
├── pyproject.toml
├── uv.lock
├── .venv/
└── src/
    └── demo_project/
        └── main.py
```

---

## 2️ Create Virtual Environment

```bash
uv venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
uv add numpy pandas
```

Automatically updates:

- 📄 `pyproject.toml`
- 🔒 `uv.lock`

---

## 4️. Write Some Code

```python
# main.py

import numpy as np
import pandas as pd

arr = np.array([10, 20, 30])

df = pd.DataFrame({
    "Numbers": arr
})

print(df)
print(arr.mean())
```

Output

```text
   Numbers
0       10
1       20
2       30

20.0
```

---

## 5️. Run the Program

```bash
uv run main.py
```

>  No need to manually activate the virtual environment.

---

## 6️. Share Your Project

Another developer only needs:

```bash
git clone <repo>
cd demo_project

uv sync
uv run main.py
```

`uv sync` automatically:

-  Creates `.venv`
-  Installs all dependencies
-  Uses versions from `uv.lock`

---

#  Typical Modern Workflow

```text
uv init my_project
        │
        ▼
uv venv
        │
        ▼
uv add numpy pandas
        │
        ▼
Write Code (main.py)
        │
        ▼
uv run main.py
        │
        ▼
git push
        │
        ▼
Other Developer
        │
        ▼
git clone
        │
        ▼
uv sync
        │
        ▼
uv run main.py
```

---

##  Migration from pip

| Old Workflow | UV Workflow |
|--------------|-------------|
| `python -m venv .venv` | `uv venv` |
| `pip install numpy` | `uv add numpy` |
| `pip freeze > requirements.txt` | `uv.lock` (automatic) |
| `pip install -r requirements.txt` | `uv sync` |
| `python main.py` | `uv run main.py` |
