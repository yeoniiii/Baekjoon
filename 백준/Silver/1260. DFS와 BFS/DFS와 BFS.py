import sys
sys.setrecursionlimit(10**6)
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)
num_dfs = []
num_bfs = []

def dfs(graph, v, visited, num):
    visited[v] = 1
    num.append(v)
    for i in sorted(graph[v]):
        if visited[i] == 0:
            dfs(graph, i, visited, num)

def bfs(graph, start, visited, num):
    q = deque([start])
    visited[start] = 1
    num.append(start)
    while q:
        v = q.popleft()
        for i in sorted(graph[v]):
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                num.append(i)
                
dfs(graph, V, visited_dfs, num_dfs)
bfs(graph, V, visited_bfs, num_bfs)

print(' '.join(map(str, num_dfs)))
print(' '.join(map(str, num_bfs)))