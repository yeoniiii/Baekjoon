import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

M, N, H = map(int, input().split()) # 가로, 세로, 높이
graph = []
for h in range(H):
    graph.append([])
    for n in range(N):
        graph[h].append(list(map(int, input().split())))

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, -1, 0, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(xyz):
    q = deque()
    for k in xyz:
        x, y, z = k
        q.append((x, y, z))
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or nz < 0 or nz >= H:
                continue
            if graph[nz][nx][ny] == -1:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nx, ny, nz))
    m = 0
    for h in range(H):
        for i in range(N):
            if m < max(graph[h][i]):
                m = max(graph[h][i])
            if 0 in graph[h][i]:
                return -1
    return m-1

nonzero = 0
st = []
for i in range(N):
    for j in range(M):
        for k in range(H):
            if graph[k][i][j] == 1:
                st.append([i, j, k])
            elif graph[k][i][j] == 0:
                nonzero += 1

if nonzero == 0:
    print(0)
else:
    print(bfs(st))