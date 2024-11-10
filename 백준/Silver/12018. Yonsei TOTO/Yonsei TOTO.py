n, m = map(int, input().split())

arr = []
for _ in range(n):
    P, L = map(int, input().split())
    mileage = sorted(list(map(int, input().split())), reverse=True)
    if P < L:
        arr.append(1)
    else:
        arr.append(mileage[L-1])
        
arr.sort()
cnt = 0
for a in arr:
    if m - a >= 0:
        cnt += 1
        m -= a
print(cnt)