n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())
start, end = 0, n-1
num = 0

while start < end:
    s = arr[start] + arr[end]
    if s == x:
        num += 1
        start += 1
    elif s > x:
        end -= 1
    else:
        start += 1

print(num)