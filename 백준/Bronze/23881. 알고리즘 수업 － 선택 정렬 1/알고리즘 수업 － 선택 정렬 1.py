N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for n in range(N, 1, -1):
    i = A.index(max(A[:n]))
    if i != n-1:
        A[i], A[n-1] = A[n-1], A[i]
        cnt += 1
        if cnt == K:
            print(A[i], A[n-1])
            break
if cnt < K:
    print(-1)