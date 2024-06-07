a = input()
b = input()

arr = [[0] * (len(b)+1) for i in range(len(a)+1)]
num = 0

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            arr[i][j] += 1 + arr[i-1][j-1]
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])

print(arr[len(a)][len(b)])