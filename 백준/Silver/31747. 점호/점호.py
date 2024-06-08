N, K = map(int, input().split())
A = list(map(int, input().split()))
t = 0

if N == K:
    num = {1:0, 2:0}
    for a in A:
        num[a] += 1
    print(max(num[1], num[2]))
else:
    while A:
        a0 = A[0]
        diff = 0
        for i in range(min(K, len(A))):
            if A[i] != a0:
                diff = 1
                del_i = i
                break
        if diff == 1:
            A.pop(del_i)
            A.pop(0)
            t += 1
        else:
            A.pop(0)
            t += 1

    print(t)