while True:
    route, Z = input().split()
    Z = int(Z) # size
    if Z == 0:
        break
    P = int(input()) # init num
    S = int(input()) # stop num
    for i in range(S):
        off, on = map(int, input().split())
        P -= off
        if Z - P >= on:
            P += on
        else:
            P = Z

    print(route, P)