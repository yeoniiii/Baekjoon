N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [0] * (N+1)
arr = []

def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(num[i-1])
            dfs()
            visited[i] = 0
            arr.pop()
            
dfs()