N = int(input())
arr = sorted(list(map(int, input().split())))

l, r = 0, 1
start, end = arr[l], arr[-r]
ans_mid = 2*10**9

while start < end:
    mid = start + end
    if mid == 0:
        ans_mid = mid
        ans = [start, end]
        break
    else:
        if abs(mid) < ans_mid:
            ans_mid = abs(mid)
            ans = [start, end]
        if mid > 0:
            r += 1
            end = arr[-r]
        elif mid < 0:
            l += 1
            start = arr[l]
        
print(*ans)