i = 1
while True:
    l, p, v = map(int, input().split())
    if l == p == v == 0:
        break
    ans = (v // p) * l + min(l, v % p)
    print("Case "+str(i)+": "+str(ans))
    i += 1