N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
same = 0
if A == B:
    same = 1
else:
    for n in range(N, 0, -1):
        i = A.index(max(A[:n]))
        if i != n-1:
            A[i], A[n-1] = A[n-1], A[i]
            if A == B:
                same = 1
                break
print(same)