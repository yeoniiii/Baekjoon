N = int(input())
M = int(input())
arr = []

for i in range(M):
    arr.append(list(map(int, input().split())))
    
visited = [0] * (N+1)

def dfsVirus(arr, v, visited):
    visited[v] = 1
    if sum(visited) >= N:
        return False
    for i in range(len(arr)):
        if v in arr[i]:
            v = arr[i][1 - arr[i].index(v)]
            if visited[v] == 0:
                dfsVirus(arr, v, visited)


dfsVirus(arr, 1, visited)
print(sum(visited) - 1)