import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    print(2-V+E)