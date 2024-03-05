from collections import deque

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr_i = list(map(int, input().split()))
    arr.append(arr_i)
    if 2 in arr_i:
        st_x, st_y = i, arr_i.index(2)
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[0] * m for _ in range(n)]

def bfs(x, y):
    arr[x][y] = 0
    visited[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

    return arr

ans = bfs(st_x, st_y)

for i in range(len(ans)):
    for j in range(len(ans[i])):
        if visited[i][j] == 0 and arr[i][j] == 1:
            ans[i][j] = -1
            
for i in range(len(ans)):
    print(*ans[i])