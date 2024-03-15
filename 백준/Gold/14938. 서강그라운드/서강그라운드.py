import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

INF = int(1e9)
n, m, r = map(int, input().split())
t = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))
    
def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

items = [0] * (n+1)
for start in range(1, n+1):
    distance = dijkstra(start)
    for i in range(1, n+1):
        if distance[i] <= m:
            items[start] += t[i-1]
print(max(items))