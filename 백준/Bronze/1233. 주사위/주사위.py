S1, S2, S3 = map(int, input().split())
d = {}
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            if i+j+k in d:
                d[i+j+k] += 1
            else:
                d[i+j+k] = 1

max_bin = max(d.values())
max_num = []
for key, val in d.items():
    if val == max_bin:
        max_num.append(key)
print(min(max_num))