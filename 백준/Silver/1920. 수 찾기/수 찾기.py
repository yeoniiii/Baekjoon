N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

def find(A, N, b):
    l, r = 0, N-1
    while l + 1 < r:
        mid = (l+r)//2
        if A[mid] > b:
            r = mid
        elif A[mid] < b:
            l = mid
        elif A[mid] == b:
            return 1
    if l + 1 == r:
        if (A[l] == b) | (A[r] == b): return 1
        else: return 0

for m in range(M):
    print(find(A, N, B[m]))