X, Y, P1, P2 = map(int, input().split())
find = False
cnt = 0
k = P1
while cnt < 500:
    if k >= P2 and (k-P2)%Y == 0:
        find = True
        break
    k += X
    cnt += 1
if find:
    print(k)
else:
    print(-1)