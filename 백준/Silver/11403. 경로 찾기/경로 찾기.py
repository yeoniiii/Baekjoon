import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

N = int(input())
graph = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    arr = list(map(int, input().split()))
    for j in range(1, N+1):
        if arr[j-1] == 1:
            graph[i][j] = 1
        #if i == j:
        #    graph[i][j] = 1
     
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()