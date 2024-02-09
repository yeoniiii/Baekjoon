import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
sang = sorted(list(map(int, input().split())))
M = int(input())
card = list(map(int, input().split()))

def iscard(arr, n, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return 1
        elif arr[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return 0

ans = []
for c in card:
    ans.append(iscard(sang, c, 0, len(sang)-1))
print(' '.join(map(str, ans)))