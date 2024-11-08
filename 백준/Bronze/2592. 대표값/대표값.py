arr = {}
for i in range(10):
    n = int(input())
    if n in arr:
        arr[n] += 1
    else:
        arr[n] = 1
ans_mean, ans_mode = 0, 0
max_mode = max(arr.values())
for key, val in arr.items():
    ans_mean += key*val
    if val == max_mode:
        ans_mode = key
print(ans_mean//10)
print(ans_mode)
