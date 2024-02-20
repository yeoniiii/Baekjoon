import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for i in range(N+1)]
parents = [0] * (N+1)
visited = [0] * (N+1)

for i in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    
def dfsTree(tree, v, visited):
    visited[v] = 1
    for i in tree[v]:
        if visited[i] == 0:
            parents[i] = v
            dfsTree(tree, i, visited)

dfsTree(tree, 1, visited)
print('\n'.join(map(str, parents[2:])))