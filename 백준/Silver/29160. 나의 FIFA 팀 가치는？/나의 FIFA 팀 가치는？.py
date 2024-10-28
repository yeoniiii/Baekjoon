import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq
members = [[0] for _ in range(12)]

N, K = map(int, input().split())
for n in range(N):
    P, W = map(int, input().split())
    heapq.heappush(members[P], -W)
    
for k in range(K):
    for i in range(1, 12):
        v = - heapq.heappop(members[i]) -1
        v = max(0, v)
        heapq.heappush(members[i], -v)
        
res = sum(-members[i][0] for i in range(1, 12))
print(res)