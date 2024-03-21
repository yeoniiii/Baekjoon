N = int(input())
parents = list(map(int, input().split()))
rm = int(input())

tree = [[] for i in range(N)]
for i in range(N):
    if parents[i] != -1:
        tree[parents[i]].append(i)
    else:
        root = i
visited = [0] * N
visited[rm] = -1

def dfs(x, visited):
    if visited[x] != -1:
        visited[x] = 1
        for i in tree[x]:
            if visited[i] == 0:
                dfs(i, visited)
    
dfs(root, visited)
leaf = 0

for i in range(N):
    if rm in tree[i]:
        tree[i].remove(rm)
    if len(tree[i]) == 0 and visited[i] == 1:
        leaf += 1

print(leaf)