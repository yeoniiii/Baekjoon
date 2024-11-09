import sys
input = lambda: sys.stdin.readline().rstrip()

Q = int(input())
for q in range(Q):
    a, b = map(int, input().split())
    if b % a == 0 and b // a >= 2:
        print(1)
    else:
        print(0)