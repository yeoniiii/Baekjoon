import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for t in range(T):
    x1, y1, x2, y2 = list(map(int, input().split()))
    N = int(input())
    cnt = 0
    for n in range(N):
        cx, cy, cr = map(int, input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2
        d2 = (x2-cx)**2 + (y2-cy)**2
        cr2 = cr**2
        if cr2 > d1 and cr2 > d2:
            pass
        elif cr2 > d1:
            cnt += 1
        elif cr2 > d2:
            cnt += 1
    print(cnt)