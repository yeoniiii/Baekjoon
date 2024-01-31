import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
n = 0

for i in range(N):
    if coin[N-i-1] <= K:
        n += K // coin[N-i-1]
        K = K % coin[N-i-1]
    if K < 0:
        break

print(n)