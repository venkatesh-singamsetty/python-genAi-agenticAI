# Python Basics – Data stuctures - list, tuple notes

> Complete notes on Python Lists, Tuples, function usage, and parameter tuning concepts.

---

## Table of Contents
1. [Tab on Function](#tab-on-function)
2. [List – Mutable Data Structure](#list--mutable-data-structure)
    - [Key Properties](#key-properties)
    - [List Methods](#list-methods)
    - [Additional Notes](#additional-notes)
3. [Tuple – Immutable Data Structure](#tuple--immutable-data-structure)
4. [Sorting Rules](#sorting-rules)
5. [Parameter Tuning vs Hyperparameter Tuning](#parameter-tuning-vs-hyperparameter-tuning)
6. [Summary – List vs Tuple](#summary--list-vs-tuple)

---

## Tab on Function
- Press **TAB** after typing a function or variable to see all available in-built functions.
- In interactive Python mode, returned values may be assigned to `_`.

---

## List – Mutable Data Structure

### Key Properties
- Defined using: `l = []`
- **Mutable** → values can be changed.
- Supports **multiple datatypes** (heterogeneous).
- **Duplication allowed**.
- **Growable** data structure.
- Sorting works **only when all elements are of similar datatype**.
- Sorting is **not possible** for mixed datatypes.

### List Methods
- `append()` – Add value at the end of the list.
- `copy()` – Copy one list to another.
- `clear()` – Remove all elements from the list.
- `del` keyword – Delete variable or a specific index.
- `insert()` – Insert value before an index.
- `pop()` – Remove element by index; default removes last element.
- `remove()` – Remove element by value.
- `reverse()` – Reverse the list.
- `extend()` – Merge one list into another.
- `sort()` – Sort list in ascending/descending order (only if same datatype).

### Additional Notes
- `pop()` removes elements by **index**.
- `remove()` removes elements by **value**.
- Sorting mixed datatype lists raises an error.
- List is fully editable and supports all CRUD operations.

---

## Tuple – Immutable Data Structure

### Key Properties
- Defined using: `t = ()`
- **Immutable** → values cannot be changed.
- Supports **multiple datatypes**.
- **Duplication allowed**.
- Indexing and slicing allowed.
- `count()` method available.

---

## Sorting Rules
- Sorting is **not possible** if list contains mixed datatypes.
- Sorting **is possible** only when all elements are of similar datatype.

---

## Parameter Tuning vs Hyperparameter Tuning

### Parameter Tuning
- System automatically provides parameters.
- Example: Laptop comes with Windows 11 OS by default.

### Hyperparameter Tuning
- User modifies system parameters.
- Example: Installing Windows 10 manually.

### Machine Learning Note
- Hyperparameter tuning helps improve ML model accuracy.

---

## Summary – List vs Tuple

| Feature | List | Tuple |
|--------|------|--------|
| Mutability | Mutable | Immutable |
| Growable | Yes | No |
| Duplication | Allowed | Allowed |
| Heterogeneous Types | Allowed | Allowed |
| Indexing | Yes | Yes |
| Slicing | Yes | Yes |
| Methods | Many | Few |
| Use Case | Dynamic data | Fixed/constant data |
