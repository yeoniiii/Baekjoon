l, u = map(int, input().split())
arr = []
for i in range(1, 100):
    for j in range(i):
        arr.append(i)
print(sum(arr[l-1:u]))