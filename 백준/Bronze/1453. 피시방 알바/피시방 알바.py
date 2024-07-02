N = int(input())
arr = list(map(int, input().split()))
pc = {}
ans = 0
for a in arr:
    if a in pc:
        ans += 1
    else:
        pc[a] = 1
print(ans)