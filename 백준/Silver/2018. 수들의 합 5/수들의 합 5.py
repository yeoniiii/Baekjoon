N = int(input())

num = 0
l, r = 1, 2
s = l
while True:
    if s < N:
        if r <= N:
            s += r
            r += 1
        else:
            break
    elif s == N:
        num += 1
        s -= l
        l += 1
    else:
        s -= l
        l += 1
print(num)