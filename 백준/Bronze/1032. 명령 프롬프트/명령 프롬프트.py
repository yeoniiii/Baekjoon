N = int(input())
prev = input()
ans = list(prev)

for _ in range(N-1):
    curr = input()
    for i in range(len(curr)):
        if prev[i] != curr[i]:
            ans[i] = '?'
        else: continue
    prev = curr
print(*ans, sep='')