N, M = map(int, input().split())
inp = list(map(int, input().split()))
num = {}
visited = {}
for i in inp:
    visited[i] = 0
    if i in num:
        num[i] += 1
    else:
        num[i] = 1
nums = sorted(list(num.keys()))
arr = []

def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in nums:
        if visited[i] < num[i]:
            if len(arr) == 0 or (len(arr) > 0 and arr[-1] <= i):
                visited[i] += 1
                arr.append(i)
                dfs()
                visited[i] -= 1
                arr.pop()
            
dfs()