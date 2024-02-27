from collections import deque

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
   
visited = [0] * (N+1)
def bfs(graph, v, visited):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        cnt += 1
        bfs(graph, i, visited)

print(cnt)