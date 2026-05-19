# Exceptions - HackerRank

## Problem Statement
You are given two values **a** and **b**. Perform integer division (`a // b`) and print the result.

If an exception occurs:

- **ZeroDivisionError** → when dividing by zero
- **ValueError** → when input is not a valid integer

Print the error code in such cases.

---

## Sample Input

3
1 0
2 $
3 1

---

## Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3

---

## Concepts Used

- `try` and `except`
- `ZeroDivisionError`
- `ValueError`
- Integer Division (`//`)

---

## Solution Approach

1. Read number of test cases.
2. Take input values `a` and `b`.
3. Perform integer division.
4. Handle exceptions using `try-except`.

---

## Python Solution

```python
test = int(input())

for _ in range(test):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)