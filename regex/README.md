# Validating Regex Patterns

## Problem Statement

You are given a string representing a regular expression pattern.

Your task is to determine whether the given pattern is a valid regular expression or not.

For each test case:

* Print `True` if the regex pattern is valid.
* Print `False` if the regex pattern is invalid.

## Example

### Input

```text
2
.*\+
.*+
```

### Output

```text
True
False
```

### Explanation

* `.*\+` is a valid regular expression.
* `.*+` is invalid because it contains multiple repeat operators, resulting in a regex compilation error.

## Approach

1. Read the number of test cases.
2. For each regex pattern:

   * Attempt to compile the pattern using Python's `re.compile()`.
   * If compilation succeeds, print `True`.
   * If a `re.error` exception occurs, print `False`.

## Python Concepts Used

* `re` module
* Exception Handling (`try-except`)
* Regular Expressions

## Complexity Analysis

* **Time Complexity:** O(n), where n is the length of the regex pattern.
* **Space Complexity:** O(1)

## Solution

```python
import re

for _ in range(int(input())):
    pattern = input()

    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)
```

## Key Learning

The `re.compile()` function can be used to validate whether a regular expression pattern is syntactically correct. Invalid patterns raise a `re.error` exception, which can be handled using a `try-except` block.
