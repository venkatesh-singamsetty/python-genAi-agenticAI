# Pandas --- Notes

## Data Structures

-   **DataFrame**
    -   2D data structure
    -   Contains rows and columns
-   **Series**
    -   1D data structure
    -   Represents a single row or a single column

------------------------------------------------------------------------

## Column Selection

``` python
tags['tag']      # Series
tags[['tag']]    # DataFrame
```

-   **Single bracket `[ ]`**
    -   Returns a Series
-   **Double bracket `[[ ]]`**
    -   Returns a DataFrame

------------------------------------------------------------------------

## Summary

-   Series → 1D
-   DataFrame → 2D
-   `[ ]` → Series
-   `[[ ]]` → DataFrame
