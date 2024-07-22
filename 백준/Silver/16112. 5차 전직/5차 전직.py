n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

ans, j = 0, 0
for i in range(n):
    ans += arr[i] * j
    if j < k:
        j += 1
print(ans)