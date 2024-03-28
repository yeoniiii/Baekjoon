import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # A에서 B로
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = []
    
    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
       
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)
                
    for i in result:
        print(i, end=' ')
        
topology_sort()