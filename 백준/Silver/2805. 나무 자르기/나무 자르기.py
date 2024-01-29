import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def max_len(arr, n):
    start, end = 1, max(arr)
    
    while start <= end:
        mid = (start + end) // 2
        l = 0
   
        for a in arr:
            if a > mid:
                l += (a-mid)
        if l >= M:    
            start = mid + 1
        else:
            end = mid - 1

    return end

print(max_len(arr, M))