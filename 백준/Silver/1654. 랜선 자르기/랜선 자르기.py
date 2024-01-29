import sys
input = lambda: sys.stdin.readline().rstrip()

K, N = map(int, input().split())
arr = sorted([int(input()) for _ in range(K)])
start, end = 1, max(arr)

while start <= end:
    mid = (start + end) // 2
    num = 0
    for i in arr:
        num += i // mid
    if num >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)