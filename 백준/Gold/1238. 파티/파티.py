import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

distance = dijkstra(X)
m = 0
for i in range(1, N+1):
    d = dijkstra(i)
    distance[i] += d[X]
    if m < distance[i]:
        m = distance[i]
print(m)