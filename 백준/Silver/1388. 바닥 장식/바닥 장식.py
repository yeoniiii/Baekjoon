import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


N, M = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(input()))
    
def dfs(x, y, val):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    if arr[x][y] != val:
        return False
    if val == '-':
        arr[x][y] = '+'
        dfs(x, y-1, val)
        dfs(x, y+1, val)
        return True
    elif val == '|':
        arr[x][y] = '+'
        dfs(x-1, y, val)
        dfs(x+1, y, val)
        return True   
    return False

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '+':
            continue
        if dfs(i, j, arr[i][j]):
            result += 1

print(result)