N, M = map(int, input().split())
visited = [0] * (N+1)
arr = []

def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        if visited[i] < M:
            visited[i] += 1
            arr.append(i)
            dfs()
            visited[i] -= 1
            arr.pop()
            
dfs()