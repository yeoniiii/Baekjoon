N = int(input())
M = int(input())

def C(n, r):
    r = min(r, n-r)
    num = denom = 1
    for i in range(r):
        num *= n-i
        denom *= i+1
    return num // denom

print(C(N+M-1-N, M-N))