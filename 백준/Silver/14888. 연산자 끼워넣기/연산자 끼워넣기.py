N = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split())) # + - * /
visited = [0] * 4
arr = []
ans = []

def calculate(arr):
    ans = A[0]
    for i in range(1, N):
        if arr[i-1] == 0:
            ans += A[i]
        elif arr[i-1] == 1:
            ans -= A[i]
        elif arr[i-1] == 2:
            ans *= A[i]
        elif arr[i-1] == 3:
            if ans < 0:
                ans = -(-ans // A[i])
            else:
                ans //= A[i]
    return ans

def dfs():
    if len(arr) == N-1:
        ans.append(calculate(arr))
        return
    for i in range(4):
        if visited[i] < op[i]:
            arr.append(i)
            visited[i] += 1
            dfs()
            arr.pop()
            visited[i] -= 1
            
dfs()
ans.sort()
print(ans[-1])
print(ans[0])