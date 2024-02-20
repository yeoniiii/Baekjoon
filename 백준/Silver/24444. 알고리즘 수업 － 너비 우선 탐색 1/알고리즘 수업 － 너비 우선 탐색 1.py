import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M, R = map(int, input().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N+1)
cnt = 0
num = [0] * (N+1)

def bfs(graph, start, visited):
    global cnt
    q = deque([start])
    cnt += 1
    num[start] = cnt
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in sorted(graph[v]):
            if visited[i] == 0:
                q.append(i)
                cnt += 1
                num[i] = cnt
                visited[i] = 1
        
bfs(graph, R, visited)
print('\n'.join(map(str, num[1:])))