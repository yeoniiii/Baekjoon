while True:
    N = int(input())
    if N == 0:
        break
    else:
        S = "".join(input().upper().split())
    
    d = {}
    i, m, cnt = 0, 0, 0
    while len(d) != len(S):
        if i >= len(S):
            cnt += 1
            i = cnt
        d[i] = S[m]
        i += N
        m += 1
    d = sorted(d.items(), key=lambda x: x[0])

    for i in d:
        print(i[1], end="")
    print()
    