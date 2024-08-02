N = int(input())
arr = list(map(int, input().split()))
dp_inc = [1] * N
dp_dec = [1] * N
for i in range(1, N):
    if arr[i] > arr[i-1]:
        dp_inc[i] = dp_inc[i-1] + 1
        dp_dec[i] = 1
    elif arr[i] < arr[i-1]:
        dp_dec[i] = dp_dec[i-1] + 1
        dp_inc[i] = 1
    else:
        dp_inc[i] = dp_inc[i-1] + 1
        dp_dec[i] = dp_dec[i-1] + 1
print(max(max(dp_inc), max(dp_dec)))