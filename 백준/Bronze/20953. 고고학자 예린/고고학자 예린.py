import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    a, b = map(int, input().split())
    print(int(((a+b-1) * (a+b) / 2) * (a+b)))