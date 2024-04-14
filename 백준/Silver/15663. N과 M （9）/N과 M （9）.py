N, M = map(int, input().split())
inp = list(map(int, input().split()))
num = {}
visited = {}
for n in inp:
    visited[n] = 0
    if n in num:
        num[n] += 1
    else:
        num[n] = 1
nums = sorted(list(num.keys()))
arr = []

def dfs():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in nums:
        if visited[i] < num[i]:
            visited[i] += 1
            arr.append(i)
            dfs()
            visited[i] -= 1
            arr.pop()
            
dfs()