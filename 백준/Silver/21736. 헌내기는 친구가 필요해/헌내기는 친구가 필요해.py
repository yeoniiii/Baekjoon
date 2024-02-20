import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(list(input()))

for i in range(N):
    if 'I' in graph[i]:
        j = graph[i].index('I')
        break

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


cnt = 0
q = deque()
q.append((i, j))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if graph[nx][ny] == 'X':
            continue
        if graph[nx][ny] in ['O', 'P']:
            if graph[nx][ny] == 'P':
                cnt += 1
            graph[nx][ny] = 'X'
            q.append((nx, ny))
if cnt > 0:
    print(cnt)
else:
    print('TT')