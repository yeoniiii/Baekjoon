A, B = map(int, input().split())
denom = 18*17/2

if A == B:
    print(f"{1-(10-A)/denom:.3f}")
else:
    yh = (A+B)%10
    num = 0
    for i in range(0, yh):
        if i % 2 == 0:
            num += 12
            if (A*2)%10 == i:
                num += 2
            if (B*2)%10 == i:
                num += 2
        else:
            num += 16
    print(f"{num/denom:.3f}")