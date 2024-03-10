import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    c = 0
    q = deque()
    q.append((x, y, c))
    visited[x][y][c] = 1
    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny][0] > 0 and visited[nx][ny][1] > 0:
                continue
            if visited[nx][ny][c] == 0:
                if graph[nx][ny] == 0:
                    q.append((nx, ny, c))
                    visited[nx][ny][c] = visited[x][y][c] + 1
                if graph[nx][ny] == 1 and c == 1:
                    continue
                if graph[nx][ny] == 1 and c == 0:
                    nc = c + 1
                    q.append((nx, ny, nc))
                    visited[nx][ny][nc] = visited[x][y][c] + 1
        
    return visited[N-1][M-1]


ans = bfs(0,0)
if ans == [0, 0]:
    print(-1)
elif 0 in ans:
        print(max(ans))
else:
    print(min(ans))