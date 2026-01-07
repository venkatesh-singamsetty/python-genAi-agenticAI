# Python Data Structures -- Quick Guide

## Dictionary

**Format to define a dictionary:**

``` python
my_dict = {key: value}
```

-   Keys are **more important** than values.
-   Keys must be **unique** and **immutable**.
-   Dictionaries are **mutable**.


## range() -- 3 Arguments

1.  start
2.  stop
3.  step

``` python
range(10)
range(2, 10)
range(1, 20, 2)
```

## list vs tuple vs set vs dict vs range

| Feature    | list         | tuple      | set           | dict             | range         |
| ---------- | ------------ | ---------- | ------------- | ---------------- | ------------- |
| Mutable    | ✔            | ✖          | ✔             | ✔                | ✖             |
| Ordered    | ✔            | ✔          | ✖             | ✔                | ✔             |
| Indexing   | ✔            | ✔          | ✖             | Keys only        | ✔             |
| Duplicates | ✔            | ✔          | ✖             | Keys ✖           | ✔             |
| Type       | Sequence     | Sequence   | Collection    | Mapping          | Sequence      |
| Ideal For  | Dynamic data | Fixed data | Unique values | Key-value lookup | Numeric loops |
