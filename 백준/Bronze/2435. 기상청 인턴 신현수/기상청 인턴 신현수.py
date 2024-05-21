N, K = map(int, input().split())
arr = list(map(int, input().split()))

sum_i = sum(arr[0:K])
max_sum = -10**6
start, end = 0, K
while True:
    if sum_i >= max_sum:
        max_sum = sum_i
    if end < N:
        sum_i -= arr[start]
        sum_i += arr[end]
        start += 1
        end += 1
    else:
        break
print(max_sum)