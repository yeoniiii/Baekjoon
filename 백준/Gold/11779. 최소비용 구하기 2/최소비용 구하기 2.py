import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
path = [0] * (N+1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start, end):
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
                path[i[0]] = now
    return distance[end]

print(dijkstra(start, end))
ans = [end]
n = path[end]
while start != end and n != 0:
    ans.append(n)
    n = path[n]
print(len(ans))
print(*ans[::-1])