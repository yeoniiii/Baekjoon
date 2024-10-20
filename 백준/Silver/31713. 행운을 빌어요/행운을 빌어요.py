import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    ans = 0
    while 4*A < B:
        A += 1
        ans += 1
    if 3*A > B:
        ans += 3*A-B
    print(ans)