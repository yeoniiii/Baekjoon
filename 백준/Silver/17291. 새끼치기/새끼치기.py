N = int(input())
arr = [[0] * 3, [0] * 4]
arr[0][0] = 1

for i in range(2, N+1):
    num = sum(arr[0]) + sum(arr[1])
    if i % 2 == 0:
        arr[1][1], arr[1][2], arr[1][3] = arr[1][0], arr[1][1], arr[1][2]
        arr[0][0], arr[0][1], arr[0][2] = 0, arr[0][0], arr[0][1]
        arr[1][0] = num
    else:
        arr[0][1], arr[0][2] = arr[0][0], arr[0][1]
        arr[1][0], arr[1][1], arr[1][2], arr[1][3] = 0, arr[1][0], arr[1][1], arr[1][2]
        arr[0][0] = num

print(sum(arr[0]) + sum(arr[1]))