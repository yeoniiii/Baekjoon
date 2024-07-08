c = list(map(int, input().split()))
x1, x2, x3, x5, x6, x7 = 0, 0, 0, 0, 0, 0
for i in range(2, c[0]):
    if c[0] % i == 0:
        x1, x2 = i, c[0]//i
        if c[4] % x2 == 0:
            x3 = c[4] // x2
            if x1 != x3:
                break
for i in range(2, int(min(c[2], c[5]))):
    if c[2] % i == 0 and c[5] % i == 0:
        x6 = i
        x5, x7 = c[5]//x6, c[2]//x6
        if x5 != x7:
            break
print(x1, x2, x3, x5, x6, x7)