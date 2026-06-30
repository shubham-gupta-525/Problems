# Itertools Combinations With Replacement

## Problem Statement

You are given a string `S` and an integer `K`.

Your task is to print all possible size `K` combinations of the string's characters, allowing individual characters to be repeated more than once.

The combinations must be printed in **lexicographic sorted order**, one per line.

---

## Example

### Input

```
HACK 2
```

### Output

```
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
```

---

## Approach

1. Read the input string and integer `K`.
2. Sort the string to ensure lexicographic order.
3. Use `itertools.combinations_with_replacement()` to generate all possible combinations of length `K`.
4. Join each tuple into a string and print it.

---

## Python Solution

```python
from itertools import combinations_with_replacement

s, k = input().split()
k = int(k)

for comb in combinations_with_replacement(sorted(s), k):
    print(''.join(comb))
```

---

## Complexity Analysis

* Let `n` be the length of the string.
* Time Complexity: `O(C(n + k - 1, k))`
* Space Complexity: `O(1)` (excluding output storage)

---

## Key Concept

`combinations_with_replacement(iterable, r)` generates combinations where elements can be repeated.

Example:

```python
from itertools import combinations_with_replacement

print(list(combinations_with_replacement('ABC', 2)))
```

Output:

```python
[('A', 'A'), ('A', 'B'), ('A', 'C'),
 ('B', 'B'), ('B', 'C'),
 ('C', 'C')]
```
