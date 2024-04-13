N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []
visited = [0] * (N+1)

def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        if visited[i] < M:
            if len(arr) == 0 or (len(arr) > 0 and arr[-1] <= num[i-1]):
                visited[i] += 1
                arr.append(num[i-1])
                dfs()
                visited[i] -= 1
                arr.pop()
                
dfs()