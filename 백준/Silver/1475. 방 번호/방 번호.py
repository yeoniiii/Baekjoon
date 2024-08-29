N = input()
d = {}
for n in N:
    if n == '6' or n == '9':
        if 9 in d:
            d[9] += 1
        else:
            d[9] = 1
    elif int(n) in d:
        d[int(n)] += 1
    else:
        d[int(n)] = 1
if 9 in d:
    if d[9] % 2 == 1:
        d[9] = d[9] // 2 + 1
    else:
        d[9] = d[9] // 2
print(max(d.values()))