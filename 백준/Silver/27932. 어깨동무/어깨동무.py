n, k = map(int, input().split())
heights = list(map(int, input().split()))

start, end = 0, max(heights)
while start <= end:
    mid = (start+end)//2
    tired = [0] * n
    for i in range(1, n):
        if abs(heights[i] - heights[i-1]) > mid:
            tired[i-1] = 1
            tired[i] = 1
    if sum(tired) <= k:
        H = mid
        end = mid-1
    else:
        start = mid+1
print(H)