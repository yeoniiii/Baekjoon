import sys
sys.setrecursionlimit(10**4)

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        if q == -1:
            return
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)
        
def partition(A, p, r):
    global cnt
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[j], A[i] = A[i], A[j]
            cnt += 1
            if cnt == K:
                print(A[i], A[j])
                return -1
    if i+1 != r:
        A[i+1], A[r] = A[r], A[i+1]
        cnt += 1
        if cnt == K:
            print(A[i+1], A[r])
            return -1
    return i+1

quick_sort(A, 0, N-1)
if cnt < K:
    print(-1)