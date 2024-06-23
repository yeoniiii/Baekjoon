import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
arr = [[] for i in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
for x in arr[1]:
    visited[x] = 1
    for v in arr[x]:
        visited[v] = 1

if sum(visited) == 0:
    print(0)
else:
    print(sum(visited) - 1)