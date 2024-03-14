from collections import deque

N, K = map(int, input().split())
visited = [0] * 100001

def bfs(x):
    min_sec = int(1e9)
    cnt = 0
    q = deque()
    q.append((x, 0))
    
    while q:
        v, sec = q.popleft()
        if v == K and min_sec >= sec:
            min_sec = sec
            cnt += 1
        else:
            for i in [v-1, v+1, 2*v]:
                if i < 0 or i > 100000:
                    continue
                if visited[i] == 0 or visited[i] == visited[v] + 1:
                    visited[i] = visited[v] + 1
                    q.append((i, visited[i]))
    return min_sec, cnt

sec, cnt = bfs(N)
print(sec)
print(cnt)