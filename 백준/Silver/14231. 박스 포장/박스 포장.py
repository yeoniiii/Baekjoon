n = int(input())
A = list(map(int, input().split()))
cnt = [1]
for i in range(1, n):
    j, max_cnt = 1, 1
    while 0 <= i-j:
        if A[i] > A[i-j]:
            if max_cnt <= cnt[i-j]:
                max_cnt = cnt[i-j] + 1
        j += 1
    cnt.append(max_cnt)
        
print(max(cnt))