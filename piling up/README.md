# Piling Up! - HackerRank Solution

## Overview

This repository contains a Python solution for the **Piling Up!** challenge from HackerRank's **Python Collections** section.

The objective is to determine whether a vertical pile of cubes can be built by selecting cubes only from the **leftmost** or **rightmost** end of a horizontal row while maintaining a non-increasing order of cube sizes.

---

## Problem Statement

Given a row of cubes with different side lengths, build a vertical pile by repeatedly choosing a cube from either end of the row.

A cube can only be placed on top of another cube if:

```
Top Cube Size ≤ Bottom Cube Size
```

For each test case, print:

- **Yes** – if a valid pile can be built.
- **No** – otherwise.

---

## Example

### Input

```text
2
6
4 3 2 1 3 4
3
1 3 2
```

### Output

```text
Yes
No
```

---

## Approach

This solution uses a **Greedy Algorithm**.

### Steps

1. Initialize the maximum allowed cube size as positive infinity.
2. Compare the leftmost and rightmost cubes.
3. Select the larger of the two.
4. If the selected cube is larger than the previously placed cube, stacking is impossible.
5. Otherwise, place the cube on the pile and continue until all cubes are processed.

---

## Algorithm

```text
Set last = ∞

While cubes remain:
    Compare leftmost and rightmost cubes.
    Pick the larger cube.

    If selected cube > last:
        Print "No"
        Stop.

    last = selected cube

If all cubes are processed:
    Print "Yes"
```

---

## Python Solution

```python
from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            print("No")
            break

        last = current
    else:
        print("Yes")
```

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| Processing each cube once | **O(n)** |

Overall complexity per test case:

```
O(n)
```

---

## Space Complexity

```
O(n)
```

A `deque` is used to efficiently remove elements from both ends.

---

## Concepts Used

- Python Collections (`deque`)
- Greedy Algorithm
- Conditional Statements
- Loops
- Input Handling

---

## Key Python Features

- `collections.deque`
- `popleft()`
- `pop()`
- `float('inf')`
- `while` loop
- `break`
- `while...else`

---

## Why `float('inf')`?

```python
last = float('inf')
```

The first selected cube can be any size because every cube size is less than infinity.

This avoids having to treat the first iteration as a special case.

---

## Learning Outcomes

- Solving greedy algorithm problems.
- Using `deque` for efficient operations on both ends of a sequence.
- Understanding `while...else` in Python.
- Improving algorithm efficiency from **O(n²)** (using list slicing) to **O(n)**.

---

## Platform

- **Platform:** HackerRank
- **Track:** Python
- **Section:** Collections
- **Challenge:** Piling Up!

---

## Author

**Your Name**

GitHub: *your-github-username*