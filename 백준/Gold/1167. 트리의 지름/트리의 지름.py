import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]

for i in range(n):
    arr = list(map(int, input().split()))
    arr.remove(-1)
    j = 1
    while j+1 <= len(arr)-1:
        tree[arr[0]].append((arr[j], arr[j+1]))
        j += 2
    
leaf = []
for i in range(1, n+1):
    if len(tree[i]) == 1:
        leaf.append(i)
        
def dfs(x, visited, dist):
    visited[x] = 1
    dists[x] = dist
    for v, dist in tree[x]:
        if visited[v] == 0:
            dfs(v, visited, dists[x] + dist)

visited = [0] * (n+1)
dists = [0] * (n+1)
dfs(1, visited, 0)

max_dist, max_leaf = 0, 0
for l in leaf:
    if max_dist < dists[l]:
        max_dist = dists[l]
        max_leaf = l

visited = [0] * (n+1)
dists = [0] * (n+1)
dfs(max_leaf, visited, 0)

print(max(dists))