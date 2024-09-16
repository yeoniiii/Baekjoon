N, K = map(int, input().split())
A = list(map(int, input().split(',')))
for k in range(K):
    B = []
    for l in range(1, len(A)):
        B.append(A[l]-A[l-1])
    A = B
if K == 0:
    B = A
print(','.join(map(str, B)))
    