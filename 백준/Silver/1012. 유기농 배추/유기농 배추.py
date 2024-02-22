import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global M, N
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        graph[b][a] = 1

    num = 0    
    for i in range(M):
        for j in range(N):
            if dfs(i, j) == True:
                num += 1
    print(num)