import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

N = int(input())
graph = [[] for i in range(N+1)]
indegree = [0] * (N+1)
time = [0] * (N+1)

for i in range(1, N+1):
    arr = list(map(int, input().split()))
    t = arr.pop(0)
    time[i] = t
    n = arr.pop(0)
    
    for j in arr:
        graph[j].append(i)
        indegree[i] += 1
       
q = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(q, (time[i], i))
        
ans = 0
order = []

while q:
    t, v = heapq.heappop(q)
    ans = t
    order.append(v)
    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, (t + time[i], i))

print(ans)