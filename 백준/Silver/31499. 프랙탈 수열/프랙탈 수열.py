N, M = map(int, input().split())
ans = 1
for i in range(1, N+1):
    ans *= i
print(ans%M)