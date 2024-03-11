import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq
INF = int(1e9)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
distance = [INF] * (N+1)

def dijkstra(start):
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

dijkstra(X)
ans = []
for i in range(1, N+1):
    if distance[i] == INF:
        continue
    elif distance[i] == K:
        ans.append(i)
if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)