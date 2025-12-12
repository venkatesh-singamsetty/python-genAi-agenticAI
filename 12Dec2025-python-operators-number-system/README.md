# 📝 Python Notes --- Operators, Number Systems & Bitwise Operations

## 1. Comparing Two Variables

To compare variables, Python uses relational and logical operators.

### Relational Operators

  | Operator   | Meaning                    |
  | ---------- | -------------------------- |
  | `==`       | Equal to |
  | `!=`       | Not equal to |
  | `>`        | Greater than |
  | `<`        | Less than |
  | `>=`       | Greater than or equal to |
  | `<=`       | Less than or equal to |

### Logical Operators

  | Operator | Meaning |
  ---------- | --------------------------------------- |
  | `and`    | True only if both conditions are True |
  | `or`     | True if any one condition is True |
  | `not`    | Reverses Boolean value |

## 2. Number Systems in Python

  | Number System   | Base   | Prefix        | Example      |
  | --------------- | ------ | ------------- | ------------ |
  | Binary          | 2      | `0b`          | `0b1010` |
  | Octal           | 8      | `0o`          | `0o17` |
  | Decimal         | 10     | *no prefix*   | `100` |
  | Hexadecimal     | 16     | `0x`          | `0xabcdef` |

Hex digits mapping: a=10, b=11, c=12, d=13, e=14, f=15.

## 3. Bitwise Operators in Python

### COMPLEMENT ( \~ )

`~x = -(x+1)`

### AND ( & )

Bitwise AND --- 1 only if both bits are 1.

### OR ( \| )

Bitwise OR --- 1 if any bit is 1.

### XOR ( \^ )

Exclusive OR --- 1 if bits are different.

### LEFT SHIFT ( \<\< )

`x << n = x * (2^n)`

### RIGHT SHIFT ( \>\> )

`x >> n = x // (2^n)`
