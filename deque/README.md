# Collections.deque() in Python

## Problem Statement

A deque (double-ended queue) is a data structure that allows insertion and deletion of elements from both ends efficiently.

You are given a series of operations to perform on an initially empty deque. The supported operations are:

* `append x` : Add `x` to the right end of the deque.
* `appendleft x` : Add `x` to the left end of the deque.
* `pop` : Remove an element from the right end of the deque.
* `popleft` : Remove an element from the left end of the deque.

After performing all operations, print the contents of the deque as space-separated values.

---

## Python Solution

```python
from collections import deque

d = deque()

n = int(input())

for _ in range(n):
    operation = input().split()

    if operation[0] == "append":
        d.append(operation[1])

    elif operation[0] == "appendleft":
        d.appendleft(operation[1])

    elif operation[0] == "pop":
        d.pop()

    elif operation[0] == "popleft":
        d.popleft()

print(*d)
```

---

## Example

### Input

```
6
append 1
append 2
append 3
appendleft 4
pop
popleft
```

### Output

```
1 2
```

---

## Explanation

Initial deque:

```
[]
```

Operations:

1. `append 1` → `[1]`
2. `append 2` → `[1, 2]`
3. `append 3` → `[1, 2, 3]`
4. `appendleft 4` → `[4, 1, 2, 3]`
5. `pop` → `[4, 1, 2]`
6. `popleft` → `[1, 2]`

Final Output:

```
1 2
```

---

## Time Complexity

| Operation  | Complexity |
| ---------- | ---------- |
| append     | O(1)       |
| appendleft | O(1)       |
| pop        | O(1)       |
| popleft    | O(1)       |

Overall Complexity: **O(n)**

---

## Concepts Used

* Python Collections Module
* deque Data Structure
* Conditional Statements
* Input Processing
* Queue Operations

---

