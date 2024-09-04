import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    L, R, S = map(int, input().split())
    if abs(L-S) < abs(R-S):
        dist = abs(L-S)
        print(dist*2+1)
    else:
        dist = abs(R-S)
        print(dist*2)