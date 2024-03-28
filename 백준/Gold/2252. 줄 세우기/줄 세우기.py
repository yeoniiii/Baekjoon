import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
indegree = [0] * (N+1)
q = []

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) # A에서 B로
    indegree[B] += 1

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)
        
result = []
while q:
    v = heapq.heappop(q)
    result.append(v)
    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)
       
print(*result)