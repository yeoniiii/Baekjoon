N = int(input())
arr = list(map(int, input().split()))
d = [0] * N
d[0] = arr[0]

if N >= 2:
    for i in range(1, N):
        d[i] = max(arr[i] + d[i-1], arr[i])

print(max(d))