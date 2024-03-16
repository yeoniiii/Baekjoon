import sys
input = lambda: sys.stdin.readline().rstrip()

from collections import deque
import copy

N, M = map(int, input().split())
graph = []
virus = []
wall = []

for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append([i, j])
        elif graph[i][j] == 0:
            wall.append([i, j])

def bfs(graph_w, virus):
    q = deque()
    for v in virus:
        x, y = v
        q.append((x, y))
        graph_w[x][y] = 2
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph_w[nx][ny] == 1:
                continue
            if graph_w[nx][ny] == 0:
                graph_w[nx][ny] = 2
                q.append((nx, ny))


def cntSafe(graph_w):
    bfs(graph_w, virus)

    safe = 0
    for i in range(N):
        for j in range(M):
            if graph_w[i][j] == 0:
                safe += 1
    return safe

safe_cnt = []

for i in range(len(wall)):
    for j in range(len(wall)):
        for k in range(len(wall)):
            if i < j < k:
                graph_w = copy.deepcopy(graph)
                x1, y1 = wall[i]
                x2, y2 = wall[j]
                x3, y3 = wall[k]
                graph_w[x1][y1] = 1
                graph_w[x2][y2] = 1
                graph_w[x3][y3] = 1
                safe_cnt.append(cntSafe(graph_w))

print(max(safe_cnt))
