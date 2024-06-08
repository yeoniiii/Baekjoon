N, K = map(int, input().split())
A = list(map(int, input().split()))

num = {1:0, 2:0}
for a in A[:K]:
    num[a] += 1
if N == K:
    print(max(num[1], num[2]))
else:
    start = 0
    t = 0
    while start <= N:
        if min(num[1], num[2]) == 0:
            if num[1] == 0:
                num[2] -= 1
            else:
                num[1] -= 1
            if start+K < N:
                num[A[start+K]] += 1
            start += 1
        else:
            num[1] -= 1
            num[2] -= 1
            if start+K < N:
                num[A[start+K]] += 1
            if start+K+1 < N:
                num[A[start+K+1]] += 1
            start += 2
        t += 1
    print(t-1)