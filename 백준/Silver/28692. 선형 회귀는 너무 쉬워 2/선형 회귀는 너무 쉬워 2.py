import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
Sx, Sy, Sxx, Sxy = 0, 0, 0, 0
for i in range(n):
    x, y = map(int, input().split())
    Sx += x
    Sy += y
    Sxx += x**2
    Sxy += x*y
if Sx**2 == n*Sxx:
    print("EZPZ")
else:
    a = (n*Sxy - Sx*Sy)/(n*Sxx - Sx**2)
    b = (Sy - a*Sx)/n
    print(a, b)
