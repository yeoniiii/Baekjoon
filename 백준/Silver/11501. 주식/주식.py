import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    N = int(input())
    price = list(map(int, input().split()))
    loc_max_p = price[N-1]
    max_p = [loc_max_p]
    for i in range(2, N+1):
        if price[N-i] >= loc_max_p:
            loc_max_p = price[N-i]
        max_p.append(loc_max_p)
    max_p = max_p[::-1]
    profit = 0

    for i in range(N):
        profit += max_p[i] - price[i]

    print(profit)