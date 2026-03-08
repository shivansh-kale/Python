"""
BUILDING CLI TOOLS IN PYTHON
----------------------------

Command Line Interface (CLI) tools allow users to interact
with programs from the terminal.

This file covers:

1. Command-line arguments with sys
2. argparse module
3. Building structured CLI commands
4. Using Typer (modern CLI framework)

CLI tools are widely used in:
- automation scripts
- data pipelines
- developer tools
"""

# =========================================================
# 1. COMMAND LINE ARGUMENTS USING SYS
# =========================================================

"""
The sys module provides access to command line arguments.
"""

import sys

print("Command-line arguments:", sys.argv)

# Example usage:
# python script.py hello world


# =========================================================
# 2. ARGPARSE MODULE
# =========================================================

"""
argparse helps build structured command-line interfaces.
"""

import argparse

parser = argparse.ArgumentParser(description="Simple CLI calculator")

parser.add_argument("--a", type=int, help="First number")
parser.add_argument("--b", type=int, help="Second number")

args = parser.parse_args()

if args.a and args.b:
    print("Sum:", args.a + args.b)


# =========================================================
# 3. SUBCOMMANDS
# =========================================================

"""
CLI tools often support subcommands.
Example: git commit, git push
"""

parser = argparse.ArgumentParser(description="Math CLI Tool")

subparsers = parser.add_subparsers(dest="command")

# Add command
add_parser = subparsers.add_parser("add")
add_parser.add_argument("x", type=int)
add_parser.add_argument("y", type=int)

# Multiply command
mul_parser = subparsers.add_parser("multiply")
mul_parser.add_argument("x", type=int)
mul_parser.add_argument("y", type=int)

args = parser.parse_args()

if args.command == "add":
    print(args.x + args.y)

elif args.command == "multiply":
    print(args.x * args.y)


# =========================================================
# 4. BUILDING CLI WITH TYPER
# =========================================================

"""
Typer is a modern library for building CLI tools easily.
"""

# pip install typer

import typer

app = typer.Typer()


@app.command()
def greet(name: str):
    """
    Simple CLI greeting command
    """
    print(f"Hello {name}!")


@app.command()
def square(number: int):
    """
    Square a number
    """
    print(number ** 2)


if __name__ == "__main__":
    app()