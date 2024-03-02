N = int(input())
arr = list(map(int, input().split()))
num = [1] * N

if N >= 2:
    for i in range(1, N):
        j, max_num = 1, 0
        while i-j >= 0:
            if arr[i] > arr[i-j] and max_num < num[i-j]:
                max_num = num[i-j]
                num[i] = max_num + 1
            j+=1

print(max(num))