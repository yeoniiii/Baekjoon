N, K = map(int, input().split())
A = list(map(int, input().split()))

from copy import deepcopy
start, end = 0, len(A)
sorted_A = deepcopy(A)
num = []

def merge_sort(A, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(A, start, mid)
        merge_sort(A, mid+1, end)
        merge(A, start, mid, end)
        
def merge(A, start, mid, end):
    global sorted_A
    i, j, t = start, mid+1, 0
    while i <= mid and j <= end:
        if A[i] <= A[j]:
            sorted_A[t] = A[i]
            i += 1
        else:
            sorted_A[t] = A[j]
            j += 1
        t += 1   
    
    while i <= mid:
        sorted_A[t] = A[i]
        i += 1
        t += 1

    while j <= end:
        sorted_A[t] = A[j]
        j += 1
        t += 1

    i, t = start, 0
    while i <= end:
        A[i] = sorted_A[t]
        num.append(sorted_A[t])
        i += 1
        t += 1

merge_sort(A, 0, len(A)-1)
if len(num) < K:
    print(-1)
else:
    print(num[K-1])