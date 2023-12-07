import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())
X = m
ex = br = 0

if X + T > M:
    print(-1)
else:
    while True:
        X += T
        ex += 1
        if ex == N:
            break
        if X + T > M:
            while X + T > M:
                if X - R < m:
                    X = m
                else:
                    X -= R
                br += 1
    print(ex+br)