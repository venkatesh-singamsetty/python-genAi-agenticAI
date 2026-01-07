- PyCharm Debugging (F8 – Step Over)
  - What does F8 do?
   - F8 = Step Over
   - Executes the current line completely and moves to the next line
   - Does not go inside functions


```python
# number is even or odd

x = 4
r = x % 2

if r == 0:
    print("Even")
```

geeksforgeeks.org/conditions-in-python



```python
# nested while

i = 1
while i <= 4:
    j = 0
    while j < 3:
        print(i * j, end=" ")
        j += 1
    print()
    i += 1
```

- `while` -> condition-based looping -> You manage increment manually
- `for` -> sequence-based looping -> manage increment automatically -> List, Tuple, Set, Dictionary, String, Range
