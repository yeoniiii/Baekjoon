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
        
def dist(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2) ** (1/2)

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
god = []
edges = []
result = 0
last = 0

for i in range(N):
    X, Y = map(int, input().split())
    god.append((X, Y))
    
for j in range(M):
    a, b = map(int, input().split())
    union_parent(parent, a-1, b-1)
    
for comb in combinations(range(N), 2):
    a, b = comb
    x1, y1 = god[a]
    x2, y2 = god[b]
    c = dist(x1, y1, x2, y2)
    edges.append((c, a, b))
    
edges.sort()
    
for edge in edges:
    c, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
     
print(format(result, ".2f"))