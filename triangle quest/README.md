# Triangle Quest 2 (HackerRank)

## Problem Statement

Given a positive integer `N`, print a palindromic triangle of size `N`.

### Example

For `N = 5`:

```
1
121
12321
1234321
123454321
```

## Constraints

- Use only one `for` loop.
- Complete the solution using exactly one `print` statement.
- Do not use string operations.

## Solution

```python
for i in range(1, int(input()) + 1):
    print((10**i // 9) ** 2)
```

## Explanation

The expression:

```python
10**i // 9
```

generates a number consisting of `i` consecutive ones.

Examples:

| i | 10**i // 9 |
|---|------------|
| 1 | 1 |
| 2 | 11 |
| 3 | 111 |
| 4 | 1111 |
| 5 | 11111 |

Squaring these numbers produces the required palindromes:

| Number | Square | Output |
|--------|--------|--------|
| 1 | 1 | 1 |
| 11 | 121 | 121 |
| 111 | 12321 | 12321 |
| 1111 | 1234321 | 1234321 |
| 11111 | 123454321 | 123454321 |

## Sample Input

```
5
```

## Sample Output

```
1
121
12321
1234321
123454321
```

## Time Complexity

- **O(N)**

## Space Complexity

- **O(1)**

## Key Concept

The mathematical identity:

```
(10^i // 9)^2
```

creates the palindromic pattern without using strings, satisfying all HackerRank constraints.