import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

S = [input() for n in range(N)]
S.sort()
test = [input() for n in range(M)]

def binary_search(arr, n, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return 1
        elif arr[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return 0

ans = 0
for t in test:
    ans += binary_search(S, t, 0, N-1)
print(ans)