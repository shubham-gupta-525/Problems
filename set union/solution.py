# Enter your code here. Read input from STDIN. Print output to STDOUT
english = input()
roll_e = set(map(int, input().split()))
french = input()
roll_f = set(map(int, input().split()))

answer = roll_e.union(roll_f)
print(len(answer))
