import sys
input = lambda: sys.stdin.readline().rstrip()

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
        
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    
    parent = [i for i in range(N+1)]
    edges = []
    result = 0
    
    for m in range(M):
        a, b = map(int, input().split())
        edges.append((1, a, b))
        
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
            
    print(result)