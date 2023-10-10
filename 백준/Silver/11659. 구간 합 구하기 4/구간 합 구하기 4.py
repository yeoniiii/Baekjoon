import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0]

for i in range(N):
    sum.append(arr[i] + sum[i])

for m in range(M):
    a, b = map(int, input().split())
    print(sum[b] - sum[a-1])