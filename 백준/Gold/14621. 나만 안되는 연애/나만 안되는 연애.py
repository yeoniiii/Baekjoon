import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
gender = list(input().split())
parent = [i for i in range(N+1)]
edges = []
result = 0


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
        
for i in range(M):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()

for edge in edges:
    d, u, v = edge
    if gender[u-1] != gender[v-1]:
        if find_parent(parent, u) != find_parent(parent, v):
            union_parent(parent, u, v)
            result += d

ans = 0
for edge in edges:
    d, u, v = edge
    if find_parent(parent, u) != find_parent(parent, v):
        ans += 1
        
if ans == 0:            
    print(result)
else:
    print(-1)