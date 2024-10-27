import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

R, C = map(int, input().split())
arr = []
check = []
for r in range(R):
    arr.append(list(input()))
    for j in range(C):
        if arr[r][j] == '.':
            check.append([r, j])
    
def bfs(v):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque([v])
    while q:
        x, y = q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if -1 < nx < R and -1 < ny < C:
                if arr[nx][ny] == '.':
                    cnt += 1
                
                    if visited[nx][ny] == False:
                        visited[nx][ny] = True
                        q.append([nx, ny])
        if cnt < 2:
            return 1
    return 0

visited = [[False] * C for _ in range(R)]
print(bfs(check[0]))