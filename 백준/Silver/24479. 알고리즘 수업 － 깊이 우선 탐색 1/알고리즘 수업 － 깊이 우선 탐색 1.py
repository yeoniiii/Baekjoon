import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
cnt = 0
num = [0] * (N+1)

def dfs(graph, v, visited):
    global cnt
    visited[v] = 1
    cnt += 1
    num[v] = cnt
    for i in sorted(graph[v]):
        if visited[i] == 0:
            dfs(graph, i, visited)

dfs(graph, R, visited)
print('\n'.join(map(str, num[1:])))