N = int(input())
arr = sorted(list(map(int, input().split())))

while len(arr) > 1:
    arr[-1] += arr.pop(0) / 2
print(arr[0])