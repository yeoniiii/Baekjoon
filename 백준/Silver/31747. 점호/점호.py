N, K = map(int, input().split())
A = list(map(int, input().split()))
t = 0

while A:
    a0 = A[0]
    diff = 0
    for a in A[:K]:
        if a != a0:
            diff = 1
    if diff == 1:
        del1, del2 = 0, 0
        for i in range(K):
            if del1 == del2 == 1:
                break
            if A[i] == 1 and del1 == 0:
                A.pop(i)
                del1 += 1
            elif A[i] == 2 and del2 == 0:
                A.pop(i)
                del2 += 1
        t += 1
    else:
        A.pop(0)
        t += 1

print(t)