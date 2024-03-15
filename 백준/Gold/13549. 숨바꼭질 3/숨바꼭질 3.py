import heapq

N, K = map(int, input().split())
visited = [0] * 100001

def bfs(x):
    min_sec = int(1e9)
    q = []
    heapq.heappush(q, (0, x))
    visited[x] = 1

    while q:
        sec, v = heapq.heappop(q)
        if v == K and min_sec >= sec:
            min_sec = sec
        else:
            for i in [v-1, v+1, v*2]:
                if 0<=i<=100000 and visited[i] == 0:
                    if i == v*2:
                        heapq.heappush(q, (sec, i))
                    else:
                        heapq.heappush(q, (sec+1, i))
                    visited[i] = 1
    return min_sec

print(bfs(N))