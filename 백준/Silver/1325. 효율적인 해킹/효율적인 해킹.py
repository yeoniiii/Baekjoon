import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque

N, M = map(int, input().split())

arr = [[] for i in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

def bfs(x):
    q = deque([x])
    visited[x] = 1
    while q:
        x = q.popleft()
        for v in arr[x]:
            if visited[v] == 0:
                visited[v] = 1
                q.append(v)

cnt = []
for i in range(1, N+1):
    visited = [0] * (N+1)
    bfs(i)
    cnt.append(sum(visited))

max_cnt = max(cnt)
for i, c in enumerate(cnt):
    if c == max_cnt:
        print(i+1, end=' ')