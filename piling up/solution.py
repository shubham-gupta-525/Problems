from collections import deque

t = int(input())

for _ in range(t):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            print("No")
            break

        last = current
    else:
        print("Yes")