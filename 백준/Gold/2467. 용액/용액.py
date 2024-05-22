N = int(input())
arr = list(map(int, input().split()))

l, r = 0, 1
min_sum = 10**10
start, end = arr[l], arr[-r]

while start < end:
    mid = (start + end)
    if abs(mid) < min_sum:
        min_sum = abs(mid)
        a, b = start, end
    if mid < 0:
        l += 1
        start = arr[l]
    else:
        r += 1
        end = arr[-r]
print(a, b)