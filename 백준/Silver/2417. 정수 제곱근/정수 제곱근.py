n = int(input())

l, r = 0, n
min_n = n+1

while l <= r:
    mid = (l + r) // 2

    if mid**2 < n:
        l = mid + 1
    elif mid**2 > n:
        r = mid - 1
        min_n = min(min_n, mid)
    else:
        print(mid)
        break

if l > r:
    print(min_n)