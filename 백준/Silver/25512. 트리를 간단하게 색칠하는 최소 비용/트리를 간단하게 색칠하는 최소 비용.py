import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
tree = [[] for i in range(n)]
cost = []
for i in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)
for i in range(n):
    cost.append(list(map(int, input().split())))
    
def bfs(color):
    total_cost = 0
    visited = [0] * n
    q = deque()
    
    visited[0] = 1
    q.append((0, color))
    total_cost += cost[0][color]
    
    while q:
        x, color = q.popleft()
        for v in tree[x]:
            if visited[v] == 0:
                visited[v] = 1
                total_cost += cost[v][1-color]
                q.append((v, 1-color))
                
    return total_cost

print(min(bfs(0), bfs(1)))     