T = int(input())
for i in range(T):
    q = divmod(int(input()), 25)
    d = divmod(q[1], 10)
    n = divmod(d[1], 5)
    print(q[0], d[0], n[0], n[1])
