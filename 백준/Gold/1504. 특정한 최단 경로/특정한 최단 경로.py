import sys
input = lambda: sys.stdin.readline().rstrip()

import heapq
INF = int(1e9)

N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start):
    q = []
    distance = [INF] * (N+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

d1 = []
d2 = []
distance = dijkstra(1)
d1.append(distance[v1])
d2.append(distance[v2])
distance = dijkstra(v1)
d1.append(distance[v2])
d2.append(distance[-1])
distance = dijkstra(v2)
d1.append(distance[-1])
d2.append(distance[v1])

s1, s2 = 0, 0
for i in d1:
    if i == INF:
        s1 = -1
        break
    else:
        s1 += i
for i in d2:
    if i == INF:
        s2 = -1
        break
    else:
        s2 += i
print(min(s1, s2))