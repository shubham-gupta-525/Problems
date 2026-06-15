from itertools import combinations_with_replacement 

s, k = input().split()
k = int(k)

pair = (list(combinations_with_replacement(sorted(s),k)))
for p in pair:
    print(''.join(p))