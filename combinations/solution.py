from itertools import combinations

word, join = input().split()
join = int(join)
word = word.upper()

print(list(combinations(word, join)))