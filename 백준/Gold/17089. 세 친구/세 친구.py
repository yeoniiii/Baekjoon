import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for m in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

min_num = 10e9
for a in range(1, N+1):
    if not graph[a]:
        continue
    for b in graph[a]:
        for c in graph[a]:
            if b == c:
                continue
            if c in graph[b]:
                min_num = min(min_num, len(graph[a])+len(graph[b])+len(graph[c])-6)

if min_num == 10e9:
    print(-1)
else:
    print(min_num)    