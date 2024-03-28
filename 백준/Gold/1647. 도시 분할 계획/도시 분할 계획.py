import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

parent = [i for i in range(N+1)] # 부모 테이블 상에서 부모를 자기 자신으로 초기화
edges = [] # 모든 간선을 담을 리스트
result = 0 # 최종 비용

for i in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
    
edges.sort() # 간선을 비용순으로 정렬
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

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

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost
        
print(result - last)