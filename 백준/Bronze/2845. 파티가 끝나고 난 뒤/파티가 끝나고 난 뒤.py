L, P = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for i in arr:
    ans.append(i - L*P)
print(*ans)