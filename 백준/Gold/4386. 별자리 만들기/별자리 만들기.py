import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [i for i in range(n+1)]
edges = []
result = 0

def dist(x1, y1, x2, y2):
    d = ((x2-x1)**2 + (y2-y1)**2) ** (1/2)
    return round(d, 2)

star = []
for i in range(n):
    x, y = map(float, input().split())
    star.append((x, y))
    
for comb in combinations(range(n), 2):
    i, j = comb
    x1, y1 = star[i]
    x2, y2 = star[j]
    cost = dist(x1, y1, x2, y2)
    edges.append((cost, i, j))
    
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        
print(result)