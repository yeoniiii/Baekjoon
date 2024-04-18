import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N = int(input())
arr = []
for i in range(N):
    arr_i = list(map(int, input().split()))
    for j in arr_i:
        heapq.heappush(arr, j)
    if i > 0:
        for k in range(N):
            heapq.heappop(arr)
print(heapq.heappop(arr))