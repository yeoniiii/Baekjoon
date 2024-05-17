N = int(input())
k = int(input())

start, end = 1, k

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    
    for i in range(1, N+1):
        cnt += min(mid//i, N)
        
    if cnt >= k:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1
        
print(ans)