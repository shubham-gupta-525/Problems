# Company Logo

## Problem Statement

A newly opened multinational brand wants to create its company logo using the three most common characters from its company name.

Given a string containing lowercase English letters, find the top three most frequent characters and print them along with their occurrence counts.

### Rules

1. Sort characters by frequency in descending order.
2. If two characters have the same frequency, sort them alphabetically.
3. Print only the top three characters.

---

## Example

### Input

```text
aabbbccde
```

### Output

```text
b 3
a 2
c 2
```

### Explanation

* `b` appears 3 times.
* `a` and `c` both appear 2 times.
* Since `a` comes before `c` alphabetically, `a` is printed first.

---

## Solution

```python
s = input()

frequency = {}

for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

frequency_sorted = sorted(
    frequency.items(),
    key=lambda x: (-x[1], x[0])
)

for k, v in frequency_sorted[:3]:
    print(k, v)
```

---

## Approach

1. Read the input string.
2. Count the frequency of each character using a dictionary.
3. Sort the dictionary items:

   * First by frequency in descending order.
   * Then alphabetically for equal frequencies.
4. Print the first three elements from the sorted list.

---

## Time Complexity

* Counting frequencies: **O(n)**
* Sorting characters: **O(k log k)**

Where:

* `n` = length of the string
* `k` = number of distinct characters

---

## Space Complexity

**O(k)**

where `k` is the number of distinct characters.


