# Symmetric Difference of Two Sets

## Overview

The **Symmetric Difference of Two Sets** program demonstrates the use of Python sets to find elements that exist in either of two sets but not in both.

This project helps in understanding set operations such as `difference()`, `union()`, and `symmetric_difference()`.

---

## Problem Statement

Given two sets of integers, **A** and **B**, print their symmetric difference in ascending order.

The symmetric difference contains all elements that are present in either set but not in both sets.

---

## Input Format

* First line contains an integer **M** (size of set A)
* Second line contains **M** space-separated integers
* Third line contains an integer **N** (size of set B)
* Fourth line contains **N** space-separated integers

---

## Output Format

Print the symmetric difference of the two sets in ascending order, one integer per line.

---

## Example

### Input

```text
4
2 4 5 9
4
2 4 11 12
```

### Output

```text
5
9
11
12
```

---

## Explanation

Set A = {2, 4, 5, 9}

Set B = {2, 4, 11, 12}

Common elements = {2, 4}

Elements present only in Set A = {5, 9}

Elements present only in Set B = {11, 12}

Symmetric Difference = {5, 9, 11, 12}

After sorting in ascending order:

```text
5
9
11
12
```

---

## Python Solution

```python
m = int(input())
set1 = set(map(int, input().split()))

n = int(input())
set2 = set(map(int, input().split()))

result = set1.symmetric_difference(set2)

for num in sorted(result):
    print(num)
```

---

## Time Complexity

* Creating Sets: O(M + N)
* Finding Symmetric Difference: O(M + N)
* Sorting Result: O(K log K)

Where:

* M = size of first set
* N = size of second set
* K = number of elements in the symmetric difference

---

## Concepts Used

* Python Sets
* Set Operations
* Symmetric Difference
* Sorting
* Input Handling

---

## Learning Outcomes

By completing this project, you will learn:

* How to create and manipulate sets in Python
* How to use set operations efficiently
* How to find unique elements between collections
* How to sort and display results in a required format
* Practical applications of symmetric difference in problem-solving
