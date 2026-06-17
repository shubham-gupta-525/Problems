# Word Order Counter

## Problem Statement

You are given **N** words. Some words may repeat. For each word, determine how many times it appears in the input.

The output should:

1. Print the number of **distinct words**.
2. Print the occurrence count of each distinct word in the order of their **first appearance**.

---

## Input Format

* The first line contains an integer **N**, representing the number of words.
* The next **N** lines each contain a word.

### Example Input

```text
4
bcdef
abcdefg
bcde
bcdef
```

---

## Output Format

* First line: Number of distinct words.
* Second line: Occurrence count of each distinct word in the order they first appeared.

### Example Output

```text
3
2 1 1
```

---

## Explanation

Input words:

```text
bcdef
abcdefg
bcde
bcdef
```

Distinct words in order of first appearance:

1. `bcdef` → appears 2 times
2. `abcdefg` → appears 1 time
3. `bcde` → appears 1 time

Therefore:

```text
3
2 1 1
```

---

## Approach

1. Create a dictionary to store the frequency of each word.
2. Maintain a list to preserve the order of first appearances.
3. For each word:

   * If it is encountered for the first time, add it to the list.
   * Update its count in the dictionary.
4. Print:

   * Number of distinct words (`len(order)`).
   * Frequencies of words according to their order in the list.

---

## Python Solution

```python
n = int(input())

word_count = {}
order = []

for _ in range(n):
    word = input().strip()

    if word not in word_count:
        word_count[word] = 0
        order.append(word)

    word_count[word] += 1

print(len(order))
print(*[word_count[word] for word in order])
```

---

## Time Complexity

* **O(N)**

## Space Complexity

* **O(N)**

where **N** is the number of input words.
