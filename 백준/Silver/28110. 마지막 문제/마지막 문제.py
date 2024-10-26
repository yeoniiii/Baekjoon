n = int(input())
arr = list(map(int, input().split()))
arr.sort()
    
temp, x = 0, 0

for i in range(n - 1):
    target = (arr[i] + arr[i + 1]) // 2
    if target != arr[i]:
        diff = min(target - arr[i], arr[i + 1] - target)
        if diff > x:
            temp = target
            x = diff

if temp == 0:
    print(-1)
else:
    print(temp)