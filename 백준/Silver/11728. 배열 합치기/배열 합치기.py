N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))

a, b = 0, 0
ans = []
while 0 <= a < N and 0 <= b < M:
    if A[a] <= B[b]:
        ans.append(A[a])
        a += 1
    else:
        ans.append(B[b])
        b += 1
    if a == N:
        for i in B[b:]:
            ans.append(i)
    if b == M:
        for i in A[a:]:
            ans.append(i)
print(*ans)