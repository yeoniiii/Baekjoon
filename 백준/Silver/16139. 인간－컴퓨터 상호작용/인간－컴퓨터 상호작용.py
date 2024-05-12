s = input()
q = int(input())
for i in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    num, cur = 0, l
    while cur <= r:
        if s[cur] == a:
            num += 1
        cur += 1
    print(num)