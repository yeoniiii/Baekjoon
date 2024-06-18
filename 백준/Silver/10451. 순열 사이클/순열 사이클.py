import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(x):
    visited[x] = 1
    v = arr[x] - 1
    if visited[v] == 0:
        dfs(v)
    return

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0] * (N)
    cnt = 0

    for i in range(N):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    print(cnt)