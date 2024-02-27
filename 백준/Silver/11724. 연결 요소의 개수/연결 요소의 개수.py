import sys
sys.setrecursionlimit(10**3)

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
   
visited = [0] * (N+1)
def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i]==0:
            dfs(graph, i, visited)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        cnt += 1
        dfs(graph, i, visited)

print(cnt)