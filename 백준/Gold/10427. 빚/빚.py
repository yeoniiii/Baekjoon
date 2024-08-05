T = int(input())

def S(n):
    global N
    min_diff = 10**9
    for i in range(n-1, N):
        cs_i = cumsum[i+1]-cumsum[i-n+1]
        diff_i = A[i]*n - cs_i
        if diff_i < min_diff:
            min_diff = diff_i
    return min_diff

for t in range(T):
    A = list(map(int, input().split()))
    N = A.pop(0)
    A.sort()
    cumsum = [0]
    for i in range(N):
        cumsum.append(cumsum[-1] + A[i])
    ans = 0
    for n in range(1, N+1):
        ans += S(n)
    print(ans)