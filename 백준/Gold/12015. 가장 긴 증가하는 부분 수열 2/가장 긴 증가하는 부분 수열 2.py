N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

def binary_search(n):
    start, end = 0, len(LIS)-1
    while start <= end:
        mid = (start + end) // 2
        if LIS[mid] == n:
            return mid
        elif LIS[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(1, N):
    n = A[i]
    if LIS[-1] < n:
        LIS.append(n)
    else:
        idx = binary_search(n)
        LIS[idx] = n
        
print(len(LIS))