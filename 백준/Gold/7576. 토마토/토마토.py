import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

M, N = map(int, input().split()) # 가로, 세로
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(xy):
    q = deque()
    for z in xy:
        x, y = z
        q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    m = 0
    for i in range(N):
        if m < max(graph[i]):
            m = max(graph[i])
        if 0 in graph[i]:
            return -1
    return m-1

nonzero = 0
st = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            st.append([i, j])
        elif graph[i][j] == 0:
            nonzero += 1

if nonzero == 0:
    print(0)
else:
    print(bfs(st))