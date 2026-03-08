# Building CLI Tools in Python

Command Line Interface (CLI) tools allow users to interact with programs directly from the terminal.

Examples of CLI tools include:

* `pip`
* `pytest`
* `git`
* `docker`

Python makes it easy to build CLI tools using several libraries.

---

# 1. Command Line Arguments with sys

The simplest way to access command-line arguments is using the `sys` module.

Example:

```python
import sys

print(sys.argv)
```

Example command:

```bash
python script.py hello world
```

Output:

```text
['script.py', 'hello', 'world']
```

However, `sys.argv` is limited and lacks structured parsing.

---

# 2. argparse

The `argparse` module provides a robust way to build command-line interfaces.

Example:

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--name")

args = parser.parse_args()

print(args.name)
```

Run:

```bash
python script.py --name Alice
```

Advantages of argparse:

* structured arguments
* automatic help messages
* argument validation

---

# 3. Subcommands

Many CLI tools use subcommands.

Example:

```bash
git commit
git push
git pull
```

Using argparse:

```python
subparsers = parser.add_subparsers()
```

Subcommands help organize complex CLI tools.

---

# 4. Typer (Modern CLI Framework)

Typer is a modern library for building CLI applications with minimal code.

Install Typer:

```bash
pip install typer
```

Example:

```python
import typer

app = typer.Typer()

@app.command()
def greet(name: str):
    print(f"Hello {name}")
```

Run:

```bash
python app.py greet Alice
```

Advantages of Typer:

* simple syntax
* automatic documentation
* built-in type validation

---

# CLI Tool Structure

Example CLI project structure:

```text
cli_tool/
│
├── cli_tool/
│   ├── __init__.py
│   └── main.py
│
├── pyproject.toml
└── README.md
```

CLI tools can also be installed as packages.

---

# Best Practices

1. Provide clear help messages.
2. Use subcommands for complex tools.
3. Validate input arguments.
4. Use libraries like Typer or Click for advanced CLIs.

---

# Summary

Python provides multiple ways to build CLI tools.

| Method   | Use Case             |
| -------- | -------------------- |
| sys.argv | simple scripts       |
| argparse | structured CLI       |
| Typer    | modern CLI framework |

CLI tools are widely used in **automation, DevOps, and machine learning workflows**.
