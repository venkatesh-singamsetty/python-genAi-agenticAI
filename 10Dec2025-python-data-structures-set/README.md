# Python Sets -- Complete Reference

This README provides a consolidated guide to Python **set** behavior,
properties, and operations.

------------------------------------------------------------------------

## 🧱 What is a Set?

A **set** in Python is:

-   **Unordered**
-   **Unindexed**
-   **Mutable** (you can add/remove elements)
-   **No duplicate values allowed**
-   Elements must be **immutable** (int, float, str, tuple)

------------------------------------------------------------------------

## 🔁 Set Behaves as Both Mutable & Immutable

-   A **set is mutable** → you can modify it after creation.\
-   **Elements inside a set must be immutable**.

Example (valid):

``` python
s = {1, 2, "hello", (1, 2)}
```

Invalid:

``` python
s = {[1, 2]}   # ❌ list is mutable → cannot store in set
```

------------------------------------------------------------------------

## 📌 Ordering Rule

-   A set **never guarantees order**.
-   Even if elements are of the **same datatype**, the order is not
    preserved.

``` python
s = {10, 20, 30}
print(s)   # Output may vary
```

------------------------------------------------------------------------

## ➕ add()

-   Used to add an element to a set.
-   Ignores duplicates.

``` python
my_set.add(10)
```

------------------------------------------------------------------------

## ❌ remove() vs discard()

### **discard()**

-   Safe method\
-   **Does NOT throw an error** if the element does not exist

``` python
s.discard(5)  # No error even if 5 not present
```

### **remove()**

-   Throws **KeyError** if the element does not exist

``` python
s.remove(5)  # ❌ KeyError if 5 not found
```

------------------------------------------------------------------------

## 🔀 Set Operations

### **1. Union (`|`)**

``` python
result = A | B
```

### **2. Intersection (`&`)**

``` python
result = A & B
```

### **3. Difference (`-`)**

``` python
result = A - B
```

### **4. Symmetric Difference (`^`)**

``` python
result = A ^ B
```

------------------------------------------------------------------------

## 👨‍👦 Relationship Methods

  Method             Meaning               Example             Memory Trick
  ------------------ --------------------- ------------------- --------------
  **issuperset()**   A contains all of B   `A.issuperset(B)`   Dad
  **issubset()**     A is inside B         `A.issubset(B)`     Son
  **isdisjoint()**   No common values      `A.isdisjoint(B)`   Neighbour
