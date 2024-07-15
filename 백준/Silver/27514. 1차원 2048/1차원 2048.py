import math

N = int(input())
arr = sorted(list(map(int, input().split())))
d = {}
for i in range(63):
    d[i] = 0
for a in arr:
    if a == 0:
        continue
    d[int(math.log2(a))] += 1
for key, value in d.items():
    if value == 0:
        continue
    if value // 2 > 0:
        d[key] -= (value // 2) * 2
        d[key+1] += value // 2
max_value = 0
for key, value in d.items():
    if value >= max_value:
        max_value = value
        max_num = key
print(2**max_num)