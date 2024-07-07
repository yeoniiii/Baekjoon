from itertools import permutations

find = 0
arr = []
for i in range(6):
    arr.append(input())

for a in permutations(arr, 3):
    arr3 = []
    for i in range(3):
        arr3.append(a[i])
    for i in range(3):
        arr3.append(a[0][i] + a[1][i] + a[2][i])
    if sorted(arr) == sorted(arr3):
        find = 1
        break
if find == 1:
    print(*arr3[:3], sep='\n')
else:
    print(0)