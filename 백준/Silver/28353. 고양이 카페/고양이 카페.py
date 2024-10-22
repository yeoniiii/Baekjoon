N, K = map(int, input().split())
arr = sorted(list(map(int, input().split())))
l, r = 0, N-1

ans = 0
while l < r:
    if arr[l] + arr[r] <= K:
        l += 1
        r -= 1
        ans += 1
    else:
        r -= 1
    
print(ans)