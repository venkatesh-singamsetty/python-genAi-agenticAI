# Python Basics Notes

This README covers **import statements**, **input with eval usage**, and **NumPy basics** in a simple and concise manner.

---

## 1. Import Details

```python
import numpy as np
import sys
```

- `import` is used to include external modules in a program
- `numpy` → numerical and array operations
- `sys` → system-level operations (like command-line arguments)
- `as np` → alias for shorter usage

---

## 2. Input and `eval()` Function

### `input()`

```python
x = input("Enter value: ")
```

- Always returns **string** type

```python
x = int(input("Enter number: "))
```

- Explicit type conversion is required

### `eval()` Usage

```python
x = eval(input("Enter value: "))
```

- Automatically converts input into Python data types
- Can accept:
  - Numbers → `10`
  - List → `[1, 2, 3]`
  - Tuple → `(1, 2)`

⚠️ **Warning:** `eval()` executes expressions, so avoid using it with untrusted input

---

## Summary

- `import` → load modules
- `input()` → string input
- `eval()` → automatic type conversion (use carefully)
