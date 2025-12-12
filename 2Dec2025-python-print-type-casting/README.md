
---

# Python Type Casting & Print Formatting

## Type Casting Rules in Python

### Casting to **int**
You can type cast to `int` from other datatypes **except**:
- `complex`
- `text strings` (non-numeric strings)

### Casting to **float**
You can type cast to `float` from other datatypes **except**:
- `complex`
- `text strings` (non-numeric strings)

### Casting to **complex**
You can type cast to `complex` from other datatypes **except**:
- `string parameters` (example: "10,20")
- `text strings` (non-numeric strings)

### Casting to **string**
You can type cast **any datatype** to `string` without any issue.

### Casting to **bool**
You can type cast **any datatype** to `bool` without any issue.

---

## Print Formatting in Python

### **Normal print statement**
```python
print('The addition of', num1, 'and', num2, 'is=', add)
```

### Using Format String (str.format)
```python
print('The addition of {} and {} and {} is= {}'.format(num1, num2, num3, add))
```

### Using F-String (Recommended)
```python
print(f'The addition of {num1} and {num2} and {num3} is= {add}')
```
