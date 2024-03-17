import sys
input = lambda: sys.stdin.readline().rstrip()

R, C = map(int, input().split())
graph = []
alphabet = [0] * 26
for i in range(R):
    graph.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
max_cnt = 0

def dfs(x, y, cnt):
    global max_cnt
    id = int(ord(graph[x][y])-ord('A'))
    alphabet[id] = 1
    max_cnt = max(cnt, max_cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<R and 0<=ny<C:
            id = int(ord(graph[nx][ny])-ord('A'))
            if alphabet[id] == 0:
                dfs(nx, ny, cnt+1)
                alphabet[id] = 0

dfs(0, 0, 1)
print(max_cnt)