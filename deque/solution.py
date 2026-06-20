from collections import deque
d = deque()
num = int(input())
for i in range (num):
    operation = input().split()
    if operation[0] == "append":
        d.append(operation[1])
    elif operation[0] == "appendleft":
        d.appendleft(operation[1])
    elif operation[0] == "pop":
        d.pop()
    elif operation[0] == "popleft":
        d.popleft()
        
print(' '.join(d))