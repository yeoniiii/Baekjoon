arr = []
N = int(input())
for i in range(N):
    a, b = input().split()
    arr.append([int(a), b])
sorted_arr = sorted(arr, key=lambda x:(x[0]))

for j in range(N):
    print(sorted_arr[j][0], sorted_arr[j][1])

