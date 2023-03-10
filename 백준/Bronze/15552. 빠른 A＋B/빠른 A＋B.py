import sys

N = int(input())
a = [sys.stdin.readline().strip('\n') for _ in range(N)]

for i in range(N) :
    print(sum(map(int, a[i].split())))