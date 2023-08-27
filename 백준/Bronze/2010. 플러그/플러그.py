import sys
input = sys.stdin.readline

N = int(input())
s = 1

for _ in range(N):
    s += int(input()) - 1
print(s)