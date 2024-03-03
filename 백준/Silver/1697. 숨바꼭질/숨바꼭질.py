from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

def bfs(x):
    q = deque()
    q.append((x, 0))
    visited[x] = 1

    while q:
        v, sec = q.popleft()
        if v == K:
            return sec
        else:
            for i in [v-1, v+1, v*2]:
                if 0<=i<=100000 and visited[i] == 0:
                    q.append((i, sec+1))
                    visited[i] = 1

print(bfs(N))