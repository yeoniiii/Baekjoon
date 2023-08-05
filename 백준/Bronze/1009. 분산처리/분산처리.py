import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())

com = {0:[10], 1:[1], 2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 5:[5],
      6:[6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1]}

for _ in range(T):
    a, b = map(int, input().split())
    a = a%10
    c = b % len(com[a])
    print(com[a][c-1] if c != 0 else com[a][-1])