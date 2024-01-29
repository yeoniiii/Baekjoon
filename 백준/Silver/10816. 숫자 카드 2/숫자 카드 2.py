import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
sang = sorted(list(map(int, input().split())))
M = int(input())
card = list(map(int, input().split()))

sang_dict = {}
for s in sang:
    if s in sang_dict:
        sang_dict[s] += 1
    else:
        sang_dict[s] = 1

def num_card(arr, n, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == n:
        return sang_dict[n]
    elif arr[mid] < n:
        return num_card(arr, n, mid+1, end)
    else: # arr_set[mid] > n
        return num_card(arr, n, start, mid-1)

ans = []
for c in card:
    ans.append(num_card(sang, c, 0, len(sang)-1))

print(*ans)