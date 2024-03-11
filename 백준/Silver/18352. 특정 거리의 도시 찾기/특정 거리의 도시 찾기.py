import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
num = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                num[i] = num[v] + 1
          
bfs(X)
ans = []

for i in range(1, N+1):
    if num[i] == K:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)