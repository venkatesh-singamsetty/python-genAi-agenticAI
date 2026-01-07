# Python Operators & Number System

## 1. Operators in Python
Operators are symbols used to perform operations on variables and values.

---

## 2. Types of Operators

### 2.1 Arithmetic Operators
Used for mathematical operations.

| Operator | Description | Example |
|--------|------------|---------|
| + | Addition | a + b |
| - | Subtraction | a - b |
| * | Multiplication | a * b |
| / | Division | a / b |
| % | Modulus | a % b |
| // | Floor Division | a // b |
| ** | Power | a ** b |

---

### 2.2 Relational (Comparison) Operators
Used to compare two values. Always returns True or False.

| Operator | Meaning |
|--------|--------|
| == | Equal to |
| != | Not equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |

Example:
```python
a = 10
b = 20
print(a > b)  # False
```

---

### 2.3 Logical Operators
Used to combine conditions.

| Operator | Description |
|--------|-------------|
| and | True if both conditions are True |
| or | True if any condition is True |
| not | Reverses the result |

Example:
```python
a = 10
b = 20
print(a > 5 and b > 15)  # True
```

---

### 2.4 Assignment Operators

| Operator | Example |
|--------|---------|
| = | a = 10 |
| += | a += 5 |
| -= | a -= 5 |
| *= | a *= 5 |
| /= | a /= 5 |

---

### 2.5 Swap Variables
```python
a = 10
b = 20
a, b = b, a
print(a, b)
```

---

## 3. Bitwise Operators
Operate on binary numbers.

| Operator | Name |
|--------|------|
| ~ | Complement |
| & | AND |
| \| | OR |
| ^ | XOR |
| << | Left Shift - x * (2^n)|
| >> | Right Shift - x // (2^n)|

Example:
```python
a = 5
b = 3
print(a & b)
print(a | b)
```

---

## 4. Number System in Python

  | Number System   | Base   | Prefix        | Example      |
  | --------------- | ------ | ------------- | ------------ |
  | Binary          | 2      | `0b`          | `0b1010` |
  | Octal           | 8      | `0o`          | `0o17` |
  | Decimal         | 10     | *no prefix*   | `100` |
  | Hexadecimal     | 16     | `0x`          | `0xabcdef` |

### 4.1 Decimal (Base 10)
```python
a = 10
```

### 4.2 Binary (Base 2)
Prefix: 0b
```python
a = 0b1010
print(a)
```

### 4.3 Octal (Base 8)
Prefix: 0o
```python
a = 0o12
print(a)
```

### 4.4 Hexadecimal (Base 16)
Prefix: 0x
```python
a = 0xA
print(a)
```
