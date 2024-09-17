A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

def gcd(x, y):
    mod = x % y
    while mod > 0:
        x, y = y, mod
        mod = x % y
    return y

A = A1*B2 + A2*B1
B = B1*B2
N = gcd(A, B)

print(A//N, B//N)