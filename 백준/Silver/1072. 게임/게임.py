X, Y = map(int, input().split())
Z = (100*Y)//X

l, r = 0, X
ans = X
if Z >= 99:
    print(-1)
else:
    while l <= r:
        mid = (l+r)//2
        if (100*(Y+mid))//(X+mid) > Z:
            ans = mid
            r = mid-1
        else:
            l = mid+1
    print(ans)