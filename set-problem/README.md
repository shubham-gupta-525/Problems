# Set .add()

## Problem Statement

Rupal has a large collection of country stamps. She wants to find the total number of **distinct countries** represented in her collection.

Given the names of countries on the stamps, determine how many unique country names exist.

## Input Format

* The first line contains an integer `N`, the number of stamps.
* The next `N` lines contain the names of countries.

## Output Format

Print the total number of distinct country stamps.

## Sample Input

```text
7
UK
China
USA
France
New Zealand
UK
France
```

## Sample Output

```text
5
```

## Explanation

The countries `UK` and `France` appear more than once.

Distinct countries are:

* UK
* China
* USA
* France
* New Zealand

Therefore, the total number of unique country stamps is **5**.

## Approach

1. Create an empty set.
2. Read each country name and add it to the set using the `.add()` method.
3. Since sets automatically remove duplicates, only unique country names remain.
4. Print the size of the set using `len()`.

## Solution

```python
n = int(input())
countries = set()

for _ in range(n):
    countries.add(input())

print(len(countries))
```

## Complexity Analysis

* **Time Complexity:** O(N)
* **Space Complexity:** O(N)

## Key Concepts

* Python Sets
* `.add()` Method
* Unique Elements
* `len()` Function

## Learning Outcome

This problem demonstrates how Python sets automatically store only unique values, making them useful for counting distinct items efficiently.
