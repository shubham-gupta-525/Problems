# Set .union() Operation - HackerRank Solution

## Overview

This repository contains a Python solution for the **Set .union() Operation** challenge from HackerRank's **Python Sets** section.

The objective is to determine the total number of students who have subscribed to **at least one** newspaper (English or French) using the `union()` method.

---

## Problem Statement

Students in a college subscribe to either:

- English newspaper
- French newspaper
- Both newspapers

You are given two sets containing the roll numbers of students subscribed to each newspaper.

Your task is to find the total number of **unique** students who have subscribed to at least one newspaper.

---

## Example

### Input

```text
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```

### Output

```text
13
```

---

## Approach

The solution uses Python's built-in **set** data structure.

### Steps

1. Read the English newspaper subscribers.
2. Read the French newspaper subscribers.
3. Convert both lists into sets.
4. Use the `union()` method to combine both sets.
5. Print the size of the resulting set.

Since sets automatically remove duplicate elements, students subscribed to both newspapers are counted only once.

---

## Algorithm

```text
Read English subscribers
Read French subscribers

Convert both lists into sets

Union = English ∪ French

Print size of Union
```

---

## Python Solution

```python
# Enter your code here. Read input from STDIN. Print output to STDOUT

english = input()
roll_e = set(map(int, input().split()))

french = input()
roll_f = set(map(int, input().split()))

answer = roll_e.union(roll_f)
print(len(answer))
```

---

## Alternative Solution

The union operator (`|`) can also be used.

```python
english = int(input())
roll_e = set(map(int, input().split()))

french = int(input())
roll_f = set(map(int, input().split()))

print(len(roll_e | roll_f))
```

---

## Time Complexity

Creating each set:

```
O(n)
```

Union operation:

```
O(n + m)
```

Overall:

```
O(n + m)
```

where:

- **n** = Number of English subscribers
- **m** = Number of French subscribers

---

## Space Complexity

```
O(n + m)
```

The union creates a new set containing all unique roll numbers.

---

## Concepts Used

- Python Sets
- `set()`
- `map()`
- `union()`
- `len()`
- Input Handling

---

## Key Python Methods

### Creating a Set

```python
numbers = set([1, 2, 3])
```

### Using `union()`

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
```

Output

```text
{1, 2, 3, 4, 5}
```

### Using the `|` Operator

```python
print(A | B)
```

Produces the same result.

---

## Learning Outcomes

- Understanding Python sets.
- Removing duplicate values automatically.
- Using the `union()` method.
- Using the `|` operator for set union.
- Calculating the number of unique elements.

---

## Platform

- **Platform:** HackerRank
- **Track:** Python
- **Section:** Sets
- **Challenge:** Set .union() Operation

---

## Author

**Your Name**

GitHub: *your-github-username*