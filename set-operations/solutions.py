m = int(input())
set1 = set(map(int,input().split())) 

n = int(input())
set2 = set(map(int, input().split()))

diff1 = set1.difference(set2)
diff2 = set2.difference(set1)
combine = diff1.union(diff2)

for i in sorted(combine):
    print(i)