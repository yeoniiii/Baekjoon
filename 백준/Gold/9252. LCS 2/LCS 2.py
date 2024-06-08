a = input()
b = input()

arr = [[0] * (len(b)+1) for i in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i][j-1], arr[i-1][j])

i, j = len(a), len(b)
num = arr[i][j]
lcs = ''

while i >= 0 and j >= 0:
    if arr[i-1][j] == arr[i][j]:
        i -= 1
    elif arr[i][j-1] == arr[i][j]:
        j -= 1
    else:
        lcs += a[i-1]
        i -= 1
        j -= 1

print(num)
if num > 0:
    print(lcs[::-1])