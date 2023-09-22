arr = list(map(int, input().split()))

for n in range(1,10000000):
    num = 0
    for a in arr:
        if n % a == 0:
            num += 1
    if num >= 3:
        print(n)
        break