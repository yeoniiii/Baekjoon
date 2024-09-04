import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    L, R, S = map(int, input().split())
    x = 1
    while True:
        if x % 2 == 0:
            S += x-1
        else:
            S -= x-1
        if S == L or S == R:
            break
        x += 1
    print(x)
        