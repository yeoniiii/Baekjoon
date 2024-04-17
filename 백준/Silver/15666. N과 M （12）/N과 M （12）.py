N, M = map(int, input().split())
num = sorted(list(set(list(map(int, input().split())))))
visited = {}
for i in num:
    visited[i] = 0
arr = []

def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in num:
        if visited[i] < M:
            if len(arr) == 0 or (len(arr)>0 and arr[-1] <= i):
                visited[i] += 1
                arr.append(i)
                dfs()
                visited[i] -= 1
                arr.pop()

dfs()