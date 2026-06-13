# HackerRank - itertools.combinations()

## Problem Statement

You are given a string `S` and an integer `K`.

Print all possible combinations of the characters of `S` for lengths from `1` to `K` in lexicographic sorted order.

### Sample Input
```
HACK 2
```

### Sample Output
```
A
C
H
K
AC
AH
AK
CH
CK
HK
```

## Explanation

1. Sort the input string lexicographically.
2. Generate combinations of size `1` to `K`.
3. Print each combination on a new line.

For the input `HACK 2`, the sorted string is `ACHK`.

Combinations of length 1:
```
A
C
H
K
```

Combinations of length 2:
```
AC
AH
AK
CH
CK
HK
```

## Solution

```python
from itertools import combinations

s, k = input().split()
k = int(k)

s = ''.join(sorted(s))

for i in range(1, k + 1):
    for comb in combinations(s, i):
        print(''.join(comb))
```

## Time Complexity

- Sorting: O(N log N)
- Combination generation: O(Σ C(N, r)) for r = 1 to K

## Concepts Used

- `itertools.combinations()`
- String sorting
- Nested loops
- Lexicographic order

## Author

Shubham Gupta